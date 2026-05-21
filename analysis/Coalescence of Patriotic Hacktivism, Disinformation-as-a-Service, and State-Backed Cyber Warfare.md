# Coalescence of Patriotic Hacktivism, Disinformation-as-a-Service, and State-Backed Cyber Warfare

**ITWeb Security Summit 2026 — Background Research Paper**
*Keynote: "Hybrid Cyber and Information Operations: How Attackers Blend Disruption and Influence in 2026"*

***

## Executive Summary

Three phenomena that analysts once treated as analytically distinct — **patriotic hacktivism**, **disinformation-as-a-service (DaaS)**, and **state-backed cyber warfare** — are converging into a single, mutually reinforcing ecosystem. This convergence is most advanced in the Russian operational model but is visible across Iranian, Chinese, and increasingly domestic-political actor ecosystems. The European External Action Service (EEAS) 4th Annual FIMI Report (March 2026), covering 540 documented incidents across 2025, explicitly identifies increased hybridisation as one of the three defining trends of the current period, alongside increased AI use and increased covertness.[^1][^2]

A critical analytical distinction runs through this coalescence question: **strictly defined cyber-enabled influence operations** (those involving an unauthorised intrusion or DDoS) require state-grade offensive capability or high-end criminal access, and are therefore controlled far more tightly by state principals. **Loosely defined cyber-enabled influence** (coordinated inauthentic behaviour, fake media infrastructure, DaaS campaigns without an intrusion component) has been so thoroughly democratised by AI and social media APIs that it can now be executed by commercial contractors, domestic political parties, individual influencers, and ideologically motivated volunteers — with or without state backing. This distinction shapes the degree of coalescence observable at each geographic level.

***

## Part I: Global Perspective

### The Spectrum of Proxy Relationships

The coalescence of the three phenomena is not uniform. Chatham House's March 2026 report on cyber proxy accountability maps a **spectrum** of proxy relationships rather than a simple binary of state-controlled vs. independent actors. Recorded Future's foundational "Dark Covenant" analysis identifies three relationship types between Russian state intelligence and the cyber underground: direct links (formal employment or secondment), indirect affiliation (structured tasking with operational independence), and tacit agreement (state tolerance enabling impunity, with implicit behavioural constraints). This taxonomy is essential for understanding the coalescence question — different actor types coalesce with the state to different degrees and through different mechanisms.[^3][^4][^5]

### 1. Patriotic Hacktivism as State-Adjacent Infrastructure

**NoName057(16) — the canonical case.** Active since March 2022, NoName057(16) mobilised approximately 4,000 Russian-speaking volunteers via Telegram and its DDoSia crowdsourced DDoS platform, offering cryptocurrency payments to sustain participation. The group was the most prominent Russia-aligned patriotic hacktivist collective in the dataset (EU-40), attacking European banks, government sites, and infrastructure in 13 countries over three years as political signalling — timing attacks to the Czech presidential election, Germany's tank-supply decision, and the Ukraine Peace Summit. Operation Eastwood, coordinated by Europol and Eurojust in July 2025, disrupted this infrastructure across 12 countries, making two arrests, issuing seven arrest warrants, and notifying over 1,000 individual supporters of their legal liability. German authorities issued arrest warrants for six Russian nationals, two of whom are assessed to be the principal orchestrators still residing in Russia.[^6][^7][^8][^9]

What did Operation Eastwood reveal about the state nexus? The two principal orchestrators remained in Russia, shielded from extradition — consistent with the "tacit agreement" model. Mandiant's analysis found that "KillNet's targeting has consistently aligned with established and emerging Russian geopolitical priorities," with targeting that "suggests that at least part of the influence component of this hacktivist activity is intended to directly promote Russia's interests." The FBI and FBI-classified advisories note overlaps between CARR, NoName057(16), and Russian GRU-directed infrastructure. Yet no direct command-and-control link to a specific GRU or FSB unit has been publicly confirmed — the relationship appears to function through shared ideological framing, Telegram target dissemination, and guaranteed impunity within Russia.[^10][^11][^12][^13]

**Cyber Army of Russia Reborn (CARR)** sits closer to the state-controlled end of the spectrum. US Treasury sanctions in July 2024 designated CARR leader Yuliya Pankratova and primary hacker Denis Degtyarenko, noting Degtyarenko had compromised the SCADA system of a US energy company and distributed training materials on ICS attacks. CARR's transition from low-impact DDoS toward industrial control system targeting from late 2023 onward represents a qualitative escalation that suggests more active state direction — the FBI noted CARR's arrest of administrator Victoria Dubranova in December 2025 revealed operational ties to both CARR and NoName057(16).[^14][^12][^10]

**Sandworm** (GRU Unit 74455) represents the fully state-embedded end of the spectrum: a GRU military unit running offensive cyber operations against critical infrastructure while maintaining hacktivist cover personas. Sandworm has been publicly linked to NotPetya ($10 billion in global losses), Ukrainian power grid attacks, and SCADA/OT targeting at industrial scale. Its role in the Ukraine conflict illustrates how state cyber warfare absorbs and directs the hacktivist surface layer.[^15]

The Ukrainian IT Army (EU-39 in the dataset) is the mirror image: a patriotic hacktivist collective created by the Ukrainian government from the first days of the February 2022 invasion, openly coordinated by state actors via Telegram, deploying DDoS and website-disruption campaigns against Russian and Belarusian targets as a wartime narrative tool. It demonstrates that the state–hacktivist coalescence is not a Russian monopoly but a structural feature of contemporary hybrid warfare.

### 2. State Hacktivist Facades: The False-Flag Layer

Several groups named in the dataset as "hacktivists" are, on closer examination, state fabrications or state-seeded fronts designed to provide plausible deniability.

**TV5Monde (EU-37):** Initially claimed by "CyberCaliphate," the April 2015 attack on the French broadcaster — which combined broadcast disruption (hack-and-destroy), website takeover (hack-and-post), and IS propaganda injection — was subsequently linked by investigators to Russian-affiliated actors. The false-flag attribution to an Islamist hacktivist group is a defining example of the state-hacktivist facade in strictly defined intrusion-based operations.

**Anonymous Sudan:** Presenting itself as a Sudanese Muslim nationalist hacktivist collective, the group conducted DDoS attacks against Sweden, Israel, the United States, and critical infrastructure in multiple countries. Truesec's investigation, corroborated by multiple firms, concluded that Anonymous Sudan was "most likely created as part of a Russian information operation" to harm Sweden's NATO application and advance pro-Kremlin narratives in the Islamic world. However, the October 2024 US indictment of Sudanese brothers Ahmed and Alaa Salah Omer confirmed that the group was in fact led by Sudanese nationals, while also noting that the group "may share ideologies with, and sometimes appear to act in concert with, Killnet and similar hacktivist groups". Anonymous Sudan thus represents a hybrid case: genuinely Sudanese operators voluntarily aligned with Russian strategic objectives and sharing infrastructure with pro-Kremlin groups, without (based on available evidence) formal tasking by Russian intelligence. This is a distinct model from direct state fabrication.[^16][^17][^18][^19][^20]

**Guccifer 2.0:** The persona that leaked stolen DNC and Podesta materials to WikiLeaks in 2016 presented itself as a lone Romanian hacker — in reality it was a GRU officer (NA-6, NA-9 in the dataset). This remains the clearest example of a state intelligence agency creating a hacktivist persona to enable a hack-and-leak operation (strictly defined, intrusion-based) while maintaining deniability.

**Iranian proxies:** The IRGC operates a documented network of hacktivist front groups. Cyber Av3ngers, CyberToufan, and Cotton Sandstorm are IRGC-attributed groups presenting as ideologically motivated hacktivists while conducting operations aligned with IRGC strategic objectives — notably the October 2023–February 2024 campaign in support of Hamas (AS-3 in the dataset) that included attacks on Israeli and US critical infrastructure. CSIS analysis notes that "Iran's history of utilizing hacktivist groups as state proxies cannot be overlooked".[^21][^22][^23]

### 3. Disinformation-as-a-Service: The Commercial Layer

The commercial DaaS market represents a third pathway through which the coalescence occurs — not through state direction but through commercial contracting, where private actors sell influence capabilities to states, political parties, and corporations alike.

**Team Jorge** is the most documented example. Exposed by a 30-outlet investigation led by Forbidden Stories in February 2023, the group — run by former Israeli special forces operative Tal Hanan — claimed responsibility for 33 presidential-level influence campaigns across Africa, Latin America, Europe, and the Middle East. Its AIMS software managed over 30,000 AI-driven fake social media accounts (avatars) across all major platforms. Team Jorge's activities included not only no-intrusion CIB campaigns (loosely defined cyber-enabled influence) but also hacking operations: it claimed to have attacked the phones of Nigerian opposition leaders in 2015 working alongside Cambridge Analytica, attacked the Catalan independence referendum in 2014, and hacked the campaign accounts of William Ruto's associates ahead of Kenya's 2022 elections. This blend — commercial contractor, no state loyalty, intrusion capability married to CIB — represents a DaaS actor that straddles the strict/loose distinction.[^24][^25][^26][^27]

**Estraterra (South America):** Multiple Latin American election cycles feature the commercial PR firm Estraterra as a DaaS actor, operating across at least six election environments in Brazil, Venezuela, Ecuador and elsewhere. The South America chapter of the source dataset identifies this as a textbook DaaS case — a commercial actor with no ideological identity, available to whoever pays, running Type-1c (CIB/fake-asset propaganda) operations without any intrusion component.

The DaaS market intersects with state operations when states become clients. The US State Department has documented that Russia's "Prigozhin network" (and its African Initiative successor) recruited DaaS capabilities and local talent across Africa. Russia moved from building its own troll farms to outsourcing disinformation amplification to local contractors and influencers — a hybrid of state-directed messaging and commercial-market execution.[^28][^29]

### 4. The Criminal–State–Hacktivist Triangle

Ransomware groups occupy the lowest-coalescence position on the spectrum but are not entirely separate from the state ecosystem in the Russian case. Recorded Future's analysis identifies "cyber privateers" — ransomware groups that operate with state tolerance, generating revenue and occasionally serving state intelligence objectives when tasked. DarkSide and REvil (JBS Foods, NA-15 in the dataset) are the archetypal cases: financially motivated, operating openly within Russia, refraining from targeting Russian entities, and occasionally performing operations that aligned with Russian intelligence interests.[^30][^4][^3]

The boundary between ransomware and hacktivism is itself blurring. Rapid7's 2025 analysis documents hacktivist groups launching their own ransomware operations, driven by a mix of ideological motivation and financial opportunism. The HStodayUS report notes that in 2024, "several hacktivist groups ventured into cybercrime, launching their own ransomware and ransomware-as-a-service (RaaS) operations" while "nation-state actors showed increased cooperation with ransomware gangs".[^31][^32]

### 5. The EEAS Hybridisation Finding

The 4th EEAS FIMI Report (2026), covering 540 incidents across 2025, reports that 10,500 social media channels and websites were mobilised across documented incidents, with 35% attributed to Russia and China combined. AI use in FIMI operations jumped approximately 259% compared to 2024, with synthetic audio, video, and text now "embedded as standard tools across both Russian and Chinese operations". The report identifies a core structural feature: Russia and China "rely on extensive covert and fabricated networks aligned with their strategic objectives — outsourcing capabilities through these opaque networks to expand reach while preserving plausible deniability and complicating attribution". This is precisely the mechanism of coalescence: the state outsources to hacktivist fronts and DaaS contractors to expand reach and reduce attribution risk.[^33][^1]

***

## Part II: Africa

### From the Source Dataset (fit ≥ 0.7)

The Africa chapter of the dataset presents an important asymmetry. All nine qualifying incidents (fit ≥ 0.7) are criminal ransomware double-extortion operations (Type 2f) against private-sector targets. The 20-incident broader Africa chapter explicitly notes "a clear split between cyber-enabled influence via CIB infrastructure (Type 1c, predominantly Russian-linked or domestic political-PR networks) and double-extortion ransomware (Type 2f)". The 11 CIB-infrastructure cases primarily attributable to Russian-linked/Wagner-aligned networks and domestic political-PR networks in sub-Saharan Africa fall below the 0.7 threshold because they lack a confirmed unauthorised intrusion — underscoring the dataset's structural bias toward strictly defined intrusion-based operations.

The continent's most significant CIB-infrastructure incidents — Russian/African Initiative networks in the Sahel, Team Jorge's election interference in Kenya, Nigeria, and Senegal — are absent from the qualifying dataset precisely because they do not involve intrusions. This is analytically significant for the coalescence question: **the dominant Africa-level coalescence is happening in the loose (no-intrusion) CIB space**, not in the intrusion-based hacktivist space that dominates the European dataset.

### Russia–Africa: From Wagner to "African Initiative"

Following Yevgeny Prigozhin's death in August 2023, Russia reorganised its Africa influence operations under the "Africa Corps" (Russian MoD) and the **African Initiative** media outlet. Analyst Jedrzej Czerep of the Polish Institute of International Affairs notes that "African Initiative, often serving as [the Africa Corps] media wing, was more accommodating and happy to reuse all assets that were already there". African Initiative maintains offices in Ouagadougou (Burkina Faso) and Bamako (Mali), operates five Telegram channels including one with over 55,000 subscribers, runs a website in Russian, English, French and Arabic, and conducts in-person events — "friendship lessons" in schools, football matches, and a journalism school in Mali staffed by Russian-directed local journalists.[^34][^29][^3]

The African Initiative model is a hybrid of state-controlled media operation and loose DaaS: the Russian state sets the narrative agenda and funds the infrastructure, but uses locally recruited African journalists, bloggers, and influencers who provide authenticity and plausible deniability. This is the Africa-level expression of the EEAS's "outsourcing to covert networks" model. It operates primarily in the no-intrusion (loose) category but intersects with the state cyber infrastructure through shared digital assets and coordination.[^28]

Forbidden Stories' investigation documents Russia's disinformation offensive in the Sahel as "a massive, comprehensive operation that forces journalists throughout the countries Moscow is manipulating to censor themselves or risk reprisal" — organised trips to Russia for Malian journalists returned them as "pro-Russia event organisers". This represents a full-spectrum influence operation: state-funded media infrastructure + local proxy recruitment + narrative alignment + self-censorship through intimidation, all without a qualifying intrusion.[^34]

### Team Jorge and Commercial DaaS in Africa

Team Jorge's Africa footprint documented in the Forbidden Stories/Guardian investigation is the clearest evidence of commercial DaaS coalescence in the continent. Claimed operations include:[^35][^24]
- **Senegal (2019):** AIMS avatars used to amplify pro-Macky Sall content to secure his re-election
- **Kenya (2022):** Hacking of William Ruto's campaign associates via Telegram and Gmail (strictly defined intrusion component)
- **Nigeria (2015):** Phone compromise of opposition candidates, credential acquisition, and disinformation — done in conjunction with Cambridge Analytica, on behalf of then-President Jonathan's campaign[^26][^24]

These cases illustrate that Africa is not merely a *target* of DaaS but a *market* for it — domestic political actors are both clients and, increasingly, domestic providers.

### Anonymous Sudan: The Africa-Linked Russian Proxy

Anonymous Sudan's positioning as an "African" hacktivist group was itself a piece of African-related disinformation: by adopting a Sudanese Muslim nationalist identity, the group (whether Russian-controlled or Russian-aligned) aimed to build Russia's credibility in the Islamic/African world. The group threatened to attack France if it sent troops to Niger following the 2023 coup — directly amplifying Russian strategic messaging on France's military withdrawal from the Sahel. Its DDoS attacks against Sweden's NATO application timing, its cooperation with Killnet, and its pro-Kremlin narrative consistency demonstrate how a nominally African hacktivist group functions as part of Russia's global influence ecosystem, regardless of whether the principal operators were Sudanese nationals or Russian operatives.[^36][^37][^16]

### Africa's Domestic Commercial Influence Market

The Africa Centre for Strategic Studies reports that disinformation campaigns seeking to manipulate African information systems surged nearly fourfold since 2022. ISS research published in March 2025 identifies "local online influencer networks" as an increasingly significant component — distinct from both foreign state operations and formal DaaS contractors. These domestic paid-influencer networks:[^38][^39][^40]
- operate across national borders (South African influencers active in Kenya, Botswana, Zimbabwe and Nigeria)[^39]
- mix ideological motivation with financial compensation
- overlap with foreign state operations when they are recruited to amplify pre-packaged material[^39]

This creates a domestic commercial market that overlaps opportunistically with both state-directed foreign operations and purely financial hacktivist/criminal operations — a three-way partial coalescence that is analytically distinct from the tightly controlled state hacktivist model dominant in Europe.

***

## Part III: South Africa

### From the Source Dataset (fit ≥ 0.7)

All nine qualifying South African incidents in the dataset are double-extortion ransomware cases (Type 2f): Transnet (AF-14), TransUnion (AF-15), Experian (AF-16), Cell C (AF-17), Sibanye-Stillwater (AF-18), Astral Foods (AF-19), MTN (AF-20), and the broader industrial wave (AF-6). South Africa accounts for nine of the 20 Africa-chapter incidents. None of these are hacktivist operations, none have confirmed state attribution, and none meet the threshold for cyber-enabled influence via CIB infrastructure. The coalescence of hacktivist, DaaS, and state-backed warfare in South Africa is therefore **entirely invisible in the qualifying dataset** — it exists in the sub-threshold CIB space.

### The Bell Pottinger / Gupta Precedent: South Africa's DaaS Case Study

The Bell Pottinger / Gupta state-capture influence operation (2015–2017) remains Africa's most forensically documented example of commercial DaaS intersecting with domestic political power. Bell Pottinger, a UK PR firm, was contracted by the Gupta family and their network to:
- Create the "white monopoly capital" narrative as a political attack vector
- Build a network of fake Twitter accounts and Facebook pages (coordinated inauthentic behaviour)
- Establish fake news sites (Black Opinion, WMCLeaks, WMCScams) as seeming independent outlets
- Coordinate amplification through ANN7 television and The New Age newspaper[^41][^42][^43]

This is a Type-1c operation (CIB/propaganda via cyber-enabled fake assets) without an intrusion component — the defining form of domestic political DaaS. The operation had no foreign state principal; its principals were the Gupta family and their political associates. Bell Pottinger's subsequent collapse after the PRCA investigation is a landmark case in the accountability of DaaS firms.[^42][^44]

The Bell Pottinger operation also illustrates a key mechanic of the South African influence ecosystem: the network of fake sites and accounts did not create the narratives from scratch but packaged and amplified real political grievances ("white monopoly capital" had genuine resonance) with fabricated supporting content. This is the architecture of effective domestic political DaaS: authentic grievance + manufactured amplification + fake provenance.

### Foreign State Operations in South Africa: The Russian Track

South Africa's role as a BRICS anchor state and its formal non-alignment on the Ukraine conflict make it a priority target for Russian narrative operations. ISS research on the 2024 elections found that one prominent South African influencer claimed "Russian agents paid him to amplify narratives aimed at 'destabilising' South Africa during the polls," providing pre-packaged content and paying R50 per like. While this cannot be independently verified, it is consistent with the African Initiative/Wagner model of using local influencers for deniability.[^39]

The DA's February 2026 public statement (ahead of the 2026 local government elections) explicitly warned of "foreign-linked influence operations" running "counter-campaigns" against the party, demanding State Security Agency investigation of "foreign funding and coordinated inauthentic behaviour". This represents an escalation in the visibility of foreign state operations into domestic South African politics.[^45]

### Domestic Political Influence Operations: MK and EFF Networks

The ISS 2025 study on disinformation during the May 2024 elections found that the two largest "influence communities" on X and Facebook were associated with the uMkhonto weSizwe (MK) party and Economic Freedom Fighters (EFF). Both "appear to have benefitted from paid influencers including those ideologically aligned to the party". The study notes these communities had "an outsized effect on the conversation given their final election results" — MK at 14.58% and EFF at 9.58% of the vote.[^40][^39]

These domestic political influence networks represent the Type-1c (CIB) space in which South Africa's most active hybrid-adjacent operations occur. They operate in the **loose (no-intrusion)** category, are funded by domestic political actors rather than foreign states, and are not hacktivist in any meaningful sense. However, the overlap with foreign state operations — where foreign actors amplify domestically produced content, or local influencers are paid to amplify foreign-produced content — creates a coalescent space that blurs the domestic–foreign, commercial–state, and hacktivist–criminal distinctions simultaneously.[^46][^39]

### Convergence Risk: The Three Pathways in South Africa

South Africa is distinctively exposed to all three forms of partial coalescence simultaneously:

| Pathway | Actor Class | Type (Strict/Loose) | State Principal | Examples |
|---|---|---|---|---|
| Criminal ransomware | Transnational criminal groups | Strict (intrusion) | None (tacit Russian tolerance) | Transnet, TransUnion, Cell C, MTN |
| Foreign state influence | Russia, potentially others | Loose (no intrusion) | Russian MoD/FSB | Russian-paid influencer amplification; African Initiative ecosystem[^39][^28] |
| Domestic commercial DaaS | Political parties, PR firms | Loose (no intrusion) | Domestic political clients | Bell Pottinger/Guptas; MK/EFF paid influencer networks[^41][^39] |

These three pathways are structurally independent but operationally overlapping: a domestic influencer who amplifies Russian-packaged content is simultaneously serving domestic political interests and foreign state objectives. A criminal ransomware group whose operators are protected by Russian tolerance is simultaneously financially motivated and state-adjacent. The coalescence is therefore not an organisational fact — it is a structural feature of an information environment where multiple actors' interests align around shared narratives and shared infrastructure.

***

## Part IV: Cross-Cutting Analytical Themes

### The Plausible Deniability Architecture

All three forms of coalescence serve a common purpose: preserving the attacking state's plausible deniability while extending its reach. Chatham House's 2026 analysis identifies this as the central strategic value of the proxy ecosystem: "The wide variety of Russian or Russia-linked cyber proxies, differing in their organization, motivation and relationship to the state, creates a spectrum of threat actors that complicates attribution and benefits Russia by enabling calibrated deniability". The EEAS 4th Report confirms that 65% of documented FIMI incidents could not be attributed to a specific state actor — precisely because the covert networks and commercial contractors in the supply chain absorb attribution costs.[^5][^1]

The key asymmetry is that plausible deniability works better in the **loose (no-intrusion)** category. In strictly defined intrusion-based operations, technical forensics (infrastructure, TTPs, malware families, operational patterns) eventually yield attribution — as with GRU/APT28 attribution for the Bundestag hack (EU-2) and Macron Leaks (EU-22). In the no-intrusion CIB space, attribution requires open-source intelligence, platform-level data sharing, and financial tracking — capabilities that most African and Global South states lack, and that platforms are increasingly unwilling to apply.[^39]

### The Strict/Loose Division Mirrors the State/Commercial Division

A consistent finding across all three geographic levels is that **strictly defined (intrusion-based) cyber-enabled influence operations tend to be state-controlled or state-directed**, because the offensive cyber capabilities required are not commercially available at scale. **Loosely defined (no-intrusion) CIB operations tend to be commercially available** and are executed by a much wider range of actors including commercial contractors, domestic political parties, and paid influencer networks.

This means the coalescence problem has two distinct dimensions requiring different defensive responses:
1. **Intrusion-based:** Counter-attribution, offensive cyber disruption, sanctions, criminal prosecution of identified individuals, platform security hardening
2. **CIB-based:** Platform transparency regulation, political advertising disclosure, AI-generated content labelling, digital literacy, civil society capacity, cross-border information regulator cooperation

### The Eastwood Precedent: Disruption as Coalescence Limiter

Operation Eastwood's July 2025 disruption of NoName057(16) represents a qualitative shift in international law enforcement response to the hacktivist-state coalescence. By notifying over 1,000 individual volunteers of their personal legal liability, the operation directly attacks the **mass-participation model** that makes patriotic hacktivist groups effective as force multipliers. Simultaneously, by issuing arrest warrants for the Russian-based orchestrators and placing five on the EU Most Wanted list, it raises the reputational and geopolitical cost for the state-tolerating-proxies model.[^7][^8][^9][^47][^6]

Chatham House's analysis, however, cautions that "even after disruption or apparent deactivation/dissolution, proxies are often able to reconstitute themselves quickly" because law enforcement "frequently fail to target the enabling ecosystems — including hosting infrastructure, payment processors, cryptocurrency exchanges and technology suppliers — on which proxy operations depend". The strategic coherence problem — fragmented across legal, economic, and operational domains — remains unsolved.[^48][^5]

### AI and the Acceleration of Coalescence

The EEAS 4th Report's finding that AI use in FIMI operations jumped 259% in 2025 is the single most important accelerant of coalescence. AI reduces the cost of CIB operations to the point where individual influencers, domestic political parties, and small commercial contractors can produce nation-state quality disinformation content at scale. This eliminates the prior capability differential between state actors and non-state actors in the loose category. It also makes the strict/loose distinction less analytically clean, because AI-enabled deepfake and synthetic media operations can achieve influence effects that previously required an intrusion (e.g., fabricated video of a political figure saying something they never said — a fake-but-cyber-equivalent of a hack-and-leak operation).[^33][^1]

Team Jorge's AIMS software, which predated the current generative AI wave, already demonstrated avatar-at-scale CIB in 2022–23. Its successor systems, now incorporating generative AI, represent a qualitative leap in the commercially available DaaS toolkit — with direct implications for African election environments where moderation capacity is lowest and the AI systems are least trained on local languages and contexts.[^24][^33][^39]

***

## Conclusions for Security Leaders

1. **The state–hacktivist–criminal triangle is structural, not accidental.** Russia (and to a lesser degree Iran and China) has deliberately architected a layered proxy ecosystem because it delivers reach while absorbing attribution costs. Defensive responses must target the enabling infrastructure, not just the visible actors.[^5][^48]

2. **The strict/loose distinction defines the addressable response space.** Intrusion-based hybrid operations are countered primarily through cyber defence, forensic attribution, and law enforcement. CIB-based operations are countered primarily through platform transparency, political finance disclosure, media literacy, and civil society capacity — tools that are far less developed in Africa and the Global South.[^39]

3. **South Africa faces all three pathways simultaneously** — criminal, foreign state (loose), and domestic commercial (loose). Each requires a different institutional response and different institutional leads. Conflating them risks policy paralysis.[^39]

4. **The commercial DaaS market is under-regulated globally and essentially unregulated in Africa.** The Bell Pottinger and Team Jorge precedents demonstrate that the coalescence between commercial contractors and both state and political-party clients is already well-established in the African theatre. Closing this gap requires extraterritorial accountability mechanisms for influence-operation firms analogous to those applied to mercenary military companies.[^24][^5]

5. **AI is eliminating the capability differential that previously separated state actors from commercial DaaS and domestic political operators in the loose (no-intrusion) space.** By 2026, the practical effect is that any moderately resourced domestic political actor can run what previously required a foreign intelligence service. This represents a fundamental shift in the threat landscape.

---

## References

1. [4th EEAS Report on Foreign Information Manipulation ... - MediaWell](https://mediawell.ssrc.org/news-items/4th-eeas-report-on-foreign-information-manipulation-and-interference-threats/)

2. [4th EEAS Annual Report on Foreign Information Manipulation and ...](https://www.eeas.europa.eu/eeas/4th-eeas-annual-report-foreign-information-manipulation-and-interference-threats_en) - The 4th EEAS Annual Report on FIMI Threats builds on the methodology of the Response Framework to FI...

3. [Dark Covenant: Connections Between the Russian](https://www.recordedfuture.com/fr/research/russian-state-connections-criminal-actors) - The intersection of individuals in the cybercriminal world and officials in the Russian government i...

4. [Dark Covenant: Connections Between the Russian | Recorded Future State and Criminal Actors](https://www.recordedfuture.com/blog/russian-state-connections-criminal-actors) - The intersection of individuals in the cybercriminal world and officials in the Russian government i...

5. [Holding state-sponsored hackers and other cyber proxies to account](https://www.chathamhouse.org/2026/03/holding-state-sponsored-hackers-and-other-cyber-proxies-account) - Deployed alongside conventional military force, these tactics entail the extensive use of proxies – ...

6. [Europol Disrupts NoName057(16) Hacktivist Group Linked to DDoS ...](https://thehackernews.com/2025/07/europol-disrupts-noname05716-hacktivist.html) - Europol dismantles NoName057(16), a Russian group behind DDoS attacks, arresting two and targeting o...

7. [Europol says it disrupted a major pro-Russian DDoS crime gang](https://www.techradar.com/pro/security/europol-says-it-disrupted-a-major-pro-russian-ddos-crime-gang) - Major infrastructure was taken offline

8. [Operation Eastwood...](https://www.computing.co.uk/news/2025/security/europol-cripples-pro-russia-cybercrime-network) - Europol has announced the successful disruption of pro-Russian cyber gang NoName057(16), in a multin...

9. [Pro-Russian Cybercrime Network Demolished in Operation Eastwood](https://www.infosecurity-magazine.com/news/prorussian-cybercrime-network/) - A Europol coordinated operation has taken down key infrastructure used by pro-Russian hacktivist gro...

10. [FBI – Federal Bureau of Investigation - Facebook](https://www.facebook.com/FBI/posts/when-connected-to-the-internet-operational-technology-ot-devices-become-easy-tar/1326026402904256/) - When connected to the internet, Operational Technology (OT) devices become easy targets for maliciou...

11. [KillNet DDoS Attacks Further Moscow's Psychological Agenda](https://www.bankinfosecurity.com/blogs/killnet-ddos-attacks-further-moscows-psychological-agenda-p-3471) - While self-proclaimed Russian hacktivist groups such as KillNet, Tesla Botnet and Anonymous Russia c...

12. [Treasury Sanctions Leader and Primary Member of the Cyber Army ...](https://home.treasury.gov/news/press-releases/jy2473) - The United States exposes the identity of and imposes sanctions on two members of the Russian govern...

13. [Russian Cybercrime & State Militarization - Analyst1](https://analyst1.com/russian-cybercrime-state-militarization/) - After being dismantled by Operation Cronos, LockBit is hit again—this time with a massive internal l...

14. [US sanctions two members of Russian 'Cyber Army' hacktivist group](https://therecord.media/cyber-army-russia-us-sanctions) - The US has imposed sanctions on two members of the Russian government-aligned hacktivist group known...

15. [Understanding Sandworm, a State-Sponsored Threat Group - ISACA](https://www.isaca.org/resources/news-and-trends/industry-news/2024/understanding-sandworm-a-state-sponsored-threat-group) - Sandworm is one of the most technically sophisticated threat groups in the world and, according to n...

16. [Hacking Group Says It Attacked Microsoft for Sudan. Experts Say Russia's Behind It](https://www.bloomberg.com/news/articles/2023-06-28/anonymous-sudan-does-group-behind-microsoft-cyberattack-have-ties-to-russia) - 'Anonymous Sudan' is promoting Russia's interests in an escalating campaign of cyberattacks against ...

17. [US Indicts Sudanese Brothers for Anonymous Sudan Attacks](https://www.bankinfosecurity.com/us-indicts-sudanese-brothers-for-anonymous-sudan-attacks-a-26540) - Two Sudanese brothers are under criminal indictment in the United States for their role in distribut...

18. [Anonymous Sudan: Threat Intelligence Report](https://insights.truesec.com/hub/report/anonymous-sudan-threat-intelligence) - Our threat intelligence report (published Feb 20, 2023) explains how the so-called "Anonymous Sudan"...

19. [What is Anonymous Sudan? - A Truesec Investigation](https://www.truesec.com/hub/blog/what-is-anonymous-sudan) - A threat actor identifying as “Anonymous Sudan” has been conducting DDoS attacks against multiple ta...

20. [US disables Anonymous Sudan infrastructure linked to DDoS attack ...](https://www.cybersecuritydive.com/news/us-disrupts-anonymous-sudan-ddos/730104/) - Authorities unsealed charges alleging two Sudanese nationals ran the hacktivist group, linked to maj...

21. [Iranian Hacktivist Proxies Escalate Activities Beyond Israel](https://blog.checkpoint.com/research/check-point-research-report-shift-in-cyber-warfare-tactics-iranian-hacktivist-proxies-extend-activities-beyond-israel/) - Cyber Av3ngers is an Iranian Government Islamic Revolutionary Guard Corps (IRGC) affiliated hacktivi...

22. [Beyond Hacktivism: Iran's Coordinated Cyber Threat Landscape](https://www.csis.org/blogs/strategic-technologies-blog/beyond-hacktivism-irans-coordinated-cyber-threat-landscape) - Hacktivist groups can exist independently. However, Iran's history of utilizing hacktivist groups as...

23. [Unmasking 35 Iranian Cyber Operatives Driving State-Sponsored ...](https://falconfeeds.io/blogs/iran-cyber-operatives-irgc-mois-state-attribution-2026/) - Groups attributed to the IRGC include APT33, APT35, APT42, Cyber Av3ngers, Pioneer Kitten, and Cotto...

24. [Team Jorge: The Israeli contractors behind disinformation and ...](https://peoplesdispatch.org/2023/02/17/team-jorge-the-israeli-contractors-behind-disinformation-and-election-interference/) - An undercover investigation into disinformation is prompting calls for inquiries by political partie...

25. [Team Jorge and the Israeli disinformation industry in Latin America](https://latinoamerica21.com/en/team-jorge-and-the-israeli-disinformation-industry-in-latin-america/) - Analysis L21 | Digital mercenaries. Team Jorge and the Israeli disinformation industry in Latin Amer...

26. [Team Jorge: A global disinformation and hacking machine](https://www.thepipd.com/content/blog/team-jorge-a-global-disinformation-and-hacking-machine/) - New revelations about an Israeli contractor involved in disinformation and hacking.

27. ['Team Jorge' ― how disinformation threatens democracy - DW.com](https://www.dw.com/en/team-jorge-investigation-raises-concerns-about-threat-to-democracy/a-64708627) - A major new investigation into election manipulation has exposed weaknesses in the security of inter...

28. [The Kremlin's Efforts to Spread Deadly Disinformation in Africa](https://2021-2025.state.gov/the-kremlins-efforts-to-spread-deadly-disinformation-in-africa/) - The Kremlin's disinformation campaign in Africa: In addition to its own staff, African Initiative re...

29. ['African Initiative,' a New Russian Media Outlet, Promotes ...](https://adf-magazine.com/2024/10/african-initiative-a-new-russian-media-outlet-promotes-disinformation/) - The African Initiative, a Kremlin-funded website is spreading pro-Russia messages and harmful disinf...

30. [Ransomware through the lens of state crime: Conceptualizing ransomware groups as cyber proxies, pirates, and privateers – DOAJ](https://doaj.org/article/71fb3d3adf164739b48808dc3380c922) - Cybercrime and other cybersecurity harms are gaining increasing political and public attention acros...

31. [The Lines Are Blurring Between Criminal and Terror Enterprises](https://www.hstoday.us/featured/the-lines-are-blurring-between-criminal-and-terror-enterprises-heres-how-to-adapt/) - Ironically, the common criminal isn't burdened with silos and boundaries. Elaborate crimes can be or...

32. [Exploring the Convergence from Hacktivism to Cybercrime - Rapid7](https://www.rapid7.com/blog/post/2025/06/03/from-ideology-to-financial-gain-exploring-the-convergence-from-hacktivism-to-cybercrime/) - Some hacktivist groups are evolving into ransomware operations and even becoming ransomware affiliat...

33. [Sae Schatz's Post - LinkedIn](https://www.linkedin.com/posts/saeschatz_read-me-the-4th-eeas-report-on-fimi-just-activity-7444401806983503873-Qwqv) - READ ME: The 4th EEAS Report on FIMI just dropped. The European External Action Service (EEAS) relea...

34. [Propaganda Machine: Russia's information offensive in the ...](https://forbiddenstories.org/propaganda-machine-russias-information-offensive-in-the-sahel/) - In the Sahel and the Central African Republic, Moscow’s disinformation agents spare no expense in ma...

35. ['Team Jorge', threat to democracy: Israeli firm meddled in ... - YouTube](https://www.youtube.com/watch?v=5QRVGhNz3tU) - A team of contractors led by a former Israeli special forces operative has allegedly meddled in over...

36. [Hacking group that has ties to Africa may be a Russian proxy](https://www.businesstechafrica.co.za/security/2023/06/29/hacking-group-that-has-ties-to-africa-may-be-a-russian-proxy/) - A hacking group that has been said to be the cause of a series of outages at Microsoft sometime this...

37. [Russian-Backed Hackers Pose a Threat to Africa's Online Community](https://adf-magazine.com/2025/01/russian-backed-hackers-pose-a-threat-to-africas-online-community/) - Experts say that hacker groups such as the Russian-backed Anonymous Sudan pose a threat to Africa's ...

38. [Mapping a Surge of Disinformation in Africa](https://africacenter.org/spotlight/mapping-a-surge-of-disinformation-in-africa/) - Africa is subject to 23 transnational disinformation campaigns—nearly all of which are sponsored by ...

39. [Africa's democracies must guard against local online ...](https://issafrica.org/iss-today/africa-s-democracies-must-guard-against-local-online-influencer-networks) - New research shows that key figures in South Africa’s domestic online influence industry are engaged...

40. [South African political influencer groups expand 'rage bait' ...](https://nationalsecuritynews.com/2025/03/south-african-political-influencer-groups-expand-rage-bait-tactics-across-africa/) - The year-long ISS study found that key figures in South Africa’s influence industry were engaged in ...

41. [How the Guptas' propaganda war machine was built](https://misinfo.investigate.africa/posts/Main-Story_2/) - The Guptas' disinformation campaign used a range of media to carry their propaganda across the natio...

42. [Bell Pottinger Exposed: Influence unpacks the evils of ...](https://www.dailymaverick.co.za/article/2020-08-21-bell-pottinger-exposed-influence-unpacks-the-evils-of-disinformation/) - Feature documentary Influence, directed by Diana Neille and Richard Poplak, made its South African d...

43. [This is the fake news campaign that tried to divide South Africa](https://www.cnet.com/culture/internet/fake-news-campaign-divided-south-africa-twitter-facebook/) - The Gupta brothers stoked racial flames in the country, but it didn't help them.

44. [Bell Pottinger - Wikipedia](https://en.wikipedia.org/wiki/Bell_Pottinger)

45. [South Africans should reject disinformation operations at the ballot box](https://www.da.org.za/2026/02/south-africans-should-reject-disinformation-operations-at-the-ballot-box) - The Democratic Alliance calls on voters to reject the online disinformation campaigns that are attem...

46. [a concerted campaign to destabilise SA post elections](https://www.dailymaverick.co.za/article/2024-06-02-disinformation-nation-a-concerted-campaign-to-destabilise-sa-post-elections/) - There are indications that an orchestrated campaign is playing out to discredit the elections and wa...

47. [Europol-led operation takes down pro-Russian cybercrime network](https://www.euronews.com/next/2025/07/16/europol-led-operation-takes-down-pro-russian-cybercrime-network) - The operation targeted a pro-Russia group that is believed to have attacked several municipalities a...

48. [Strategic coherence is the most powerful tool we have for cyber ...](https://bindinghook.com/strategic-coherence-is-the-most-powerful-tool-we-have-for-cyber-proxy-accountability/) - Our new research paper for Chatham House frames accountability as two mutually reinforcing instrumen...

