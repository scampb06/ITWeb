---
layout: default
title: "Drivers of Hybrid Cyber-Influence Operations"
---

# Drivers of Hybrid Cyber–Influence Operations: Global, African, and South African Perspectives

**Prepared for ITWeb Security Summit 2026 Keynote Research**
**Based on: ITWeb Hybrid Incidents PDF dataset + independent research**

***

## Executive Summary

The increasing hybridisation of cyber and influence operations — identified by the EEAS as one of the three dominant FIMI trends in 2025, alongside rising AI adoption and deepening covertness — is not a random evolution. It is the product of converging geopolitical, economic, and technical forces that differ meaningfully across geographic scopes. At the global level, hybridisation is primarily driven by great-power strategic competition in a fracturing multipolar order, the industrialisation of the cybercrime economy, and the dramatic reduction in technical barriers brought about by AI and as-a-service models. In Africa, these global drivers are amplified by a specific post-colonial contestation for influence — particularly the Russian narrative offensive in Francophone Africa and the expansion of commercially-operated influence-as-a-service — layered on top of very low cyber resilience and high digital growth rates that make organisations attractive ransomware targets. In South Africa specifically, a unique combination of BRICS/non-aligned geopolitical positioning, domestic political fragmentation, high internet penetration relative to the continent, and the country's own emerging influence-brokerage industry creates a threat environment that differs qualitatively from both the European and broader African patterns.[^1]

A critical analytical distinction running through this analysis is the difference between **strictly defined cyber-enabled influence operations** (Types 1a–1h in the taxonomy, requiring an unauthorised intrusion or DDoS as the enabling mechanism) and **loosely defined cyber-enabled influence** (influence operations that use cyber infrastructure — platforms, bots, paid advertising, deepfakes, fake domains — but do not involve any unauthorised intrusion). The drivers for these two sub-categories partially overlap but diverge on key dimensions: strict-definition operations require state-grade cyber offensive capability or high-end criminal access, whereas loose-definition operations have been democratised to the point where domestic political actors, commercial contractors, and individual influencers can operate them.

***

## Part 1: Global Drivers

### 1.1 From the PDF Dataset

The ITWeb Hybrid Incidents dataset (≥0.7 fit score) contains 40 European, 9 qualifying North American, 10 African, and a number of Asian incidents. Reading across the continental observations, five driver themes emerge explicitly from the incident narratives:

- **Geopolitical conflict acceleration:** The majority of qualifying European intrusion-based operations (EU-15, EU-21, EU-35: Gamaredon phishing; EU-22: Macron Leaks; EU-2: Bundestag; EU-18/19: Ghostwriter) are explicitly war- or election-driven. Every one of the four qualifying North American hack-and-leak operations (NA-5, NA-6, NA-7, NA-9) was election-driven. Asia contributes Iran-Hamas war operations (AS-3) and PRC-Taiwan election pressure (AS-7, AS-8, AS-9). The dataset is dominated by kinetic-conflict and electoral-cycle triggers.
- **State actor plausible-deniability calculus:** The dataset's continental observations note that the proxy/contractor/hacktivist model — Wagner-linked channels, NoName057(16), Ghostwriter, Guccifer 2.0 personas — is consistently used to maintain state deniability. This is a deliberate cost-benefit driver: hybrid operations impose costs on adversaries below the threshold of kinetic response.
- **Financial extortion as the dominant Africa/criminal driver:** All qualifying Africa incidents are financially motivated ransomware/extortion operations (AF-6, AF-9, AF-14, AF-15, AF-16, AF-17, AF-18, AF-19, AF-20). The criminal actors are exploiting low cyber resilience in a rapidly digitalising market.
- **Democratic election cycles as temporal trigger:** The dataset explicitly flags elections in EU member states (EP2024, Moldova, Bulgaria, Germany, Romania, Poland), the US (2016, 2024), and Taiwan as consistent triggers for hybridisation surges.
- **Criminalisation of social engineering (2c/2f types):** MGM/Scattered Spider (NA-14) and Change Healthcare (NA-16) represent a new driver: criminal groups adopting state-grade social-engineering techniques (vishing, deepfake-style impersonation) for financial rather than political ends.

### 1.2 Broader Global Research

#### Geopolitical Drivers

The fundamental geopolitical driver is the erosion of the post-1991 unipolar order and the emergence of what JP Morgan's Centre for Geopolitics calls a "multi-speed, multipolar" environment in which the "CRINK" alignment of China, Russia, Iran and North Korea "reflects shared opposition to a Western-led global order". This creates a persistent structural incentive for hybrid operations: states that cannot challenge Western military-economic power directly find cyber–influence operations to be an asymmetric instrument that is deniable, scalable, cheap, and difficult to attribute.[^2][^3][^4]

Russia's strategic doctrine explicitly frames information operations as an integral component of warfare — not a supplement to it. The SVR, GRU, and FSB operate with different toolkits (SVR: covert cyber espionage; GRU: disruptive and influence operations; FSB: domestic cyber repression and counter-intelligence) but a shared doctrine that treats the information and cognitive domains as legitimate warfighting theatres. The Ukraine conflict accelerated hybridisation because Russia needed to supplement its stalled military campaign with operations that degraded Western will to sustain Ukraine (EU-1, EU-40 dataset patterns).[^1]

China's hybridisation driver is distinct: it is primarily shaped by Taiwan unification narratives, the Belt and Road narrative contest, and the technology-decoupling rivalry with the US and EU. PRC operations in the dataset (AS-7, AS-8, AS-9) are consistently timed to electoral cycles in Taiwan, suggesting a deliberate strategy of using election-period information environment degradation as an alternative to direct military pressure.[^5]

Iran's driver is ideological and geopolitical simultaneously: operations supporting Hamas (AS-3), targeting Israeli infrastructure, and attempting to influence US elections (NA-7) are all explicitly tied to the Islamic Revolutionary Guard Corps' doctrine of proxy-and-asymmetric-warfare as a substitute for conventional military power. The IRGC treats hybrid operations as "strategic deterrence on a budget".[^5]

The emergence of a contested multipolar order also creates a new driver for **non-aligned states** to become targets: as great powers compete for the alignment of swing states, those states' information environments become active theatres regardless of whether they choose to participate.[^6][^7]

#### Economic Drivers

The **Ransomware-as-a-Service (RaaS) industrialisation** is the single most important economic driver of the hybridisation of criminal cyber operations with influence techniques. The World Economic Forum projects cybercrime costs will reach $10.5 trillion globally in 2025. The RaaS model has professionalized the criminal ecosystem: operators provide malware, leak-site infrastructure, negotiation support, and even "customer service" to affiliates who supply access. This industrialisation lowered barriers to entry dramatically — new white-label RaaS platforms like DragonForce's RansomBay enable even less technically skilled actors to operate branded extortion campaigns. The number of newly formed ransomware groups increased by 30% in 2025, and global vulnerability disclosures rose 21% to surpass 35,000.[^8][^9]

The **double-extortion model** is itself a hybridisation driver: once encrypted data is insufficient leverage, criminal groups added leak-site doxing (a form of influence operation — targeted reputational destruction through public data disclosure) as a second pressure mechanism. This means that every significant ransomware operation now has an influence component, even if that component is commercially rather than politically motivated. The Transnet (AF-14), TransUnion (AF-15), and Cell C (AF-17) cases in the dataset are all examples of this pattern.[^8]

**Sanctions and financial exclusion** drive a distinct economic mechanism: state actors under sanctions — Russia, Iran, North Korea — have strong economic incentives to use cyber operations both for revenue generation (DPRK crypto theft) and for weakening the sanctioning economies. This creates a structural alignment between state geopolitical motivations and financially-driven operations.[^3]

#### Technical Drivers

The EEAS 4th FIMI Report (2026, covering 2025 incidents) identifies three top trends: increased hybridisation, increased AI use, and increased covertness. These are not independent — they are mutually reinforcing.[^1]

**Generative AI as a force multiplier** has transformed the cost-structure of influence operations. AI-generated text, synthetic audio, and manipulated video have "shifted from experimental use to routine deployment" and become "cost-effective and scalable tools for threat actors". Peer-reviewed evidence from Oxford's PNAS Nexus (March 2025) confirms that state-backed campaigns using generative AI show measurable increases in the "size and scope" of their propaganda output compared to pre-AI baselines. This is the key technical mechanism behind the EEAS observation that **loose-definition cyber-enabled influence** (no intrusion required) has become dramatically cheaper and thus more prevalent. The European Parliament Research Service (December 2025) further notes that narrative laundering via Wikipedia — injecting false claims that are then absorbed by AI training data and surfaced in chatbot answers — represents a second-order AI amplification mechanism.[^10][^11][^1]

**Platform architecture as a structural enabler:** The attention-maximisation logic of social media recommendation algorithms creates structural incentives for high-engagement content — which disinformation (emotionally charged, novel, often outrage-inducing) reliably generates more than accurate information. This is a technical driver baked into the infrastructure rather than introduced by adversaries.[^12]

**Bulletproof hosting infrastructure** provides the technical backbone for covert operations. Russian-linked bulletproof hosting providers (ZServers, Aeza Group, Media Land) offer phishing pages, malware command-and-control, ransomware leak sites, fast-flux IP rotation, and layered front companies that resist law enforcement takedown. The Five Eyes sanctioned Media Land in November 2025. This infrastructure allows state actors and criminal groups alike to outsource their technical footprint to providers whose permissive jurisdictions insulate them from attribution.[^13][^14][^15]

**The increasing covertness trend** noted by the EEAS reflects adversaries learning from exposure: after the Stanford Internet Observatory's 2022 "Unheard Voice" report exposed CENTCOM-linked fake-persona operations, the Pentagon shifted to paid advertising models that are legally disclosed but difficult to attribute to specific influence objectives. Russian operations shifted from large bot networks (easily detectable by platform algorithms) to smaller, higher-quality networks of fake accounts amplified by paid promotion. This adaptation dynamic — exposure triggers covertness innovation — is itself a technical driver.[^16][^1]

**The as-a-service commercial ecosystem** is the technical driver that democratises hybridisation. Team Jorge's AIMS platform controlling 30,000+ fake accounts, Archimedes Group's Facebook campaigns, DragonForce's white-label RaaS: all represent commercial infrastructure that lowers the technical entry bar for actors with money but without state-grade cyber capability. The CSET (Georgetown) noted in its AI disinformation series that "the outsourcing of these operations to private companies that provide influence as a service" exacerbates the risk precisely because it separates technical capability from the motivational accountability structures that govern state actors.[^9][^17][^18][^12]

### 1.3 The Strict vs. Loose Distinction at the Global Level

At the global level, the key driver asymmetry between the two sub-categories is:

| Driver dimension | Strict definition (requires intrusion/DDoS) | Loose definition (no intrusion) |
|---|---|---|
| Primary actors | State APTs, high-end criminal RaaS affiliates | State actors, commercial contractors, political parties, domestic influencers |
| Technical barrier | High (requires offensive cyber capability or vulnerability exploitation) | Low and declining (generative AI, paid social ads, fake accounts) |
| Geopolitical driver | Active conflict, elections, sanctions pressure | Elections, commercial profit, narrative contestation, all of the above |
| Economic driver | RaaS industrialisation, cryptocurrency ransom infrastructure | Influence-as-a-service market, political advertising budgets |
| Key technical enabler | Bulletproof hosting, 0-day exploit kits, credential-theft tooling | LLMs, synthetic media tools, social media ad platforms, fast-grow bot networks |
| AI impact | Accelerates reconnaissance, credential stuffing, spearphish personalisation | Transforms scale, cost, and quality of content generation; chatbot narrative injection |

The EEAS hybridisation trend reflects principally the **convergence** of these two pathways — increasingly, a single operation uses both, sequencing an intrusion (Type 2b spearphish) to gain material that is then weaponised through loose-definition influence infrastructure (Type 1b/1c).

***

## Part 2: Africa-Specific Drivers

### 2.1 From the PDF Dataset

All ten qualifying Africa incidents in the dataset are financially-motivated intrusion-based operations (Types 2f and 1b/1d): Transnet, TransUnion, Experian, Kenya Airways, Sibanye-Stillwater, Astral Foods, Cell C, MTN, and the Q4 2024 industrial ransomware cluster. The Africa continental observations in the PDF make no reference to state-actor hybrid influence operations, for a structural reason already noted: the ≥0.7 threshold requires either an unauthorised intrusion/DDoS or a tactically connected subsequent breach for the influence component to qualify. This threshold systematically excludes most of the documented Russian and commercial-contractor influence activity in Africa, which operates primarily through fake accounts, paid promotion, and coordinated inauthentic behaviour — none of which require an intrusion.

The PDF's Africa observations therefore capture **only the criminal economic driver** (profitable targets, low resilience, double-extortion model) and miss the geopolitical and commercial-political drivers that are well-documented in other datasets.

### 2.2 Broader Africa Research

#### Geopolitical Drivers in Africa

The dominant state-actor geopolitical driver in Africa is **Russia's strategic contest for Sahel influence**, which is structurally distinct from its European operations because it exploits existing post-colonial grievances rather than creating new ones. The Wagner Group (rebranded "Africa Corps" after Prigozhin's death), operating in Mali, Burkina Faso, the Central African Republic, Libya, and Sudan, pursues a dual-track model: security services in exchange for mining rights and narrative capture. The information operations component — Sahel "ghost reporters" generating pro-Russian, anti-French content in local languages, fake Facebook pages spreading Russian narratives, amplification of anti-ECOWAS sentiment — is explicitly designed to legitimise the Wagner military presence and delegitimise French and Western influence. The Carnegie Endowment notes that Russia "takes advantage of France's and other Western countries' worsening relations with Sahelian states" and long-standing failures to address root causes of instability — the information operations work because they amplify real grievances, not because they invent them.[^19][^20][^21][^22]

The **French counter-response** creates a reflexive hybridisation dynamic in the Sahel. France and its commercial contractors (notably Percepto International) have run counter-narrative operations that African publics increasingly perceive as self-serving propaganda, which in turn validates the anti-Western meta-narrative that Russia cultivates. Niger and Burkina Faso restricting TV5Monde and RFI in 2026 reflects the endpoint of this dynamic: French state media becomes itself a target of narrative delegitimisation, with local publics unable to distinguish authentic journalism from state messaging.[^23][^24]

**China's African information posture** is less intrusion-oriented than Russia's, focusing primarily on BRI narrative management and countering "debt-trap diplomacy" framings in international media. The EEAS 4th FIMI report notes China accounts for 6% of attributed FIMI incidents globally, with regional hubs specifically targeting Sub-Saharan Africa. Chinese operations in Africa are predominantly **loose-definition** Type 1c: co-ordinated amplification networks and state-media (CGTN, Xinhua, ChinAfrica) promotion of counter-narratives, without documented intrusion components targeting African democratic institutions. This is consistent with China's broader "sharp power" doctrine: managing perception rather than disrupting infrastructure.[^1]

**The electoral hybridisation pattern** is also visible in Africa. The EEAS 4th FIMI report notes that Russia targeted elections in "Côte d'Ivoire" in 2025 alongside European states, replicating patterns seen in the Sahel. Commercial actors — particularly Archimedes Group (Israel) and Team Jorge (Israel) — conducted documented election-interference operations in Nigeria 2015/2019, Kenya 2022, Senegal 2019, Congo, Togo, and Tunisia. These are explicitly **strict-definition hybrid** operations where real intrusions (SS7 exploitation, Gmail/Telegram hacks) were combined with CIB influence campaigns. The commercial contractor model in Africa differs from the state-actor model in that the client is often the incumbent regime itself paying to manipulate its own electorate rather than an external power projecting force.[^25][^18][^1]

#### Economic Drivers in Africa

The **low cyber-resilience / high digital growth asymmetry** is the primary economic driver of Africa's ransomware epidemic. Ransomware attacks across Africa surged 134% between 2022 and 2024. Africa's cybersecurity market was valued at only $2.5 billion in 2020, while the continent loses more than $3.5 billion annually to direct cyberattacks. The Kearney analysis identifies a structural readiness gap: "countries in the region lack the strategic mindset, policy preparedness, and institutional oversight needed to address cybersecurity issues".[^26][^27]

South Africa bears the sharpest burden: it accounts for nearly 40% of reported continent-wide ransomware incidents, followed by Nigeria and Kenya. A Sophos Q1 2025 report found that 71% of South African organisations hit by ransomware paid the ransom — a dramatically high payment rate that directly incentivises further targeting. The criminal economic logic is explicit: "organisations are vulnerable, and will pay".[^28][^26][^8]

The **Africa influence-as-a-service market** is an emerging economic driver specific to the continent. ISS research on South Africa's 2024 election found a domestic paid-influencer market in which operators charge per post amplification, sell hashtag manipulation services, and export their techniques transnational to other African election cycles. This is a commercially-driven loose-definition cyber-enabled influence ecosystem that has emerged organically from Africa's high social-media growth rates and weak platform moderation capacity, and is now a documented driver of information environment degradation.[^29][^30]

#### Technical Drivers in Africa

**Mobile-first internet architecture** with WhatsApp as the dominant information-distribution channel creates a technically distinct threat environment from the Western social-media platforms that most disinformation research tools are optimised for. Disinformation distributed via WhatsApp group networks — a closed, encrypted architecture — is structurally invisible to the detection methods used in European and North American contexts, allowing even relatively unsophisticated influence operations to scale undetected.[^31][^30]

**Limited platform moderation capacity in African languages:** Most Meta, Google, and X content moderation tools are optimised for English, French, and other European languages. Disinformation in Hausa, Swahili, Zulu, Bambara, Tigrinya, or Wolof reaches audiences far larger than these tools can monitor. This is a technical asymmetry that structurally advantages influence operators in African information environments.[^30]

**Rapid, uneven digitalisation:** The World Bank Cyber Threats to the Financial Sector report notes that African financial institutions' rapid cloud migration, without corresponding security investment, creates large exposed attack surfaces. The MTN pan-African subscriber-data breach (AF-20 in the dataset), involving 22 markets, is a consequence of this structural over-extension.[^32]

***

## Part 3: South Africa–Specific Drivers

### 3.1 From the PDF Dataset

The PDF's South Africa incidents are exclusively in the criminal extortion category: Transnet (AF-14), TransUnion (AF-15), Experian (AF-16), Cell C (AF-17), Sibanye-Stillwater (AF-18), Astral Foods (AF-19), and the Q4 2024 industrial cluster (AF-6). The continental observations note that "South Africa and Tunisia account[ed] for the most reported attacks in the region" in Q4 2024. The AF-14 Transnet entry makes one geopolitically-significant observation: the attack's timing, days after the 2021 KwaZulu-Natal unrest, "fuel[led] unverified public speculation of coordinated economic destabilisation" — though investigators concluded the two events were unrelated.

This is an analytically important negative finding: the dataset cannot distinguish between a financially-motivated criminal ransomware hit and a state-sponsored disruptive operation designed to look like one. The absence of attribution evidence does not confirm absence of geopolitical motivation.

### 3.2 Broader South Africa Research

#### Geopolitical Drivers Specific to South Africa

South Africa's geopolitical position creates a uniquely complex hybrid threat environment. As the only African member of BRICS, and as a state pursuing explicit non-alignment and "active neutrality" in the Russia-Ukraine conflict, it occupies a strategic pivot position that makes it simultaneously:

1. **A target for Russian influence maintenance** — to prevent South Africa from moving toward the Western position on Ukraine, sanctioning Russia, or allowing weapons transit to Ukraine; and
2. **A target for Western counter-pressure** — including the Trump administration's coercive narrative campaign (Expropriation Act, AfriForum lobbying, Elon Musk amplification, Executive Order 14204, aid suspension) designed to pressure Pretoria on its BRICS posture and ICJ genocide case;[^33][^34]
3. **A target for Israeli influence operations** as the lead applicant in the ICJ genocide case — documented through paid Google/YouTube "hasbara" advertising explicitly targeting the ICJ framing and IDF covert media channels; and[^35][^36][^37]
4. **An arena for domestic political influence operations** as South Africa's first coalition government in 30 years navigates fragile multi-party dynamics.

The ISS 2024 election study found that Russia's narrative objectives were visible in South Africa's 2024 election information environment, and that at least one prominent South African influencer claimed to have been paid by Russian agents to amplify destabilisation narratives at a rate of R50 per engagement. This cannot be independently verified, but it is consistent with the documented Wagner-linked paid-influencer networks operating across the continent.[^22][^30]

The **ICJ case as a geopolitical trigger for information operations** is specific to South Africa and deserves separate attention. South Africa filed its genocide application in December 2023; the case remains live through 2026. The Israeli state's response has included a documented hybrid information campaign: paid Google ads at the top of ICJ-related search results; a $45 million Google/YouTube advertising contract (June 2025) for global narrative promotion; and IDF Spokesperson's Unit covert media channels posing as independent outlets. This is a real-world example of **loose-definition cyber-enabled influence** (Type 1c) with South Africa as an identified adversarial audience — and it uses the commercial paid-advertising infrastructure of private US technology companies, not intrusion techniques.[^38][^39][^36][^37][^35]

**South Africa's BRICS positioning** also creates information environment vulnerability from a different angle: Russia and China's active courtship of BRICS as a counter-Western platform means that South African public opinion is a legitimate influence target for both pro- and anti-BRICS narrative campaigns. The Transnational Institute's analysis notes that BRICS countries now account for 46% of global GDP and 55% of the world's population, making the ideological contest over BRICS legitimacy a genuinely high-stakes global narrative contest.[^7][^40]

#### Economic Drivers Specific to South Africa

South Africa's combination of **relatively high internet penetration (approximately 26 million social media users)**, **high digital payments adoption**, **large industrial and mining sector**, and **critically underfunded public-sector cybersecurity** makes it the most attractive ransomware target on the continent. It accounts for 40% of Africa's ransomware incidents; the Sophos 71% payment rate; and six of the seven qualifying Africa incidents in the PDF dataset.[^41][^26][^28]

The **domestic political-economy of influence** is a distinctive South African driver. ISS research on the 2024 election found that the MK Party and EFF were the largest online "communities" in a sample of 1.2 million X documents and over 177,000 Facebook documents, and both "appear to have benefitted from paid influencers including those ideologically aligned to the party". This is a domestic political-commercial influence market — not a foreign operation — that is generating its own hybridisation dynamic. The ISS notes that this market is being "exported" to other African election cycles by South African operators, making South Africa a net exporter of influence techniques as well as a target.[^42][^29][^30]

The **Starlink/BEE regulatory conflict** represents a commercially-driven geopolitical-economic driver that is specific to South Africa and entirely documented: Elon Musk's personal financial interest in obtaining a BEE exemption for Starlink directly intersects with his amplification of anti-South-African narratives and the Trump administration's coercive policy posture. This is a case where private commercial interests, geopolitical influence, and cyber-enabled (Grok/X) information operations are functionally integrated — a novel hybrid driver model.[^34][^43]

#### Technical Drivers Specific to South Africa

South Africa's **relative digital maturity within the African context** creates a double-edged technical exposure: it is the continent's most attractive target precisely because it has more digital assets to compromise, but it also has marginally more defensive capacity than its neighbours. The ISS 2024 election study found that fact-checkers and traditional media played a "significant role" in debunking disinformation — a capacity most other African states lack.[^30]

The country's **shift to WhatsApp and smaller, localised encrypted networks** for political communication is noted by ISS researchers as a major emerging technical driver of disinformation's evasion of detection. As content moves from public X and Facebook feeds (where content warnings and third-party fact-checkers operate) to private WhatsApp group chains, the monitoring and intervention capacity of regulators, civil society, and platforms collapses.[^30]

The **Meta decision to end third-party fact-checking** in early 2025 — removing Africa Check's content warnings from South African Facebook content — eliminates a key technical countermeasure precisely when influence operations are intensifying and AI-generated content is proliferating. Trump's executive order purporting to "stop government censorship" on social media reinforces this deregulatory technical environment globally.[^30]

**Outdated and under-resourced public-sector cyber infrastructure** — demonstrated by Transnet running an application that could be penetrated with Shamoon-variant ransomware, and by the TransUnion SFTP server protected by the password "Password" — is a persistent technical driver of criminal hybrid operations. South Africa's National Cybersecurity Policy Framework remains under-resourced relative to the threat surface, and public-sector entities (Transnet, SASSA, SARS, SOEs) carry disproportionate risk.

***

## Part 4: The Hybridisation Trend — Synthesis Across Scales

The EEAS identification of hybridisation as a top-three trend reflects a structural logic that applies at all three geographic scales, though with different mechanisms:[^1]

**Globally:** Hybridisation is driven by strategic rational choice — blending operations is more cost-effective than running separate ones, and the fusion creates synergies (leaked data provides authentic content for influence campaigns; influence operations create the social context that makes phishing lures credible). The dataset's North America section notes this explicitly: "every one of the four qualifying North American hack-and-leak operations was preceded by spearphishing (2b), and three deployed cutout personas (2g) to disguise state attribution". The intrusion and the influence operation are not parallel tracks; they are a single integrated weapon.

**In Africa:** Hybridisation at the state-actor level (Russia, China, commercial contractors) operates largely in the **loose-definition** domain — no intrusions required — because the information environment is malleable enough with organic amplification alone. The criminal hybridisation (ransomware + doxing extortion) operates in the strict-definition domain, but its influence component is commercially rather than politically motivated. The two tracks are increasingly converging: state actors use commercially-operated fake-influencer networks, and criminal groups observe that their disruptions (Transnet port shutdown) have geopolitical effects they can leverage or sell.

**In South Africa:** All three hybridisation pathways are simultaneously active:
1. Criminal strict-definition (ransomware + leak-site doxing) — financially driven, internationally-sourced perpetrators targeting domestic organisations
2. State-actor loose-definition (Russian election narrative interference, Israeli paid advertising on ICJ framing, US/Trump administration political coercion narratives) — geopolitically driven, using commercial cyber infrastructure with no intrusion
3. Domestic commercial loose-definition (paid influencer networks, algorithm-gaming, rage-bait amplification) — politically and commercially driven, domestic perpetrators with transnational reach

This three-pathway model is analytically important for keynote framing: South Africa's security leaders need to build defences against adversaries with fundamentally different motivations, capabilities, and legal statuses — simultaneously.

***

## Analytical Note: Selection Bias and Non-English Source Gaps

The PDF dataset's ≥0.7 threshold, and the English-language research ecosystem that underlies it, create three documented gaps that affect the drivers analysis:

1. **Under-representation of loose-definition operations in Africa** — because these require no intrusion, they score below the threshold. The Russian Sahel narrative offensive, the Archimedes/Team Jorge commercial operations, the Israeli paid-advertising campaign targeting South Africa, and the domestic influence-as-a-service market are all real, documented drivers that are invisible in the dataset.[^18][^36][^29][^25]

2. **Under-representation of Western state operations as drivers** — the CENTCOM fake-persona networks, GCHQ/JTRIG documented false-flag and CIB operations, the Pentagon's evolving paid-advertising influence network, and the Trump administration's overt-but-deceptive South Africa narrative campaign are structural drivers that the research ecosystem has been slow to document with the same systematic rigour applied to Russian and Chinese operations.[^44][^16][^33]

3. **Under-representation of Francophone, Swahili, Hausa, and Arabic-language disinformation ecosystems** — Forbidden Stories and French-language sources (Le Monde, France24, RFI) provide the most systematic evidence on the Sahel narrative contest, and the German-language Der Spiegel contributed the Team Jorge investigation. English-language synthesis of these sources remains incomplete, which systematically understates Africa's information environment complexity for Anglophone audiences.[^21][^45][^46]

For keynote audiences at ITWeb Security Summit, the practical implication is that threat intelligence drawn solely from English-language sources — including most commercially available threat intelligence feeds and think-tank reports funded by DoD, State Department, or EU institutions — will systematically over-represent the Russian/Chinese threat and under-represent the Western-state, commercial-contractor, and domestic political-actor threats operating in the same information environment.

---

## References

1. [4th EEAS Report on Foreign Information Manipulation ... - MediaWell](https://mediawell.ssrc.org/news-items/4th-eeas-report-on-foreign-information-manipulation-and-interference-threats/) - FIMI continues to adapt to technological advances, particularly in Artificial Intelligence (AI). AI-...

2. [[PDF] World Rewired: Navigating a Multi-Speed, Multipolar Order](https://www.jpmorganchase.com/content/dam/jpmorganchase/documents/center-for-geopolitics/jpmc-world-rewired.pdf) - The informal alignment of China, Russia, Iran and North Korea, sometimes labelled “CRINK”, reflects ...

3. [Geopolitics and Cyber Risk: How Global Tensions Shape the Attack ...](https://www.rapid7.com/blog/post/it-geopolitics-and-cyber-risk-how-global-tensions-shape-the-attack-surface/) - Geopolitical tensions and sanctions often create conditions in which state-aligned hackers operate w...

4. [Rethinking Cyber Deterrence in a Multipolar World - RUSI](https://www.rusi.org/explore-our-research/publications/emerging-insights/rethinking-cyber-deterrence-multipolar-world) - This paper balances existing prevailing scepticism about the feasibility of cyber deterrence against...

5. [The Geopolitical-Cyber Convergence: 2025 Predictions - ZeroFox](https://www.zerofox.com/blog/the-geopolitical-cyber-convergence-2025-predictions-from-zerofox-experts/) - The increasingly complex geopolitical environment is shaping the cyber threat landscape in 2025, cau...

6. [Multipolarities – The World-Order Visions of Others](https://www.swp-berlin.org/en/publication/multipolarities-the-world-order-visions-of-others) - Across both the globe and ideological boundaries, “multipolarity” has become a central point of refe...

7. [BRICS Summit 2025: will slow and steady actually win the race?](https://issafrica.org/iss-today/brics-summit-2025-will-slow-and-steady-actually-win-the-race) - Dr Samir Puri, Chatham House's Centre for Global Governance and Security Director, says: 'BRICS has ...

8. [How Ransomware Economics Drives the Global Cybercrime Industry](https://kbi.media/how-ransomware-economics-drives-the-global-cybercrime-industry/)

9. [2026 Global Cyber Risk Outlook: How AI and RaaS are Accelerating ...](https://www.quorumcyber.com/insights/2026-global-cyber-risk-outlook-how-ai-and-raas-are-accelerating-attacks/) - It examines how attack patterns and threat trends are evolving, and how they are likely to develop i...

10. [[PDF] Information manipulation in the age of generative artificial intelligence](https://www.europarl.europa.eu/RegData/etudes/BRIE/2025/779259/EPRS_BRI(2025)779259_EN.pdf) - Laundering deceptive narratives via Wikipedia thus helps inject disinformation into AI chatbots, whi...

11. [Evidence of AI's impact from a state-backed disinformation campaign](https://academic.oup.com/pnasnexus/article/4/4/pgaf083/8097936) - Our results illustrate how generative-AI tools have already begun to alter the size and scope of sta...

12. [AI and the Future of Disinformation Campaigns - CSET](https://cset.georgetown.edu/publication/ai-and-the-future-of-disinformation-campaigns-2/) - This report describes how AI can supercharge current techniques to increase the speed, scale, and pe...

13. [Five Eyes just made life harder for bulletproof hosting providers](https://cyberscoop.com/bulletproof-hosting-providers-sanctions-mitigation-media-land/) - The Treasury Department, along with officials from the United Kingdom and Australia, imposed sanctio...

14. [US cracks down on Russian bulletproof hosting services enabling ...](https://www.elliptic.co/blog/us-cracks-down-on-russian-bulletproof-hosting-services) - US cracks down on Russian bulletproof hosting services enabling cybercrime. Elliptic. 19 November, 2...

15. [[PDF] Mitigating Risks From Bulletproof Hosting Providers](https://www.ic3.gov/CSA/2025/251119.pdf) - The authoring agencies have observed a marked increase in cybercriminal actors using BPH infrastruct...

16. [Renee DiResta - Fewer Bots, More Ads - LinkedIn](https://www.linkedin.com/posts/reneediresta_fewer-bots-more-ads-the-pentagons-evolving-activity-7460722130939387905-zJ3h) - In 2022, I co-authored "Unheard Voice," a Stanford Internet Observatory / Graphika report on Pentago...

17. [Archimedes Group - Wikipedia](https://en.wikipedia.org/wiki/Archimedes_Group)

18. [Team Jorge: The Israeli contractors behind disinformation and ...](https://peoplesdispatch.org/2023/02/17/team-jorge-the-israeli-contractors-behind-disinformation-and-election-interference/) - An undercover investigation into disinformation is prompting calls for inquiries by political partie...

19. [Russia's Growing Footprint in Africa's Sahel Region](https://carnegieendowment.org/russia-eurasia/research/2023/02/russias-growing-footprint-in-africas-sahel-region) - Through the infamous Wagner mercenary group, Moscow is inserting itself in countries such as Mali an...

20. [Russia in Africa: Private Military Proxies in the Sahel](https://gjia.georgetown.edu/global-governance/russia-in-africa-private-military-proxies-in-the-sahel/) - By 2019, more than a thousand Wagner mercenaries were operating in CAR, exploiting natural resources...

21. [Propaganda Machine: Russia's information offensive in the Sahel](https://forbiddenstories.org/propaganda-machine-russias-information-offensive-in-the-sahel/) - In the Sahel and the Central African Republic, Moscow's disinformation agents spare no expense in ma...

22. [The 'ghost reporters' writing pro-Russian propaganda in West Africa](https://www.aljazeera.com/features/2025/3/20/the-ghost-reporters-writing-pro-russian-propaganda-in-west-africa) - Disinformation researcher Nina Jankowicz said she was “quite surprised they chose someone who has di...

23. [Alliance of Sahel States Members Niger and Burkina Faso Restrict ...](https://www.instagram.com/p/DYHQ_0hCofb/) - ... French media. The country recently suspended TV5 Monde over accusations of biased reporting and ...

24. [How Russian disinformation toppled government after government ...](https://www.washingtonpost.com/technology/2023/10/21/percepto-africa-france-russia-disinformation/) - Pro-Russian fake news sites populated YouTube and pro ... disinformation campaigns in the Sahel have...

25. [Who is behind Israel's Archimedes Group, banned by Facebook for ...](https://www.timesofisrael.com/who-is-behind-israels-archimedes-group-banned-by-facebook-for-election-fakery/) - Website of company that boasted it would 'change reality' for its clients was registered by Grey Con...

26. [African Businesses Face Growing Ransomware Crisis As Attacks ...](https://techtrends.africa/african-businesses-face-ransomware-attacks/) - Ransomware attacks across Africa have surged to unprecedented levels, with cybersecurity firms repor...

27. [Cybersecurity in Africa—a call to action](https://www.kearney.com/documents/291362523/296371292/Cybersecurity+in+Africa%E2%80%94a+call+to+action.pdf/cb6f42c4-570c-ddd7-4f8c-719507863674?t=1683214143000)

28. [Africa: Ransomware - What It Is and Why It's Your Problem](https://allafrica.com/stories/202601190049.html) - Analysis - Ransomware is a type of malicious software that makes a victim's data, system or device i...

29. [SA disinformation menace flags need for Africa's ...](https://www.dailymaverick.co.za/article/2025-03-18-disinformation-menace-africas-democracies-need-to-guard-against-influencer-networks/) - New research shows that key figures in South Africa’s domestic online influence industry are engaged...

30. [Africa's democracies must guard against local online ...](https://issafrica.org/iss-today/africa-s-democracies-must-guard-against-local-online-influencer-networks) - New research shows that key figures in South Africa’s domestic online influence industry are engaged...

31. [Elections will reveal SA's exposure to social media digital ...](https://www.dailymaverick.co.za/article/2024-05-28-elections-will-reveal-sas-exposure-to-social-media-digital-influence-as-service-for-manipulation/) - Without access to social media data, ensuring voters have verifiable information rather than manipul...

32. [[PDF] Cyber Threats to the Financial Sector in Africa - World Bank Document](https://documents1.worldbank.org/curated/en/099830405172214598/pdf/P16477000601530760af01093740e385fe8.pdf)

33. [Addressing Egregious Actions of The Republic of South Africa](https://www.whitehouse.gov/presidential-actions/2025/02/addressing-egregious-actions-of-the-republic-of-south-africa/) - February 7, 2025. Related. Fact Sheet: President Donald J. Trump Addresses Human Rights Violations i...

34. [‘White supremacists in suits and ties': the rightwing Afrikaner group in Trump's ear](https://www.theguardian.com/us-news/2025/feb/14/trump-musk-south-africa-afriforum) - Trump's asylum offer to South Africa's white minority follows years of AfriForum lobbying on Elon Mu...

35. [10 April 2026 Soldiers and journalists say the Israeli army's](https://www.facebook.com/groups/564144257700789/posts/2118669168914949/) - On the positive side, this article seemed to contain less of the boilerplate bias, misinformation, d...

36. [Israel Google ad accuses South Africa of 'blood libel' when ...](https://www.middleeasteye.net/news/israeli-ad-accusing-south-africa-blood-libel-targets-google-users-searching-icj) - The accusation of 'malicious blood libel' appears at the top of Google's results page when searching...

37. [Google signed a $45 million contract with the Israeli prime minister's ...](https://www.facebook.com/middleeastmonitor/posts/google-signed-a-45-million-contract-with-the-israeli-prime-ministers-office-to-r/1182422403917787/) - Whoops it's owned by an Israeli-Canadian. And has helped Israel in war. The guy is Zionist too! Oh w...

38. [ICJ to deliver order in the case South Africa vs. Israel - DIRCO](https://dirco.gov.za/icj-to-deliver-order-in-the-case-south-africa-vs-israel/) - The International Court of Justice (ICJ) will today, 24 May 2024, deliver an order in the case, Sout...

39. [South Africa notes Israel's response filing to the ICJ - The Presidency](https://www.thepresidency.gov.za/south-africa-notes-israels-response-filing-icj) - The State of Israel filed its response on Thursday, 12 March 2026. The Court had initially ordered I...

40. [BRICS: BRICS 2025 - Friedrich-Naumann-Stiftung](https://www.freiheit.org/brics-what-are-key-issues-2025) - ... security, development and human rights policy. Global Security Hub · EN · DE · Global World Orde...

41. [Online influence and disinformation – preparing for South Africa's polls](https://issafrica.org/iss-today/online-influence-and-disinformation-preparing-for-south-africa-s-polls) - The electoral commission’s ground rules alone can’t be expected to insulate the country from harmful...

42. [Under the influence? Online mis/disinformation in South Africa's May ...](https://issafrica.org/research/southern-africa-report/under-the-influence-online-mis-disinformation-in-south-africa-s-may-2024-election) - This report spotlights the tactics, narratives and actors who drive such campaigns and offers lesson...

43. [How a land law sparked Elon Musk's accusations of 'genocide ...](https://www.nbcnews.com/news/world/south-africa-racist-white-farmers-trump-musk-genocide-ramaphosa-rcna190749) - How a land law sparked Elon Musk's accusations of 'genocide' against his home country. Musk has desc...

44. [Fewer Bots, More Ads: The Pentagon's Evolving Online Influence ...](https://www.lawfaremedia.org/article/fewer-bots--more-ads--the-pentagon-s-evolving-online-influence-campaigns) - Fewer Bots, More Ads: The Pentagon's Evolving Online Influence Campaigns. Renée DiResta. Wednesday, ...

45. ['Team Jorge' ― how disinformation threatens democracy - DW.com](https://www.dw.com/en/team-jorge-investigation-raises-concerns-about-threat-to-democracy/a-64708627) - A major new investigation into election manipulation has exposed weaknesses in the security of inter...

46. [France faces a crossfire of Russian and American disinformation](https://www.lemonde.fr/en/les-decodeurs/article/2026/02/02/france-faces-a-crossfire-of-russian-and-american-disinformation_6750034_8.html) - Who is Candace Owens, the pro-Trump influencer spreading transphobic fake news about Brigitte Macron...

