---
layout: default
---

# South America (SA) — Hybrid Cyber–Influence Incident Classification

This table classifies 7 incidents targeting South American entities according to the cyber–influence taxonomy:
- **(1) Cyber-enabled influence** — cyber operations serving an influence goal (1a–1h)
- **(2) Influence-enabled cyber** — disinformation/deception enabling a cyber intrusion (2a–2h)
- **(3) Parallel cyber–influence** — simultaneous, independent cyber and influence operations by the same actor

The **% fit** column rates how well each incident fits its primary type, on a 0.0–1.0 scale:
- **1.0** — textbook fit (defining act of the sub-type clearly present).
- **0.7–0.9** — strong fit, partial or mixed on one element.
- **≤ 0.5** — capped here for Type-1 incidents without a real unauthorised intrusion or DDoS, and for Type-2 incidents lacking a tactically-connected subsequent intrusion or DDoS by the same actor.
- **Type-3** scored on whether the cyber and influence components are by the same threat actor and close in time.

<div id="fit-filter" style="margin:16px 0;padding:12px 16px;background:#f3f6fb;border:1px solid #d0d7de;border-radius:6px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;">
  <label for="fitSlider" style="font-weight:600;white-space:nowrap;">Min % fit:</label>
  <input type="range" id="fitSlider" min="0" max="1" step="0.1" value="0" style="width:200px;cursor:pointer;">
  <span id="fitValue" style="font-weight:600;min-width:2.5em;">≥ 0.0</span>
  <span id="fitCount" style="color:#555;font-size:0.9em;"></span>
  <button id="fitReset" style="padding:4px 10px;border:1px solid #d0d7de;border-radius:4px;cursor:pointer;background:#fff;font-size:0.9em;">Show all</button>
</div>

| ID | Incident title | Country / scope | Primary type | Secondary type(s) | Perpetrator (as described) | Main victim category | % fit |
|---|---|---|---|---|---|---|---|
| SA-1 | [Disinformation networks and cyber-enabled manipulation during Brazil's 2018 election](../all_incidents/SA-Disinformation-Networks-and-Cyber-Enabled-Manipulation-During-Brazils-2018-Election.md) | Brazil | 1c – cyber-enabled CIB and mass-messaging propagation (WhatsApp-centred information ecosystem and coordinated content amplification) | — | Domestic political/PR-aligned networks and online actors | Elections, voters, democratic institutions | 0.4 |
| SA-2 | [Disinformation networks and institutional attacks during Brazil's 2022 election](../all_incidents/SA-Disinformation-Networks-and-Institutional-Attacks-During-Brazils-2022-Election.md) | Brazil | 1c – cyber-enabled CIB and video-first social propagation attacking electoral institutions | — | Mixed/uncertain (domestic disinformation networks documented by Reuters and rights groups; regional patterns also present) | Elections, voters, Superior Electoral Court (institutional target) | 0.4 |
| SA-3 | [Estraterra network targeting Ecuador and multiple Latin American elections](../all_incidents/SA-Estraterra-Network-Targeting-Ecuador-and-Multiple-Latin-American-Elections.md) | Ecuador, Argentina, Bolivia, Chile, Uruguay, Venezuela | 1c – cyber-enabled CIB through fake pages, accounts and Instagram profiles | — | Domestic political/PR firm (Ecuadorian PR firm Estraterra operating out of Canada with political consultants and former Ecuadorian government employees) | Elections, voters across multiple Latin American states | 0.4 |
| SA-4 | [Latin American election-focused coordinated inauthentic behavior affecting several South American countries](../all_incidents/SA-Latin-American-Election-Focused-Coordinated-Inauthentic-Behavior-Affecting-Several-South-American-Countries.md) | Argentina, Bolivia, Chile, Uruguay, Ecuador, Venezuela | 1c – cyber-enabled CIB across Facebook and Instagram with deceptive page identities | — | Domestic political/PR firm (Estraterra-linked network) | Elections, voters, candidate perceptions | 0.4 |
| SA-5 | [Pentagon Uses Entorno Diario to Shape Latin American Views on China](../all_incidents/SA-Pentagon-Uses-Entorno-Diario-to-Shape-Latin-American-Views-on-China.md) | Latin America (Spanish- and Portuguese-speaking audiences; Colombia, Venezuela, Bolivia and others) | 1c – cyber-enabled covert propaganda via pseudo-news website with paid X/social ad amplification | 2d – pseudo-news website with weak US-government provenance disclosure | Western governments (US — Pentagon-linked gc_ network; General Dynamics IT) | Civil society, public opinion, regional views of China | 0.5 |
| SA-6 | [Regional disinformation and propaganda flows from extra-regional state media into South American information environments](../all_incidents/SA-Regional-Disinformation-and-Propaganda-Flows-from-Extra-Regional-State-Media-into-South-American-Information-Environments.md) | Argentina, Colombia, Uruguay, Venezuela; broader Spanish-language space | 1c – cyber-enabled CIB and industrial-scale digital propaganda distribution via cyborg accounts and platform manipulation | — | Mixed: Russia/Russian-linked, China/PRC-linked, and allied state-media ecosystems | Civil society, public opinion, regional discourse | 0.4 |
| SA-7 | [Venezuelan government-linked influence campaign on Twitter](../all_incidents/SA-Venezuelan-Government-Linked-Influence-Campaign-on-Twitter.md) | Venezuela; regional Latin American audiences | 1c – cyber-enabled CIB using fake or managed accounts to amplify pro-Maduro narratives | — | Domestic government-aligned (Venezuelan government-linked network per DFRLab) | Civil society, public opinion, regional perceptions | 0.4 |

## Continental observations

- **South America is the dataset's clearest example of *commercial* and *domestic-political* influence operations.** Estraterra (SA-3, SA-4) is a textbook case of *disinformation-as-a-service*: a commercial PR firm contracted across at least six Latin American election environments — directly relevant to the keynote's question on disinformation-as-a-service.
- **Almost the entire South American record is Type-1c** — coordinated inauthentic behaviour on Facebook, Instagram, Twitter, TikTok and WhatsApp. No hack-and-leak (1b), defacement (1f), or ransomware-driven cases (2f) are documented in this regional sample.
- **Perpetrator mix is distinctive**: domestic political networks and commercial PR firms (Brazil, Estraterra, Venezuela) dominate, with extra-regional state actors (Russia, China, Pentagon) as a secondary layer riding the same infrastructure.
- **Brazil's 2022 institutional attacks (SA-2)** are notable for explicitly targeting an *electoral institution* (the Superior Electoral Court) — a pattern that prefigures many later attempts elsewhere to delegitimise vote-counting bodies.
- **SA-5 (Pentagon Entorno Diario)** mirrors the AS-10/11/12/13 and EU-27 Pentagon-linked gc_ network operations, confirming this as a globally distributed Western covert influence ecosystem worth flagging in the keynote.

<script>
(function () {
  function filterByFit() {
    var threshold = parseFloat(document.getElementById('fitSlider').value);
    document.getElementById('fitValue').textContent = '≥ ' + threshold.toFixed(1);
    var rows = document.querySelectorAll('table tbody tr');
    var visible = 0;
    rows.forEach(function (row) {
      var cells = row.querySelectorAll('td');
      var last = cells[cells.length - 1];
      var val = parseFloat(last ? last.textContent.trim() : '');
      var show = isNaN(val) || val >= threshold;
      row.style.display = show ? '' : 'none';
      if (show) visible++;
    });
    document.getElementById('fitCount').textContent =
      visible + ' / ' + rows.length + ' shown';
  }
  document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('fitSlider').addEventListener('input', filterByFit);
    document.getElementById('fitReset').addEventListener('click', function () {
      document.getElementById('fitSlider').value = 0;
      filterByFit();
    });
    filterByFit();
  });
})();
</script>
