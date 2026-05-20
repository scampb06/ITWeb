# Hybrid Cyber–Influence Attack Types, Prevalence & Protagonists: Global, Africa & South Africa

*Prepared for the ITWeb Security Summit 2026 keynote — "Hybrid cyber and information operations: how attackers blend disruption and influence in 2026"*

***

## 1. Framework: The Three-Type Taxonomy

This report uses the taxonomy from the ITWeb Hybrid Incidents dataset:

- **Type 1 — Cyber-enabled influence (1a–1h):** A cyber operation (intrusion, DDoS, defacement, etc.) that primarily serves an influence goal — shaping perceptions, damaging reputations, suppressing dissent, or signalling political power.
- **Type 2 — Influence-enabled cyber (2a–2h):** Deception, disinformation, or social engineering that enables or amplifies a cyber intrusion — e.g., phishing lures (2b), impersonation (2c/2d), false-flag personas (2g), or doxxing-based extortion (2f).
- **Type 3 — Parallel cyber–influence:** Simultaneous, independently-run cyber and influence operations by the same actor, forming a composite campaign without tight tactical integration.

Each incident is scored for taxonomic fit (0–1.0); only those scoring ≥0.7 are discussed here from the primary dataset.[^1]

***

## 2. Global Picture (G)

### 2.1 What the PDF Dataset Shows

The ITWeb Hybrid Incidents PDF classifies 101 incidents across six continents, with 40 in Europe and 20 in Africa. Looking across all qualifying incidents, the following types emerge:[^1]

| Type | Sub-type | Count (qualifying ≥0.7) | Illustrative Example |
|------|----------|------------------------|---------------------|
| 1b | Hack-and-leak | 10 | DNC (NA-6), Macron Leaks (EU-22), IRGC-2024 (NA-7) |
| 1c | CIB / propaganda via fake assets | 8 | Doppelganger (EU-6 etc.), Ghostwriter Baltic (EU-18), BadBazaar (AS-1) |
| 1d | Hack-and-destroy (wiper/operational disruption) | 5 | Sony Pictures (NA-13), Transnet (AF-14), Sandworm Ukraine |
| 1f/1g | Defacement / DDoS-for-suppression | 4 | NoName057(16) (EU-40), Ukrainian IT Army (EU-39), PRC-Taiwan (AS-7) |
| 2b | Phishing/spearphishing as intrusion enabler | 9 | Gamaredon (EU-15, EU-35), Bundestag (EU-2), InvisiMole (EU-21) |
| 2c/2d | Deepfake or impersonation scam | 3 | Arup deepfake-CFO (AS-14), MGM vishing (NA-14), Lazarus brand scam (AS-5) |
| 2f | Double-extortion ransomware (doxxing lever) | 9 | Transnet (AF-14), TransUnion (AF-15), JBS (NA-15), Change Healthcare (NA-16) |
| 2g | False-flag / cutout persona | 6 | Guccifer 2.0 (NA-6), "Guardians of Peace" (NA-13), CyberCaliphate (EU-37) |
| 3 | Parallel cyber–influence | 8 | EU Parliament 2024 (EU-1), Moldova (EU-23), PRC-Taiwan 2016 (AS-8) |

**The three most prevalent types globally**, based on the dataset, are: **2f (double-extortion ransomware with doxxing leverage)**, **1b (hack-and-leak)**, and **2b (phishing as intrusion enabler)** — with **1c (CIB/propaganda via fake digital infrastructure)** a close fourth.[^1]

**Key structural finding from the dataset:** Hack-and-leak (1b) and phishing (2b) are almost never separated — every qualifying 1b incident in the dataset has 2b as a secondary type. Similarly, every qualifying 2f incident has either 1b or 1d as a secondary type. The taxonomy illuminates layering, not discrete standalone attacks.[^1]

### 2.2 Broader Research Assessment

Beyond the PDF's sampled incidents, the global picture in 2024–2026 is characterised by several dominant patterns:

**Double-extortion ransomware (2f + 1b/1d) is the single most prolific hybrid type.** With nearly 6,500 incidents recorded in 2025 — the second-largest spike on record — and double extortion now the baseline standard across virtually all ransomware gangs, this is the defining volume threat. Ransomware groups posted 3,734 victims to public extortion sites in just the first half of 2025, a 20% increase over the prior six months and a 67% jump year-on-year. The leak site is the influence layer: it creates public pressure, reputational damage, and regulatory exposure that is inseparable from the financial coercion.[^2][^3]

**Cyber-enabled influence via CIB infrastructure (1c)** is the most prevalent *state-actor* type. Russia's "franchise" model — Doppelganger, Ghostwriter, Storm-1516, Operation Overload, RT-mirror networks — all share the same signature: fake domain/account infrastructure built to inject propaganda and impersonate trusted outlets. Africa is now subject to 23 documented transnational disinformation campaigns, nearly all sponsored by external states. China's capability for CIB has also "significantly increased," with pro-PRC actors running coordinated inauthentic behaviour across multiple continents in 2024.[^4][^5][^1]

**Influence-enabled phishing (2b) as the intrusion gateway** is the most consistent technical precursor. The ODNI 2025 Threat Assessment and ESET's April–September 2025 APT Report both document that spearphishing and credential theft remain the primary initial access mechanism for state-linked APT groups globally, often using thematically relevant lure content (war events, economic crises) to increase credibility.[^6][^7]

**Impersonation-based fraud (2c/2d)** is the fastest-growing type at the intersection of AI and cybercrime. The Arup Hong Kong deepfake-CFO incident (AS-14, US$25.6M lost without any system intrusion) is the dataset's textbook example of how entirely AI-generated social engineering can substitute for a technical breach. MuddyWater's "internal spearphishing" — sending phishing messages from a compromised internal account — and the MGM Resorts vishing attack represent a continuum of the same trend.[^6][^1]

**Parallel operations (Type 3)** cluster around two triggers: *elections* and *armed conflict*. The 2024 EU Parliament elections, Moldova's 2024 presidential vote, Taiwan's 2016 and 2018 elections, and the Russia–Ukraine war all generated Type-3 campaigns where the same actor ran independent cyber and influence streams simultaneously.[^1]

**False-flag personas (2g)** are a consistent secondary layer across state-attributed operations, used to deny attribution, buy time, or amplify confusion. "Guardians of Peace" (DPRK), "Guccifer 2.0" (GRU), and "CyberCaliphate" (Russia-linked) are now canonical examples.[^1]

### 2.3 Circumstances of Each Type

| Type | When it tends to occur |
|------|----------------------|
| **1b Hack-and-leak** | Elections, major geopolitical disputes, corporate coercion; preceded by months of access (2b entry) |
| **1c CIB / propaganda** | Continuous background operation; accelerates ahead of elections, referenda, or major political events |
| **1d Hack-and-destroy (wiper/operational)** | Armed conflict (Sandworm/Ukraine), state coercion of corporations (DPRK/Sony), or ransomware where payment is withheld |
| **1f/1g Defacement / DDoS signalling** | Triggered by symbolic political events (state visits, military decisions, summits); used as low-escalation signalling by patriotic hacktivists |
| **2b Phishing / spearphishing** | Year-round; peaks during crises when lure themes (conflicts, disasters, elections) are topical |
| **2c/2d Impersonation / deepfake fraud** | Financial fraud (CFO scams); HR/IT credential resets; accelerating with generative AI capability |
| **2f Double-extortion ransomware** | Opportunistic targeting of profitable/under-defended sectors; Christmas/holiday periods (weekend attacks); also used by criminal proxies with state tolerance |
| **2g False-flag persona** | State-attributed operations requiring deniability; criminal gangs evading attribution |
| **Type 3 Parallel** | Armed conflict; election cycles; major policy disputes between states |

***

## 3. Africa (AF)

### 3.1 What the PDF Dataset Shows

Of the 20 Africa-classified incidents in the source dataset, 9 qualify at ≥0.7 fit. The continental table reveals a sharp two-track structure:[^1]

**Track A — CIB / electoral influence (1c):** 11 of the 20 incidents (those not meeting the threshold) are primarily Russian-linked or domestic political-PR CIB operations. Qualifying incidents include the Kenya Airways double-extortion (AF-9) and the MTN Group breach (AF-20), but the bulk of the CIB cases fell below the 0.7 threshold because the cyber component (fake-account infrastructure) lacked a confirmed unauthorized intrusion.[^1]

**Track B — Double-extortion ransomware (2f):** 8 of the 9 qualifying incidents are Type 2f, primarily targeting South Africa (six incidents) and Kenya (one). Victims span ports and rail (Transnet/AF-14), credit bureaux (TransUnion/AF-15, Experian/AF-16), telecoms (Cell C/AF-17, MTN/AF-20), mining (Sibanye-Stillwater/AF-18), poultry and food production (Astral Foods/AF-19), and aviation (Kenya Airways/AF-9).[^1]

**South Africa accounts for 9 of the 20 African incidents**, making it the single largest country in the Africa dataset and the epicentre of the continent's double-extortion ransomware epidemic.[^1]

The Experian breach (AF-16) stands out as a rare pure influence-enabled-cyber case (2d/2g): a South African fraudster impersonated a legitimate Experian client to extract 24 million consumer records — no ransomware, no state actor, just identity deception enabling a data theft.[^1]

### 3.2 Broader Research Assessment

**CIB/influence operations across Africa in 2024–2026** are significantly more widespread and varied than the ransomware-focused PDF dataset suggests. The Africa Center for Strategic Studies documents 23 transnational disinformation campaigns active on the continent, covering every sub-region. Key campaigns from broader research include:[^4]

- **Central African Republic (CAR):** Prigozhin-linked Russian networks deployed fake local personas and media fronts to build support for Wagner-aligned security actors and undermine French influence (2019–2020). Documented by Graphika and Stanford Internet Observatory.[^8]
- **Sudan (2018–2019):** Russian-linked actors connected to the Prigozhin network provided social-media messaging coordination to suppress protest information flows during the uprising against President al-Bashir.[^8]
- **Mali and Burkina Faso (2022):** DFRLab documented coordinated pro-Russian/pro-Wagner Facebook assets that spiked before military coups in both countries, building narratives hostile to France and supportive of Russian security partnerships.[^8]
- **Ethiopia (2021):** DFRLab and Meta documented coordinated inauthentic behaviour around the Tigray conflict, including click-to-tweet campaigns amplifying government narratives and inflaming ethnic tensions.[^8]
- **Uganda (2021):** Facebook removed accounts linked to Uganda's Ministry of Information and Communications Technology that were running fake personas to shape the election information environment.[^8]
- **Zimbabwe (2018):** Fake-news mercenaries deployed coordinated propaganda during the election period.[^8]
- **Libya (2019–2020):** Multiple foreign powers — including Russia — ran competing CIB operations around the conflict and elections, documented by Stanford Internet Observatory, Graphika, and DFRLab.[^8]

**The Wagner → "The Company" transition** is a major development for the Africa threat landscape. After Prigozhin's death in August 2023, his network of more than 60 influence agents was restructured under direct SVR (Russian Foreign Intelligence Service) supervision. Leaked documents covering January–October 2024 and published in February 2026 by The Continent and an international consortium reveal operations across Madagascar, Namibia, and South Africa.[^9]

**Ransomware on the continent** is escalating sharply. INTERPOL's 2025 Africa Cyberthreat Assessment reports that South Africa suffered the highest number of ransomware detections on the continent in 2024 (17,849), followed by Egypt (12,281) and Nigeria (3,459). Kaspersky data shows suspected scam notifications rising up to 3,000% in some African countries. Ninety percent of African countries self-assessed as needing "significant improvement" in law enforcement and prosecution capacity.[^10]

**Domestic political actors** are an increasingly documented protagonist in African disinformation. As the Africa Center for Strategic Studies notes, campaigns are no longer exclusively foreign; domestic political PR networks, ruling-party communications operations, and opposition-aligned actors are all deploying coordinated online influence infrastructure.[^11]

***

## 4. South Africa (SAF)

### 4.1 What the PDF Dataset Shows

South Africa dominates the Africa chapter: 9 of the 20 incidents are South Africa-specific or South-Africa-headquartered organisations, and 7 of the 9 qualifying (≥0.7) Africa incidents involve South African targets.[^1]

All qualifying South Africa incidents in the dataset are **Type 2f (double-extortion ransomware)**, with secondary types of **1b (hack-and-leak via leak site)** or **1d (hack-and-destroy through operational disruption)**:

| Incident | Perpetrator | Victim Sector | Primary/Secondary |
|----------|-------------|---------------|-------------------|
| AF-6 Industrial ransomware wave | BianLian, RansomHub, MeowLeaks, BlackSuit, MedusaLocker, Cactus | Industrial/critical infrastructure | 2f / 1b |
| AF-14 Transnet | "Death Kitty"/HelloKitty (Russia/Eastern Europe per CrowdStrike) | Ports, rail, supply chain | 2f / 1d |
| AF-15 TransUnion | N4ughtySecTU (self-ID'd Brazilian crew) | Credit bureau, downstream banks | 2f / 1b |
| AF-16 Experian | Karabo Phungula (South African fraudster, convicted) | Credit bureau, consumers | 2d / 2g |
| AF-17 Cell C | RansomHouse | Telecoms | 2f / 1b |
| AF-18 Sibanye-Stillwater | Unattributed | Mining | 2f / 1d |
| AF-19 Astral Foods | Unattributed | Agriculture/poultry | 2f / 1d |
| AF-20 MTN Group | "Unknown third party" | Telecoms, pan-African | 2f / 1b |

The Experian case (AF-16) is the dataset's only South Africa incident classified primarily under influence-enabled cyber (2d/2g): a domestic fraudster used client-impersonation to extract 24 million consumer records, later convicted.[^1]

**No South Africa incidents in the qualifying PDF dataset are classified under CIB or electoral influence operations (1c).** This reflects a significant selection-bias gap: the dataset's inclusion criteria (% fit ≥0.7 requiring a confirmed cyber intrusion or DDoS component) structurally disadvantages CIB campaigns where the "cyber" element is fake-account infrastructure rather than an unauthorized intrusion.[^1]

### 4.2 Broader Research Assessment

**Russian influence operations** targeting South Africa are more extensively documented by broader research than the PDF dataset captures:

- **2019 election interference attempt:** Daily Maverick and Africa Center documentation record a suspected Prigozhin-linked attempt to shape South African electoral discourse, using cyber-enabled CIB infrastructure.[^8]
- **"The Company" operations (2024):** Leaked SVR-supervised documents, published February 2026, show Russian operatives offered to help the ANC discredit opposition parties ahead of the May 2024 elections, including through "paid online campaigns and fabricated content." The Democratic Alliance was specifically targeted in the post-election government-of-national-unity negotiations, with Russian operatives arguing that DA members in key ministries "could harm Russia's political and defence ties with South Africa."[^9]
- **ANC/RET disinformation (2024 elections):** Independent of Russian networks, the Daily Maverick and DFRLab documented extensive domestic disinformation during the 2024 elections, including fabricated news stories impersonating the *Mail & Guardian* that falsely claimed the ANC had been "sold for R150-million" to DA interests, circulated on WhatsApp — a textbook Type 1c / 2g hybrid using fake media infrastructure.[^12][^13]
- **South African First Facebook operation (2020):** Africa Center documentation links a domestic CIB network, connected to the "South African First" political formation, to coordinated inauthentic behavior on Facebook using pseudo-fact-checking and "leak" pages to manipulate political discourse.[^8]
- **IEC impersonation campaigns:** The Electoral Commission of South Africa (IEC) has publicly documented multiple impersonation campaigns targeting the credibility of its CEO and the electoral process itself — Type 2c/2g influence operations using fabricated WhatsApp conversations and fake social-media posts.[^14]

**Ransomware targeting South Africa** is intensifying beyond what the PDF captures. Kaspersky data shows South Africa had 17,849 ransomware detections in 2024, the highest on the continent. Malware surged by 123% in H1 2025 compared to the same period in 2024. CYFIRMA's 2025 South Africa threat landscape report confirms convergence of persistent ransomware campaigns with widespread targeting of financial services, telecoms, healthcare, and manufacturing.[^15][^16][^10]

**South Africa is an under-defended node** in a highly connected regional digital economy, making it both an attractive terminal target and a bridgehead for attacks on pan-African infrastructure. The MTN Group breach (AF-20), affecting 18 African and Middle Eastern markets from its South African headquarters, illustrates this bridgehead dynamic.[^1]

***

## 5. Protagonists: Actor Classes and Examples

### 5.1 Classification Framework

The actors engaging in hybrid cyber–influence operations can be classified across five broad classes, which exist on a spectrum of state direction rather than in watertight categories:

1. **State intelligence/military agencies** (direct state operation)
2. **State-linked APT groups / cyber units** (semi-autonomous, state-resourced)
3. **State proxies and influence contractors** (outsourced, deniable)
4. **Patriotic hacktivists** (ideologically aligned volunteers, state-tolerated)
5. **Criminal groups** (financially motivated; some with state tolerance or co-option)

### 5.2 Global Examples by Class

#### Class 1: State Intelligence / Military Agencies (Direct)

State agencies conduct operations that they directly control and resource, often with the highest technical sophistication and strategic patience.

- **Russia — GRU (APT28 / Fancy Bear):** Responsible for the Bundestag hack-and-leak (EU-2), the DNC (NA-6) and Podesta (NA-9) operations, the Macron Leaks (EU-22), and Ghostwriter intrusions against German politicians (EU-19). Every operation followed the same playbook: 2b phishing to gain initial access → extended dwell time for exfiltration → timed release via cutout personas (2g) for maximum political impact (1b).[^1]
- **Russia — FSB (Gamaredon, InvisiMole):** Ukraine-focused persistent intrusion and surveillance campaigns (EU-15, EU-21, EU-35) using war-themed phishing lures that double as influence tools — the lure *is* the disinformation, embedding malware in content framed as genuine wartime intelligence.[^1]
- **Iran — IRGC:** The 2024 US presidential election hack-and-leak (NA-7), with three IRGC-linked nationals indicted, demonstrated a direct state intelligence operation targeting electoral integrity through spearphishing and unsolicited timed leaks to media and political figures.[^1]
- **Russia — SVR ("The Company"):** The post-Prigozhin restructuring placed former Wagner influence operatives directly under SVR supervision, running operations across Africa (Madagascar, Namibia, South Africa) as documented in February 2026 leaks.[^9]

#### Class 2: State-Linked APT Groups

These groups are resourced, directed, or closely aligned with state agencies but maintain operational semi-autonomy, enabling partial deniability.

- **Russia — Sandworm (GRU Unit 74455):** Destructive wiper campaigns against Ukrainian infrastructure (ZEROLOT, Sting), energy, logistics, and grain sectors through 2025. The wiper is the influence tool — operational disruption is itself a message to Ukrainian society about the costs of resistance.[^6]
- **China — PLA Strategic Support Force-affiliated groups:** Defacement of Taiwanese public-facing displays (7-Eleven, train stations, university) during Nancy Pelosi's August 2022 visit (AS-7) — a textbook 1f/1c hybrid using compromised public infrastructure to broadcast political messaging to domestic and international audiences.[^1]
- **China — FamousSparrow (Latin America expansion):** Launched extensive campaigns against government entities in Argentina, Guatemala, Honduras, Panama, and Ecuador in 2025, reflecting Beijing's strategic competition with the US near the Panama Canal.[^6]
- **DPRK — Lazarus Group:** Fake cryptocurrency applications (AS-5), supply-chain compromise of South Korean software vendors, and DeceptiveDevelopment fake-job-offer campaigns targeting cryptocurrency developers — all blending financial crime with intelligence-gathering in an influence-enabled cyber (2c) pattern.[^6][^1]
- **Iran — MuddyWater:** "Internal spearphishing" — compromising a mailbox and sending phishing emails from that trusted internal account — active in Nigeria, Greece, Israel, and the US in 2025.[^6]

#### Class 3: State Proxies and Influence Contractors

These actors are explicitly contracted or managed by states to conduct influence operations with arm's-length deniability.

- **Prigozhin/Wagner → "The Company" (Russia's Africa proxy):** Internet Research Agency-style operations adapted for African political landscapes. More than 60 former Wagner operatives now working under direct SVR supervision, targeting elections in CAR, Sudan, Libya, Mali, Burkina Faso, Madagascar, Namibia, and South Africa, using local-language content, paid influencers, fake media, and manufactured documents.[^9][^8]
- **"Russosphere" network (Luc Michel, Belgium):** A coordinated French-language network spanning Facebook, YouTube, and Telegram, pushing pro-Kremlin messages across Francophone Africa, connected to Russian-aligned far-right European activism.[^17]
- **Ghostwriter (Belarus/Russia-linked contractor):** Account compromise and fake-post injection against Baltic politicians, media, and German Bundestag members — a contractor-style operation blending 1c, 1b, and 2b components.[^1]

#### Class 4: Patriotic Hacktivists

These actors are ideologically aligned volunteers who operate with varying degrees of state knowledge and tolerance, providing plausible deniability while extending state reach.

- **NoName057(16) (Russia-aligned):** ~4,000 volunteers using the DDoSia tool for a multi-year DDoS campaign against European banks and financial infrastructure, each attack publicly claimed on Telegram as political retaliation for named decisions (e.g., Germany sending Leopard 2 tanks). Disrupted by Europol's Operation Eastwood in July 2025 but not eliminated.[^1]
- **Ukrainian IT Army:** The inverse case — volunteer hacktivists organised by Ukraine's government targeting Russian and Belarusian government, media, financial, and energy websites. A Type-1g DDoS campaign explicitly framed as a "wartime narrative signal" and used to demonstrate mobilised cyber participation.[^1]
- **Killnet and XakNet (Russia-aligned):** Coordinated with NoName057(16) on European targeting; documented as overlapping and complementary operations rather than genuinely independent.[^1]
- **Iran-aligned hacktivists (post-12-Day War, 2025):** Following Israel's June 2025 military operations against Iran, Iranian state actors supplied tools and capabilities to pro-Iranian hacktivist groups, who used them against Western critical infrastructure targets — closely mirroring Russia's proxy model.[^18][^19]

#### Class 5: Criminal Groups (Financially Motivated)

These actors are primarily profit-driven but their techniques — and increasingly their relationships with states — create structural overlap with hybrid cyber–influence operations.

- **REvil / Sodinokibi (Russian-speaking RaaS):** JBS Foods attack (NA-15), disrupting beef and pork processing across three continents. The ransom demand and operational disruption created national-security-level pressure on critical food supply chains — a financial criminal operation with state-level strategic effect.[^1]
- **ALPHV / BlackCat and RansomHub:** Change Healthcare attack (NA-16), causing a weeks-long national pharmacy and claims-processing outage affecting 100M+ Americans. The ALPHV fake "law-enforcement seizure" exit-scam against its own affiliate (2g) adds a further deceptive layer.[^1]
- **Scattered Spider (UNC3944):** English-speaking, US/UK-based group responsible for the MGM Resorts vishing and ransomware attack (NA-14). The vishing of the IT help desk (impersonating an MGM employee) is a textbook Type-2c influence-enabled cyber operation — social engineering as the sole intrusion vector.[^1]
- **RansomEXX, RansomHouse, N4ughtySecTU, BianLian:** Multiple groups active in Africa (Kenya Airways/AF-9, Cell C/AF-17, TransUnion/AF-15, industrial wave/AF-6) using double-extortion playbooks. Attribution varies from Eastern Europe (RansomEXX, RansomHouse) to self-identified Brazilian (N4ughtySecTU) to unknown.[^1]
- **Black Axe (Nigeria-based transnational syndicate):** In West Africa, BEC fraud has driven highly organised multi-million-dollar criminal enterprises with regional impact across banking and financial services.[^10]

### 5.3 Africa-Specific Actor Landscape

Africa's actor landscape is distinctive in three ways:

**1. Foreign state proxies dominate the CIB/influence track.** Russia (via Wagner / "The Company" / Russosphere) is the most documented external actor, but China-linked CIB operations have been documented in Ethiopia, Kenya, and beyond, and domestic governments (Uganda, Ethiopia, Tanzania, Zimbabwe) have also deployed CIB infrastructure against their own civil societies and opposition.[^11][^8]

**2. Criminal ransomware groups, many Eastern European in origin**, dominate the cyber-disruption track. With 90% of African countries lacking adequate prosecution capacity and low cyber-resilience in critical-infrastructure operators, Africa offers an accessible and high-ROI target environment for groups primarily based outside the continent.[^10]

**3. Domestic political actors** are a third, underreported class. Africa Center for Strategic Studies documents that "domestic disinformation is on the rise" — coordinated online campaigns by ruling parties, opposition formations, and ethnic/political pressure groups, deploying the same fake-account and fake-site infrastructure as foreign state actors but driven by domestic electoral incentives.[^11]

### 5.4 South Africa-Specific Actor Landscape

South Africa sits at the intersection of all three tracks:

- **Russian state proxy operations ("The Company"):** Documented operations in 2024 targeting the ANC, DA, and the government-of-national-unity negotiations, offering fabricated content and paid campaigns.[^9]
- **Domestic political-PR networks:** ANC-aligned RET networks circulated fabricated media (the "R150-million" story in May 2024), and the "South African First" party network ran domestic CIB on Facebook.[^13][^12][^8]
- **International criminal ransomware groups:** Responsible for all qualifying (≥0.7) hybrid incidents in the PDF dataset — Transnet, TransUnion, Cell C, Sibanye-Stillwater, Astral Foods, MTN Group, the industrial wave. Groups span Eastern European RaaS operators (Death Kitty/HelloKitty, RansomHouse) to mixed-attribution extortion crews (N4ughtySecTU, BianLian).[^1]
- **Domestic fraudsters:** The Experian breach (Karabo Phungula) demonstrates that influence-enabled cyber does not require sophisticated criminal networks — a single actor exploiting a procedural weakness in client-verification processes can extract millions of records.[^1]
- **State-linked APT activity:** While not yet documented in South Africa with the same certainty as criminal ransomware, CYFIRMA's 2025 threat landscape assessment notes persistent state-sponsored targeting of South African government and financial-sector infrastructure alongside criminal campaigns.[^15]

***

## 6. Selection Bias: What the PDF Dataset Over- and Under-Represents

The PDF dataset is explicit that it is a curated sample scored for fit ≥0.7 against a specific hybrid-operations taxonomy. Key biases to flag for the keynote:

- **Over-represents Europe (40/101 incidents, or 40%)**: this reflects the density of open-source attribution and English/European-language research, not necessarily the volume of actual incidents.
- **Under-represents CIB operations in Africa**: the taxonomy's requirement for a confirmed unauthorized intrusion or DDoS means that most Wagner/SVR influence operations — which use fake-account infrastructure rather than network intrusion — fall below the 0.7 threshold. The 11 Africa CIB cases noted in the continental summary all fell below the bar.[^1]
- **Ransomware cases qualify easily because the double-extortion model has a natural 2f+1b structure**: the leak site *is* the influence operation, providing a clean taxonomic fit. This inflates the apparent share of ransomware in the dataset relative to influence-only operations.
- **Domestic state suppression operations in authoritarian contexts** (Uganda, Tanzania, Ethiopia) are probably more numerous in reality than documented, due to lower research attention and restricted media environments.
- **South Africa's CIB operations are comprehensively missing** from the qualifying subset: the documented Russian and domestic disinformation campaigns from 2019–2024 would likely score 0.4–0.6 under the taxonomy's strict criterion for intrusion, reflecting a real capability gap in public attribution of the intrusion component rather than absence of the campaigns themselves.

***

## 7. Summary Tables

### Prevalence by Geography (PDF Dataset, ≥0.7 Qualifying Incidents)

| Geography | Total classified | Qualifying (≥0.7) | Dominant type(s) | Key selection bias |
|-----------|-----------------|-------------------|------------------|-------------------|
| Global (all) | 101 | ~48 | 2f, 1b, 2b, 1c | Europe over-represented |
| Europe | 40 | 13 | 1c, 1b, 2b, Type 3 | Russian ops dominant |
| North America | 16 | 9 | 1b, 2b, 2f, 2c | Hack-and-leak historic record |
| Africa | 20 | 9 | 2f, 1b, 2d | CIB ops fall below threshold |
| Asia | 14 | 8 | 1c, 2c, 1f, Type 3 | Widest type variety |
| South Africa | 9 of 20 | 7 of 9 | 2f dominant | Russian/domestic CIB missing |

### Actor Classes by Geography

| Class | Global examples | Africa examples | South Africa examples |
|-------|----------------|-----------------|----------------------|
| State intelligence (direct) | GRU, FSB, IRGC, SVR | SVR/"The Company" | SVR (operations documented 2024) |
| State-linked APT | APT28, Gamaredon, Sandworm, PLA-SSF, Lazarus | — | Potential state-linked APT (CYFIRMA assessment) |
| State proxies/contractors | Ghostwriter, Russosphere, IRA | Wagner/"The Company", Russosphere Francophone | "The Company" (ANC/DA targeting, 2024) |
| Patriotic hacktivists | NoName057(16), Ukrainian IT Army, Killnet, Iran proxies | — | — |
| Criminal groups | REvil, ALPHV, Scattered Spider, RansomHub | RansomEXX, RansomHouse, N4ughtySecTU, Black Axe | Death Kitty, RansomHouse, BianLian, RansomHub, N4ughtySecTU |
| Domestic political actors | — | Uganda MoICT, Ethiopian gov-aligned networks, Zimbabwe propaganda networks | ANC-RET networks, South African First, domestic fraudsters |

---

## References

1. [ITWeb_Hybrid_Incidents.pdf](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/79175947/0d834b30-796f-4d98-b0af-fa446679379d/ITWeb_Hybrid_Incidents.pdf?AWSAccessKeyId=ASIA2F3EMEYE2MJFVS2O&Signature=Zlj%2FSAzOhW5nLyxK7Kiqug%2FyRHA%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBMaCXVzLWVhc3QtMSJGMEQCIB4yGXcCh%2F7BjkjAmvQS7HkiyaTCojVvLU2%2B1FZf%2BMhFAiAqLnIQkyjcb9oh4lJc0kSB85ku9PI7aRbMGYtX0bI05Sr8BAjc%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMokBvxHpSr9VzPfBfKtAEGT9ervZsYfc%2FPQhdFhuW%2BcKQsp%2FGY6ptysMPSnVnCZQbqoNhA89LzdnzHi%2FML7UmBapsEgPju1qpXYFlN9LfCef3SOBPD69pV9lWPJUonZOulgco02YID4IFeMaBdUQ8d7AWJRb2I758OteMkrPAMNEis6wJh9CP2JB9ycCTd7x20nHHyahO3cDDBb7rP8FwQ%2FXhpsxAxzYf7yxSNOoV8nrR%2BeUotWeib82Dd%2FA2auOOMUarC1kpwev81st%2Fec9oqVmvfrNdkwGXbTMoqqhzXR9stxZkhHfxbOi%2Bb7K5XP6qt1Jpai1AWxQRE%2FSVjWvYriZH6qgtqLWh9OHlESxaPtyAhcgb0n2NyRe1J0vIm3t6Qo9%2FJyU0Dz1vCeWXwRUzM0QQCqBM%2Fn1VMV7fm2XL4jqVFk0g%2FV8iCt4dkZviQ1vbVWXCIKSZXENgHUMH952q4Nj%2FyKCLeVguRrY0SGbqBO0HppSBOkiaiFA%2BHKjF7W71D3rJ%2BTdSufeEyH8qEOy0l5NXBtFYenAGdwg%2F2ARIQ1hOBOgJWuOSMD8yil3%2FN69wxKLlE3AoaplM%2FdFvzaWT0yDZyHj%2BHjlDVPA89S4H3ZuLZ%2FShYC0Ckb1gOFX05AfOF%2BxVk7H54IAXCsimVdGfskESrjBkb2wiDLOy4W8ulQmzvgoJcHYHZm5ikiloK7j1udI2mMoL3IpPtGKkwp5ZBpyFnkwIuD2KIKyJqSp%2Fp%2Fhzpwpmix5TBRA8mpMCS8hZ0Zr69tQOeur1a2ieGqwRgRFp%2F0l5N3waJHJbtjJDazCI2bLQBjqZASKHgeOFl%2FYvKGRnHl6e9MndNJIBwVIMM5TNJtrynKk4NcSE3Tl8v3yWw00MHxZZuIdR41G8TqeiBTzJ04kuRwFzH6nzo8AVT5MUbQj%2BRs%2B8RgkcJ7kszy8vKw8FTp44sCuxyzG3IduLK2uWwnD6lGASF0lAfN0il4xP82jsB0g%2B2mK8marly46WJYVRNAGqra0l%2BJUQl41%2FPQ%3D%3D&Expires=1779219035) - **page-1**
ITWeb Security Summit
Hybrid Cyber / FIMI Incidents
Global Classification by Continent
In...

2. [10 New Ransomware Groups of 2025](https://cyble.com/knowledge-hub/10-new-ransomware-groups-of-2025-threat-trend-2026/) - Discover 10 new ransomware groups of 2025, their tactics, victim trends, and what security teams sho...

3. [Ransomware's new playbook is chaos - Help Net Security](https://www.helpnetsecurity.com/2025/12/31/ransomware-tactics-expanding/) - Ransomware tactics are expanding as attacks rise, payments fall, and AI drives threat capabilities, ...

4. [Mapping a Surge of Disinformation in Africa](https://africacenter.org/spotlight/mapping-a-surge-of-disinformation-in-africa/) - Africa is subject to 23 transnational disinformation campaigns—nearly all of which are sponsored by ...

5. [[PDF] Annual Threat Assessment of the U.S. Intelligence Community](https://www.dni.gov/files/ODNI/documents/assessments/ATA-2025-Unclassified-Report.pdf) - PRC actors have increased their capabilities to conduct covert influence operations and disseminate ...

6. [Russia-linked hackers intensify attacks as global APT activity shifts](https://www.helpnetsecurity.com/2025/11/06/global-apt-activity-report-2025/) - ESET’s Global APT Activity Report reveals rising cyber operations by Russia, China, Iran, and North ...

7. [ODNI 2025 Threat Assessment notes threats from Russia, China ...](https://industrialcyber.co/reports/odni-2025-threat-assessment-notes-threats-from-russia-china-iran-north-korea-targeting-critical-infrastructure-telecom/) - ODNI 2025 Threat Assessment notes threats from Russia, China, Iran, North Korea targeting critical i...

8. [africa_hybrid_incidents.md](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_a0759534-63d2-4f7c-b582-5270c8e3e903/c1b82765-7860-4393-a5cd-28eb926ee6fd/africa_hybrid_incidents.md?AWSAccessKeyId=ASIA2F3EMEYE2MJFVS2O&Signature=hXxScq%2B6ozXysBjOJ%2B7JymSEeJ4%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBMaCXVzLWVhc3QtMSJGMEQCIB4yGXcCh%2F7BjkjAmvQS7HkiyaTCojVvLU2%2B1FZf%2BMhFAiAqLnIQkyjcb9oh4lJc0kSB85ku9PI7aRbMGYtX0bI05Sr8BAjc%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAEaDDY5OTc1MzMwOTcwNSIMokBvxHpSr9VzPfBfKtAEGT9ervZsYfc%2FPQhdFhuW%2BcKQsp%2FGY6ptysMPSnVnCZQbqoNhA89LzdnzHi%2FML7UmBapsEgPju1qpXYFlN9LfCef3SOBPD69pV9lWPJUonZOulgco02YID4IFeMaBdUQ8d7AWJRb2I758OteMkrPAMNEis6wJh9CP2JB9ycCTd7x20nHHyahO3cDDBb7rP8FwQ%2FXhpsxAxzYf7yxSNOoV8nrR%2BeUotWeib82Dd%2FA2auOOMUarC1kpwev81st%2Fec9oqVmvfrNdkwGXbTMoqqhzXR9stxZkhHfxbOi%2Bb7K5XP6qt1Jpai1AWxQRE%2FSVjWvYriZH6qgtqLWh9OHlESxaPtyAhcgb0n2NyRe1J0vIm3t6Qo9%2FJyU0Dz1vCeWXwRUzM0QQCqBM%2Fn1VMV7fm2XL4jqVFk0g%2FV8iCt4dkZviQ1vbVWXCIKSZXENgHUMH952q4Nj%2FyKCLeVguRrY0SGbqBO0HppSBOkiaiFA%2BHKjF7W71D3rJ%2BTdSufeEyH8qEOy0l5NXBtFYenAGdwg%2F2ARIQ1hOBOgJWuOSMD8yil3%2FN69wxKLlE3AoaplM%2FdFvzaWT0yDZyHj%2BHjlDVPA89S4H3ZuLZ%2FShYC0Ckb1gOFX05AfOF%2BxVk7H54IAXCsimVdGfskESrjBkb2wiDLOy4W8ulQmzvgoJcHYHZm5ikiloK7j1udI2mMoL3IpPtGKkwp5ZBpyFnkwIuD2KIKyJqSp%2Fp%2Fhzpwpmix5TBRA8mpMCS8hZ0Zr69tQOeur1a2ieGqwRgRFp%2F0l5N3waJHJbtjJDazCI2bLQBjqZASKHgeOFl%2FYvKGRnHl6e9MndNJIBwVIMM5TNJtrynKk4NcSE3Tl8v3yWw00MHxZZuIdR41G8TqeiBTzJ04kuRwFzH6nzo8AVT5MUbQj%2BRs%2B8RgkcJ7kszy8vKw8FTp44sCuxyzG3IduLK2uWwnD6lGASF0lAfN0il4xP82jsB0g%2B2mK8marly46WJYVRNAGqra0l%2BJUQl41%2FPQ%3D%3D&Expires=1779219035) - # Hybrid Cyber/FIMI Incidents in Africa

This document compiles Africa-focused incidents involving b...

9. [Reports Uncover Russian Efforts to Swing African Elections](https://adf-magazine.com/2026/04/reports-uncover-russian-efforts-to-swing-african-elections/) - “It shows how disinformation and online networks can quietly shape public opinion during critical po...

10. [New INTERPOL report warns of sharp rise in cybercrime in Africa](https://www.interpol.int/en/News-and-Events/News/2025/New-INTERPOL-report-warns-of-sharp-rise-in-cybercrime-in-Africa) - LYON, France: A growing share of reported crimes in Africa is cyber-related, according to INTERPOL's...

11. [Domestic Disinformation on the Rise in Africa](https://africacenter.org/spotlight/domestic-disinformation-on-the-rise-in-africa/) - A growing trend of domestic political actors deploying targeted disinformation schemes requires expa...

12. [Lessons learned from South Africa's 2024 elections](https://dfrlab.org/2024/07/31/lessons-learned-from-south-africas-2024-elections/) - Independent media worked overtime to mitigate the spread of disinformation, while generative AI play...

13. [a concerted campaign to destabilise SA post elections](https://www.dailymaverick.co.za/article/2024-06-02-disinformation-nation-a-concerted-campaign-to-destabilise-sa-post-elections/) - There are indications that an orchestrated campaign is playing out to discredit the elections and wa...

14. [Electoral Commission warns of malicious disinformation ...](https://www.elections.org.za/content/About-Us/News/Electoral-Commission-warns-of-malicious-disinformation-on-social-media/)

15. [CYBER THREAT LANDSCAPE- SOUTH AFRICA - cyfirma](https://www.cyfirma.com/research/cyber-threat-landscape-south-africa/) - The cyber threat landscape in South Africa during 2025 reflects a convergence of persistent ransomwa...

16. [South Africa's cyber threat landscape is intensifying. Malware ...](https://www.facebook.com/Kaspersky/posts/-south-africas-cyber-threat-landscape-is-intensifying-malware-surged-by-123-in-h/1254440913393872/) - South Africa's cyber threat landscape is intensifying. Malware surged by 123% in H1 2025 compared to...

17. [Researchers find new pro-Russia influence campaign targeting Africa](https://www.npr.org/2023/02/01/1152899845/a-pro-russian-social-media-campaign-is-trying-to-influence-politics-in-africa) - ... misinformation and disinformation. The activist, Luc Michel, was ... How AI deepfakes polluted e...

18. [Iran leans on hacktivist proxies in wake of Israeli, U.S. strikes - Axios](https://www.axios.com/2025/07/01/iran-hacktivist-israeli-us-strikes) - Iranian state-backed hackers are borrowing from the Russian cyber playbook and sharing tools with id...

19. [Iran and the Expanding Cyber Front: What Government Leaders ...](https://www.icitech.org/post/iran-and-the-cxpanding-cyber-front-what-government-leaders-need-to-know) - Their model blends state operators, contractors, and proxy or "patriotic" hacking groups. This creat...

