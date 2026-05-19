#!/usr/bin/env python3
"""
ITWeb Security Summit — Master PDF generator.
Chapters: EU, NA, AF, AS, AU, SA.  Filter: % fit >= 0.7 (n/a rows kept).
Index covers: perpetrators, countries, taxonomy codes, key techniques.
"""
import re
from pathlib import Path
from collections import defaultdict

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Flowable,
    Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, NextPageTemplate,
)
from reportlab.platypus.tableofcontents import TableOfContents

# ── Paths & settings ──────────────────────────────────────────────────────────
BASE    = Path('C:/Users/steph/OneDrive/Documents/GitHub/ITWeb')
OUT     = BASE / 'ITWeb_Hybrid_Incidents.pdf'
IDIR    = BASE / 'all_incidents'
XDIR    = BASE / 'country_indexes'
MIN_FIT = 0.7
W, H    = A4

CONTINENTS = [
    ('EU', 'Europe'),
    ('NA', 'North America'),
    ('AF', 'Africa'),
    ('AS', 'Asia'),
    ('AU', 'Australia / Oceania'),
    ('SA', 'South America'),
]

# ── Palette ───────────────────────────────────────────────────────────────────
NAVY  = colors.HexColor('#1b3a6b')
NAVYL = colors.HexColor('#2a4a7f')
ICE   = colors.HexColor('#eaf1fb')
F3    = colors.HexColor('#f3f6fb')
F6    = colors.HexColor('#f6f8fa')
BORD  = colors.HexColor('#d0d7de')
DARK  = colors.HexColor('#24292e')
MID   = colors.HexColor('#555555')

# ── Styles ────────────────────────────────────────────────────────────────────
def _ps(name, **kw):
    defaults = dict(fontName='Helvetica', fontSize=9, leading=13,
                    textColor=DARK, spaceBefore=0, spaceAfter=0)
    defaults.update(kw)
    return ParagraphStyle(name, **defaults)

S = {
    'body'  : _ps('body'),
    'bodyJ' : _ps('bodyJ', alignment=TA_JUSTIFY),
    'small' : _ps('small', fontSize=7, leading=10, textColor=MID),
    'bold'  : _ps('bold', fontName='Helvetica-Bold'),
    'h1'    : _ps('h1', fontName='Helvetica-Bold', fontSize=26, leading=32,
                  textColor=colors.white, alignment=TA_CENTER),
    'h1sub' : _ps('h1sub', fontSize=13, leading=18,
                  textColor=colors.HexColor('#a8c8ff'), alignment=TA_CENTER),
    'h2'    : _ps('h2', fontName='Helvetica-Bold', fontSize=15, leading=20,
                  textColor=colors.white),
    'h3'    : _ps('h3', fontName='Helvetica-Bold', fontSize=10, leading=14,
                  textColor=NAVY, spaceBefore=8, spaceAfter=4),
    'bullet': _ps('bullet', leftIndent=10, spaceBefore=1, spaceAfter=1),
    'center': _ps('center', alignment=TA_CENTER),
    'toc0'  : _ps('toc0', fontName='Helvetica-Bold', fontSize=11, leading=16,
                  textColor=NAVY, spaceBefore=6),
    'toc1'  : _ps('toc1', fontSize=9, leading=13, leftIndent=14, textColor=DARK),
    'toc2'  : _ps('toc2', fontSize=8, leading=11, leftIndent=28, textColor=MID),
    'idx_h' : _ps('idx_h', fontName='Helvetica-Bold', fontSize=10, leading=14,
                  textColor=NAVY, spaceBefore=10, spaceAfter=2),
    'idx_e' : _ps('idx_e', fontSize=8, leading=11, leftIndent=10),
    'th'    : _ps('th', fontName='Helvetica-Bold', fontSize=7, leading=9,
                  textColor=colors.white),
    'td'    : _ps('td', fontSize=7, leading=9, textColor=DARK),
    'td_sm' : _ps('td_sm', fontSize=6.5, leading=8.5, textColor=DARK),
    'ref'   : _ps('ref', fontSize=7.5, leading=11, textColor=MID,
                  leftIndent=12, firstLineIndent=-12),
}

# ── Markdown → safe XML text ──────────────────────────────────────────────────
def _xml(text):
    """Escape & then apply bold/italic/link markdown to XML markup."""
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    text = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*([^*]+)\*',     r'<i>\1</i>', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)   # strip links
    text = re.sub(r'`([^`]+)`', r'<font name="Courier" fontSize="7">\1</font>', text)
    return text

def _plain(text):
    """Markdown → plain text."""
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*',     r'\1', text)
    return text.strip()

# ── Index tracking flowable ───────────────────────────────────────────────────
class IndexMark(Flowable):
    """Zero-height flowable: records page numbers for index terms."""
    def __init__(self, terms, store):
        super().__init__()
        self.terms = terms   # list of (category, term)
        self.store = store   # defaultdict(set)
        self.width = self.height = 0

    def draw(self):
        pg = self.canv.getPageNumber()
        for cat, term in self.terms:
            self.store[(cat, term)].add(pg)

    def wrap(self, aw, ah):
        return 0, 0

# ── TOC bookmark flowable ─────────────────────────────────────────────────────
class Bookmark(Flowable):
    def __init__(self, name, level, text, toc):
        super().__init__()
        self.name  = name
        self.level = level
        self.text  = text
        self.toc   = toc
        self.width = self.height = 0

    def draw(self):
        self.canv.bookmarkPage(self.name)
        self.toc.notify('TOCEntry', (self.level, self.text,
                                      self.canv.getPageNumber(), self.name))

    def wrap(self, aw, ah):
        return 0, 0

# ── Parse classification index ────────────────────────────────────────────────
def parse_index(prefix):
    path = XDIR / f'{prefix}-classification.md'
    raw  = path.read_text(encoding='utf-8')
    raw  = re.sub(r'^---.*?---\s*', '', raw, flags=re.DOTALL)
    raw  = re.sub(r'<div[^>]*>.*?</div>', '', raw, flags=re.DOTALL)
    raw  = re.sub(r'<script[^>]*>.*?</script>', '', raw, flags=re.DOTALL)

    lines = raw.splitlines()
    title = ''; intro = []; observations = []; rows = []
    in_table = False; in_obs = False; after_fit_block = False

    for line in lines:
        s = line.strip()
        if not title and s.startswith('# '):
            title = s[2:].strip(); continue
        if s.startswith('## Continental observations'):
            in_table = False; in_obs = True; continue
        if in_obs:
            if s.startswith('- '): observations.append(s[2:])
            continue
        if s.startswith('| ID |'):
            in_table = True; continue
        if in_table and s.startswith('|---'):
            continue
        if in_table and s.startswith('|'):
            cells = [c.strip() for c in s.split('|')[1:-1]]
            if len(cells) < 8:
                continue
            fit_raw = cells[7].strip()
            try:    fit = float(fit_raw)
            except: fit = None
            tm = re.match(r'\[([^\]]+)\]\(\.\.(/[^)]+)\)', cells[1])
            inc_title = tm.group(1) if tm else _plain(cells[1])
            # Derive filename from link or from ID + title
            if tm:
                fn = Path(tm.group(2).lstrip('/'))
                filepath = BASE / fn
            else:
                filepath = None
            rows.append({
                'id': cells[0], 'title': inc_title,
                'filepath': filepath,
                'country': _plain(cells[2]), 'primary': _plain(cells[3]),
                'secondary': _plain(cells[4]), 'perpetrator': _plain(cells[5]),
                'victim': _plain(cells[6]), 'fit': fit, 'fit_raw': fit_raw,
            })
            continue
        if in_table and not s.startswith('|'):
            in_table = False
        # Intro paragraphs (skip % fit legend lines for brevity)
        if s and not s.startswith('#') and not s.startswith('|') \
                and 'fit' not in s.lower()[:20]:
            if s.startswith('- ') or s.startswith('* '):
                intro.append(('bullet', s[2:]))
            elif not s.startswith('The **% fit**') and not s.startswith('- **1.0**') \
                    and not s.startswith('- **0.7') and not s.startswith('- **≤') \
                    and not s.startswith('- **Type'):
                intro.append(('para', s))

    filtered = [r for r in rows if r['fit'] is None or r['fit'] >= MIN_FIT]
    return {'title': title, 'intro': intro, 'rows': filtered,
            'all_rows': rows, 'observations': observations}

# ── Parse incident file ───────────────────────────────────────────────────────
def parse_incident(filepath):
    raw     = Path(filepath).read_text(encoding='utf-8')
    raw     = re.sub(r'^---.*?---\s*', '', raw, flags=re.DOTALL)
    lines   = raw.splitlines()
    result  = {'title': '', 'kv': [], 'cyber': [], 'disinfo': [], 'refs': []}
    section = None

    for line in lines:
        s = line.strip()
        if   s.startswith('## Incident Summary'):   section = 'sum'
        elif s.startswith('## Cyberattack'):         section = 'cyber'
        elif s.startswith('## Disinformation'):      section = 'disinfo'
        elif s.startswith('## References'):          section = 'refs'
        elif s.startswith('## '):                    section = None
        elif not s: continue

        if section == 'sum':
            m = re.match(r'\*\*Title:\*\*\s*(.*)', s)
            if m: result['title'] = _plain(m.group(1)); continue
            m = re.match(r'\*\*([^*]+):\*\*\s*(.*)', s)
            if m:
                val = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', m.group(2))
                val = re.sub(r'\*\*([^*]+)\*\*', r'\1', val)
                result['kv'].append((m.group(1), val.strip()))
        elif section == 'cyber' and s.startswith('- '):
            result['cyber'].append(s[2:])
        elif section == 'disinfo' and s.startswith('- '):
            result['disinfo'].append(s[2:])
        elif section == 'refs':
            m = re.match(r'\[(\d+)\]\(([^)]+)\):\s*(.*)', s)
            if m:
                result['refs'].append({'num': m.group(1), 'url': m.group(2),
                                       'text': _plain(m.group(3))})

    return result

# ── Index term extraction ─────────────────────────────────────────────────────
TECHNIQUES = [
    'ransomware', 'spearphishing', 'phishing', 'vishing', 'deepfake',
    'hack-and-leak', 'DDoS', 'wiper', 'hack-and-post', 'defacement',
    'coordinated inauthentic behaviour', 'CIB', 'impersonation',
    'double-extortion', 'social engineering', 'false flag',
    'hack-and-destroy', 'disinformation', 'data exfiltration',
]
TAXONOMY_RE = re.compile(r'\b([12][a-h])\b')
_SKIP = {'the','and','or','of','in','at','by','a','an','to','for','with',
         'on','from','is','its','are','as','via','their','that','this',
         'plus','wider','multiple','broader','various','several','other',
         'north','south','east','west','central','type','per'}

def extract_terms(row, incident):
    terms = []
    # Taxonomy codes
    for field in [row['primary'], row['secondary']]:
        for m in TAXONOMY_RE.finditer(field):
            terms.append(('Taxonomy codes', m.group(1).upper()))
    # 'Type 3' / '3 –' style
    if re.search(r'\b3\s*[–-]', row['primary']):
        terms.append(('Taxonomy codes', '3'))

    # Perpetrators — strip parentheticals, split on commas/slashes
    perp = re.sub(r'\s*\([^)]+\)', '', row['perpetrator'])
    for p in re.split(r'[,;/]', perp):
        p = p.strip()
        low = p.lower()
        if len(p) > 3 and low not in ('mixed','uncertain','domestic',
                                       'not applicable','western governments'):
            terms.append(('Perpetrators', p))

    # Countries — split country/scope on commas and common separators
    for seg in re.split(r'[,;()\[\]/]', row['country']):
        seg = seg.strip()
        words = [w for w in seg.split() if w.lower() not in _SKIP and len(w) > 1]
        candidate = ' '.join(words).strip()
        if 2 < len(candidate) <= 40:
            terms.append(('Countries', candidate))

    # Techniques — scan full text
    full = ' '.join([
        row['primary'], row['secondary'],
        ' '.join(b for b in incident['cyber'] + incident['disinfo']),
    ]).lower()
    for kw in TECHNIQUES:
        if kw.lower() in full:
            terms.append(('Techniques', kw))

    return terms

# ── Page template (header + footer) ──────────────────────────────────────────
MARGIN = 18 * mm

def _header_footer(canv, doc):
    canv.saveState()
    pg = doc.page
    if pg > 2:
        # Header strip
        canv.setFillColor(NAVY)
        canv.rect(MARGIN, H - MARGIN - 5.5*mm,
                  W - 2*MARGIN, 5.5*mm, fill=1, stroke=0)
        canv.setFillColor(colors.white)
        canv.setFont('Helvetica', 6.5)
        canv.drawString(MARGIN + 2*mm, H - MARGIN - 3.8*mm,
                        'ITWeb Security Summit — Hybrid Cyber / FIMI Incidents')
        canv.drawRightString(W - MARGIN - 2*mm, H - MARGIN - 3.8*mm,
                             'For Research Use')
        # Footer rule + page number
        canv.setStrokeColor(BORD)
        canv.setLineWidth(0.4)
        canv.line(MARGIN, MARGIN + 2*mm, W - MARGIN, MARGIN + 2*mm)
        canv.setFillColor(MID)
        canv.setFont('Helvetica', 7)
        canv.drawString(MARGIN, MARGIN - 1*mm, f'% fit ≥ {MIN_FIT}')
        canv.drawRightString(W - MARGIN, MARGIN - 1*mm, f'{pg}')
    canv.restoreState()

def make_doc(toc):
    doc = BaseDocTemplate(
        str(OUT), pagesize=A4,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN + 7*mm, bottomMargin=MARGIN + 7*mm,
        title='ITWeb Security Summit — Hybrid Cyber/FIMI Incidents',
        author='ITWeb Security Summit',
        subject='Hybrid cyber and FIMI incident classification',
    )
    frame = Frame(MARGIN, MARGIN + 7*mm,
                  W - 2*MARGIN, H - 2*MARGIN - 14*mm,
                  id='main', showBoundary=0)
    doc.addPageTemplates([
        PageTemplate(id='main', frames=[frame], onPage=_header_footer),
    ])
    return doc

# ── Flowable builders ─────────────────────────────────────────────────────────
CW = W - 2*MARGIN   # usable content width

def chap_banner(text):
    t = Table([[Paragraph(text, S['h2'])]],
              colWidths=[CW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVY),
        ('LEFTPADDING',   (0,0), (-1,-1), 10),
        ('RIGHTPADDING',  (0,0), (-1,-1), 10),
        ('TOPPADDING',    (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    return t

def sec_banner(text):
    t = Table([[Paragraph(text, _ps('_sh', fontName='Helvetica-Bold',
                                    fontSize=8.5, leading=12,
                                    textColor=colors.white))]],
              colWidths=[CW])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), NAVYL),
        ('LEFTPADDING',   (0,0), (-1,-1), 8),
        ('TOPPADDING',    (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    return t

def kv_block(kvlist, key_w=50*mm):
    if not kvlist:
        return []
    data = []
    for key, val in kvlist:
        val_xml = _xml(val)
        data.append([
            Paragraph(f'<b>{_xml(key)}</b>', S['body']),
            Paragraph(val_xml, S['body']),
        ])
    t = Table(data, colWidths=[key_w, CW - key_w])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (0,-1), F3),
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING',   (0,0), (-1,-1), 6),
        ('RIGHTPADDING',  (0,0), (-1,-1), 6),
        ('TOPPADDING',    (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW',     (0,0), (-1,-2), 0.3, BORD),
        ('BOX',           (0,0), (-1,-1), 0.5, BORD),
    ]))
    return [t]

def bullet_block(bullets):
    if not bullets:
        return []
    data = []
    for b in bullets:
        m = re.match(r'\*\*([^*]+):\*\*\s*(.*)', b, re.DOTALL)
        if m:
            key = _xml(m.group(1))
            val = _xml(re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', m.group(2)))
            xml = f'<b>{key}:</b> {val}'
        else:
            xml = _xml(re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', b))
        data.append([Paragraph('•', S['body']), Paragraph(xml, S['body'])])
    t = Table(data, colWidths=[5*mm, CW - 5*mm])
    t.setStyle(TableStyle([
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING',   (0,0), (0,-1), 3),
        ('RIGHTPADDING',  (0,0), (-1,-1), 4),
        ('TOPPADDING',    (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ROWBACKGROUNDS',(0,0), (-1,-1), [colors.white, F6]),
    ]))
    return [t]

def ref_block(refs):
    if not refs:
        return []
    out = [Paragraph('<b>References</b>', S['h3'])]
    for r in refs:
        out.append(Paragraph(
            f'[{r["num"]}] {_xml(r["text"])} — <i>{r["url"]}</i>',
            S['ref']))
    return out

def class_table(rows):
    """Render filtered classification table."""
    if not rows:
        return [Paragraph(
            '<i>No incidents meet the % fit ≥ 0.7 threshold for this region.</i>',
            S['body'])]
    # Column widths summing to CW
    cw = [10*mm, 52*mm, 26*mm, 42*mm, 38*mm, 36*mm, 26*mm, 10*mm]
    scale = CW / sum(cw)
    cw = [c * scale for c in cw]

    hdr = ['ID', 'Incident', 'Country/Scope', 'Primary Type',
           'Secondary Type(s)', 'Perpetrator', 'Victim Category', '% Fit']
    data = [[Paragraph(h, S['th']) for h in hdr]]
    for r in rows:
        fit_s = 'n/a' if r['fit'] is None else f"{r['fit']:.1f}"
        data.append([
            Paragraph(r['id'],          S['td']),
            Paragraph(_xml(r['title']), S['td_sm']),
            Paragraph(_xml(r['country']),     S['td_sm']),
            Paragraph(_xml(r['primary']),     S['td_sm']),
            Paragraph(_xml(r['secondary']) if r['secondary'] else '—', S['td_sm']),
            Paragraph(_xml(r['perpetrator']), S['td_sm']),
            Paragraph(_xml(r['victim']),      S['td_sm']),
            Paragraph(fit_s,            S['td']),
        ])
    rbs = [('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, F6])]
    t = Table(data, colWidths=cw, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  NAVY),
        ('BACKGROUND',    (0,1), (-1,-1), colors.white),
        ('VALIGN',        (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING',   (0,0), (-1,-1), 3),
        ('RIGHTPADDING',  (0,0), (-1,-1), 3),
        ('TOPPADDING',    (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('GRID',          (0,0), (-1,-1), 0.3, BORD),
        ('LINEBELOW',     (0,0), (-1,0),  1,   NAVY),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [colors.white, F6]),
    ]))
    return [t]

# ── Cover page ────────────────────────────────────────────────────────────────
def cover_page():
    story = []
    story.append(Spacer(1, 40*mm))
    # Full-width navy banner
    banner_data = [[
        Paragraph('ITWeb Security Summit', S['h1']),
    ]]
    bt = Table(banner_data, colWidths=[CW])
    bt.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,-1), NAVY),
        ('TOPPADDING',    (0,0), (-1,-1), 20),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(bt)

    sub_data = [[
        Paragraph('Hybrid Cyber / FIMI Incidents', S['h1sub']),
    ]]
    st = Table(sub_data, colWidths=[CW])
    st.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,-1), NAVYL),
        ('TOPPADDING',    (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 16),
    ]))
    story.append(st)
    story.append(Spacer(1, 18*mm))

    desc_rows = [
        ['Global Classification by Continent'],
        [f'Incidents with % fit ≥ {MIN_FIT} · All six continents'],
        ['Taxonomy: Cyber-enabled influence · Influence-enabled cyber · Parallel operations'],
        [''],
        ['Prepared for the ITWeb Security Summit'],
        ['2026'],
    ]
    for i, (row,) in enumerate(desc_rows):
        sty = 'bold' if i in (0,) else 'center'
        story.append(Paragraph(row, S['center_bold' if i==0 else 'center']
                                if hasattr(S.get('center_bold', None), '__class__')
                                else S['center']))
        story.append(Spacer(1, 2*mm))

    story.append(Spacer(1, 30*mm))
    # Thin rule
    rule_data = [['']]
    rt = Table(rule_data, colWidths=[CW])
    rt.setStyle(TableStyle([
        ('LINEABOVE', (0,0), (-1,-1), 2, NAVY),
    ]))
    story.append(rt)
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph(
        'This document contains all incidents classified with a % fit score of '
        f'{MIN_FIT} or above. Rows marked <i>n/a</i> are placeholder entries '
        'representing continents where no qualifying incidents were documented.',
        S['small']))
    story.append(PageBreak())
    return story

# ── Build cover descriptions separately (avoid earlier confusion) ─────────────
_CB = ParagraphStyle('center_bold', fontName='Helvetica-Bold', fontSize=13,
                     leading=18, textColor=NAVY, alignment=TA_CENTER)

def cover_page_v2():
    story = []
    story.append(Spacer(1, 35*mm))
    banner = Table([[Paragraph('ITWeb Security Summit', S['h1'])]],
                   colWidths=[CW])
    banner.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), NAVY),
        ('TOPPADDING',    (0,0),(-1,-1), 22),
        ('BOTTOMPADDING', (0,0),(-1,-1), 8),
    ]))
    story.append(banner)
    sub = Table([[Paragraph('Hybrid Cyber / FIMI Incidents', S['h1sub'])]],
                colWidths=[CW])
    sub.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), NAVYL),
        ('TOPPADDING',    (0,0),(-1,-1), 8),
        ('BOTTOMPADDING', (0,0),(-1,-1), 18),
    ]))
    story.append(sub)
    story.append(Spacer(1, 16*mm))
    story.append(Paragraph('Global Classification by Continent', _CB))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph(
        f'Incidents with % fit ≥ {MIN_FIT}  ·  Six continents', S['center']))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph(
        'Taxonomy: Cyber-enabled influence  ·  Influence-enabled cyber  ·  '
        'Parallel operations', S['center']))
    story.append(Spacer(1, 20*mm))
    rule = Table([['']], colWidths=[CW])
    rule.setStyle(TableStyle([('LINEABOVE', (0,0),(-1,-1), 1.5, NAVY)]))
    story.append(rule)
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph('Prepared for the ITWeb Security Summit · 2026',
                            S['center']))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph(
        'This document includes all incidents with a % fit score of '
        f'{MIN_FIT} or above. Entries marked <i>n/a</i> represent continents '
        'where no qualifying incidents were documented in the source dataset.',
        S['small']))
    story.append(PageBreak())
    return story

# ── TOC page ──────────────────────────────────────────────────────────────────
def toc_page(toc):
    story = []
    story.append(chap_banner('Table of Contents'))
    story.append(Spacer(1, 6*mm))
    story.append(toc)
    story.append(PageBreak())
    return story

# ── Incident flowables ────────────────────────────────────────────────────────
def incident_story(row, incident, toc, index_store):
    story = []
    inc_id = row['id']

    # Bookmark + TOC entry (level 1)
    bm_key = f'inc_{inc_id}'
    story.append(Bookmark(bm_key, 1, f'{inc_id}: {incident["title"]}', toc))

    # Index mark
    terms = extract_terms(row, incident)
    story.append(IndexMark(terms, index_store))

    # Incident title bar (lighter than chapter banner)
    title_data = [[
        Paragraph(f'<b>{inc_id}</b>',                    S['small']),
        Paragraph(_xml(incident['title']),
                  _ps('_it', fontName='Helvetica-Bold', fontSize=9.5,
                      leading=13, textColor=NAVYL)),
        Paragraph(f'% fit: <b>{row["fit_raw"]}</b>', S['small']),
    ]]
    tt = Table(title_data, colWidths=[14*mm, CW - 36*mm, 22*mm])
    tt.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), ICE),
        ('LEFTPADDING',   (0,0),(-1,-1), 6),
        ('RIGHTPADDING',  (0,0),(-1,-1), 6),
        ('TOPPADDING',    (0,0),(-1,-1), 5),
        ('BOTTOMPADDING', (0,0),(-1,-1), 5),
        ('VALIGN',        (0,0),(-1,-1), 'MIDDLE'),
        ('BOX',           (0,0),(-1,-1), 0.5, BORD),
        ('ALIGN',         (2,0),(2,-1),  'RIGHT'),
    ]))
    story.append(tt)
    story.append(Spacer(1, 2*mm))

    # Summary key-value block
    story += kv_block(incident['kv'])
    story.append(Spacer(1, 3*mm))

    # Cyberattack details
    if incident['cyber']:
        story.append(sec_banner('Cyberattack Details'))
        story.append(Spacer(1, 1*mm))
        story += bullet_block(incident['cyber'])
        story.append(Spacer(1, 2*mm))

    # Disinformation details
    if incident['disinfo']:
        story.append(sec_banner('Disinformation Details'))
        story.append(Spacer(1, 1*mm))
        story += bullet_block(incident['disinfo'])
        story.append(Spacer(1, 2*mm))

    # References
    story += ref_block(incident['refs'])
    story.append(Spacer(1, 6*mm))
    return story

# ── Chapter flowables ─────────────────────────────────────────────────────────
def chapter_story(prefix, label, toc, index_store):
    story = []
    data = parse_index(prefix)
    story.append(PageBreak())

    # Chapter bookmark + TOC level 0
    bm = f'chap_{prefix}'
    story.append(Bookmark(bm, 0, f'Chapter: {label}', toc))
    story.append(chap_banner(label))
    story.append(Spacer(1, 5*mm))

    # Intro paragraphs
    for kind, text in data['intro']:
        if kind == 'bullet':
            story.append(Paragraph('• ' + _xml(text), S['bullet']))
        else:
            story.append(Paragraph(_xml(text), S['bodyJ']))
        story.append(Spacer(1, 1*mm))

    story.append(Spacer(1, 3*mm))
    story.append(Paragraph(
        f'<b>Incidents included (% fit ≥ {MIN_FIT}):</b> '
        f'{len(data["rows"])} of {len(data["all_rows"])}', S['body']))
    story.append(Spacer(1, 2*mm))

    # Classification table
    story += class_table(data['rows'])
    story.append(Spacer(1, 5*mm))

    # Continental observations
    if data['observations']:
        story.append(Paragraph('<b>Continental observations</b>', S['h3']))
        for obs in data['observations']:
            story.append(Paragraph('• ' + _xml(obs), S['bullet']))
            story.append(Spacer(1, 1*mm))

    # Incident detail pages
    for row in data['rows']:
        filepath = row['filepath']
        if filepath is None or not filepath.exists():
            # Try to find by ID prefix
            candidates = sorted(IDIR.glob(f'{row["id"]}-*.md'))
            if candidates:
                filepath = candidates[0]
        if filepath is None or not filepath.exists():
            continue
        incident = parse_incident(filepath)
        story.append(PageBreak())
        story += incident_story(row, incident, toc, index_store)

    return story

# ── Index page ────────────────────────────────────────────────────────────────
def index_story(index_store):
    story = []
    story.append(PageBreak())
    story.append(chap_banner('Index'))
    story.append(Spacer(1, 5*mm))

    # Group by category, sort entries
    by_cat = defaultdict(dict)
    for (cat, term), pages in index_store.items():
        sorted_pages = sorted(pages)
        by_cat[cat][term] = sorted_pages

    cat_order = ['Countries', 'Perpetrators', 'Taxonomy codes', 'Techniques']
    for cat in cat_order:
        if cat not in by_cat:
            continue
        story.append(Paragraph(cat, S['idx_h']))
        entries = sorted(by_cat[cat].items(), key=lambda x: x[0].lower())
        data = []
        for term, pages in entries:
            page_str = ', '.join(str(p) for p in pages)
            data.append([
                Paragraph(_xml(term), S['idx_e']),
                Paragraph(page_str, S['idx_e']),
            ])
        if data:
            t = Table(data, colWidths=[CW * 0.65, CW * 0.35])
            t.setStyle(TableStyle([
                ('VALIGN',        (0,0),(-1,-1), 'TOP'),
                ('LEFTPADDING',   (0,0),(-1,-1), 4),
                ('RIGHTPADDING',  (0,0),(-1,-1), 4),
                ('TOPPADDING',    (0,0),(-1,-1), 1),
                ('BOTTOMPADDING', (0,0),(-1,-1), 1),
                ('ROWBACKGROUNDS',(0,0),(-1,-1), [colors.white, F6]),
                ('ALIGN',         (1,0),(1,-1), 'RIGHT'),
            ]))
            story.append(t)
        story.append(Spacer(1, 4*mm))
    return story

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    print('Building PDF …')
    toc = TableOfContents()
    toc.levelStyles = [S['toc0'], S['toc1'], S['toc2']]
    toc.dotsMinLevel = 0

    index_store = defaultdict(set)

    story = []
    story += cover_page_v2()
    story += toc_page(toc)

    for prefix, label in CONTINENTS:
        print(f'  Chapter: {label}')
        story += chapter_story(prefix, label, toc, index_store)

    story += index_story(index_store)

    doc = make_doc(toc)
    doc.multiBuild(story)
    print(f'Done: {OUT}')

if __name__ == '__main__':
    main()
