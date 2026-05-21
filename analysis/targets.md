---
layout: default
title: "Targets of Hybrid Cyber-Influence Operations"
---

# Targets of Hybrid Cyber–Influence Operations: Sectors, Communities, Regions, and Targeted Decisions

**Prepared for ITWeb Security Summit 2026 Keynote Research**
**Based on: ITWeb Hybrid Incidents PDF (file:237) + Alto Intelligence Mining Report (file:238) + independent research**
**Taxonomy: (1) Cyber-enabled influence (1a–1h) | (2) Influence-enabled cyber (2a–2h) | (3) Parallel cyber–influence**

***

## Executive Summary

Hybrid cyber–influence operations do not target sectors, communities, and processes randomly. They exhibit clear, strategic targeting logic that differs by actor class, campaign type, and geographic scope. Three structural patterns emerge across all three geographic scopes:

1. **Decision-proximity targeting:** Both state actors and criminal groups aim at the decisions that matter most — elections, military-support choices, contract negotiations, regulatory approvals, and financial transactions. The target is not always the institution that holds the decision; it is often the information environment that shapes the decision-makers.

2. **Resilience-asymmetry exploitation:** Organisations and communities with high value but low cyber or information resilience attract disproportionate targeting — the "soft belly" logic explains why African critical infrastructure, healthcare, and community-level electoral processes are over-represented in the criminal dataset, and why diaspora communities, ethnic minorities, and civil society in authoritarian-adjacent environments are systematically targeted for influence operations.

3. **The loose/strict distinction is sector-specific:** Strictly-defined hybrid operations (requiring an unauthorised intrusion) are concentrated in government, elections, media, defence, and high-value private-sector organisations. Loosely-defined cyber-enabled influence (no intrusion) is concentrated in electoral and civil-society environments, natural-resource and extractive sectors, diaspora and minority communities, and the cognitive dimension of military conflicts. The Alto Intelligence report provides a detailed case study of the latter category for the mining sector specifically.

***

## Part 1: Global — Sectors, Communities, and Processes Targeted

### 1.1 From the PDF Dataset

Reading across all qualifying incidents (≥0.7), the PDF dataset reveals the following victim categories:

| Victim sector/category | Dataset incidents | Dominant operation type | Notes |
|---|---|---|---|
| Government / parliament | EU-2, EU-15, EU-21, EU-35, NA-5, NA-6, NA-7, NA-9, AS-3, AS-4 | Strict (intrusion + influence) | APT spearphish → espionage → leak/post |
| Elections / voters / electoral process | EU-1, EU-22, EU-23, EU-33, NA-5, NA-6, NA-7, NA-9, AS-8, AS-9 | Both strict and loose | Hack-and-leak + CIB; also pure CIB without intrusion |
| Media / broadcasters | EU-37 (TV5Monde), EU-18, EU-19, multiple EU Doppelganger/1c incidents | Strict (hack-and-post/takeover) | Media hijacking for propaganda; also fake domains (loose) |
| Financial sector / banking | EU-40 (NoName), NA-16 (Change Healthcare adjacent), NA-14 | Strict (DDoS, ransomware) | DDoS as political signalling + ransomware extortion |
| Healthcare | NA-16 (Change Healthcare), AS-4 | Strict (ransomware, malware) | Healthcare payments; Iranian repression of civil society |
| Private sector (entertainment, hospitality, food, mining) | NA-13 (Sony), NA-14 (MGM), NA-15 (JBS), AF-18 (Sibanye) | Strict (ransomware, hack-and-leak) | High-profile/high-revenue corporate targets |
| NATO / military-support decisions | EU-40, EU-39, EU-15, EU-35 | Both | Financial sector DDoS timed to tank/Ukraine decisions; phishing of defence institutions |
| Ethnic minorities / diaspora communities | AS-1 (Uyghurs), AS-4 (Baluchi, Kurdish, Turkic) | Strict (surveillance malware + influence) | State-level transnational repression |
| Civil society / journalists / dissidents | AS-4, EU-18 (Baltic), EU-22 (Macron campaign staff) | Both | Account compromise, smear operations, fake content |

The PDF's continental observations explicitly flag: "five overlapping Russian influence franchises dominate [Europe]: Doppelganger, Operation Overload, RT Deutsch mirrors, Ghostwriter, and Storm-1516/R-FBI" — all targeting the same cluster of victims: elections, democratic institutions, media, and public opinion on Ukraine. The North America continental observations note that the continent is "the global capital of hack-and-leak operations", with elections and democratic campaigns as the defining target. The Asia observations introduce a distinct target category: ethnic and religious minority communities subject to state-directed transnational cyber-repression.

### 1.2 Broader Global Research: What the PDF Misses

#### Elections and Democratic Processes (both strict and loose definition)

Elections are the most consistently targeted process globally, by both state and commercial actors. The 2023 Nigerian election saw what researchers describe as "likely the first deluge of AI-generated electoral content on the [African] continent" — including fake endorsements from Hollywood celebrities and AI-generated audio claiming candidates intended to rig the vote, distributed hours before polling. The EEAS 4th FIMI report confirms elections as the primary temporal trigger for FIMI escalation globally. At least 24 African countries held elections in 2024 and 17 in 2025, making the continent the world's most intensive electoral battleground for influence operations by volume.[^1][^2][^3]

The processes being targeted within democratic cycles include not just the vote itself but upstream decisions: candidate selection, media narrative formation, judiciary and election commission credibility (Africa Check documents that in Nigeria and Kenya, disinformation specifically targeted these institutions), and post-election legitimacy. This upstream targeting means that the actual voting infrastructure is often a secondary target — the primary target is the cognitive environment in which voters, media, and institutions reach their judgments.[^4]

#### Military-Support Decisions (both definitions, with strict definition for effect)

NoName057(16)'s DDoS campaign against European banks explicitly timed attacks to coincide with named political decisions: Italian G7 reaffirmation of Ukraine support, Czech Republic training of Ukrainian soldiers, German Leopard 2 tank decisions, Sweden's NATO accession. The target is not the banks themselves — it is the decision-maker's perception of cost. Ukrainian IT Army's DDoS campaign against Russian and Belarusian infrastructure (EU-39) mirrors this precisely: the target is Russian public morale and international perception of Russian vulnerability. In both cases, financial-sector entities are being used as proxy targets to shape decisions in the military and political domain.

#### Critical Infrastructure and High-Impact Private Sector (strict definition dominant)

Change Healthcare (NA-16) is the global dataset's most impactful single incident: approximately 100 million Americans' health data compromised, US$2.87 billion in response costs, weeks-long disruption to the US pharmacy and claims-processing system. The influence layer — ALPHV's fake law-enforcement seizure notice to disguise an exit-scam against its own affiliate, and RansomHub's subsequent re-extortion claim — is a novel case where threat-actor-to-threat-actor deception is deployed as an influence operation within the criminal ecosystem itself. JBS Foods (NA-15) demonstrated that food-supply infrastructure operating across three continents can be simultaneously disrupted by a single RaaS attack. Both cases target not only the immediate victim but the public's perception of systemic resilience.

#### The Extractive and Critical Minerals Sector: A Specialist Target (loose definition dominant)

The Alto Intelligence report provides a granular taxonomy of a targeting category largely invisible in the Hybrid Incidents PDF: **state-aligned and commercial Advanced Persistent Manipulator (APM) operations targeting mining governance, contract negotiations, and social license decisions**. This is almost entirely a loose-definition phenomenon — no intrusions are required because the attack surface is the information environment rather than IT systems — and it is therefore systematically underrepresented in intrusion-threshold datasets like the PDF.

Alto documents six categories of targeted decisions in the extractive sector:

1. **Contract negotiations and regulatory approvals:** In multiple West African jurisdictions, Russian and Chinese-aligned APM networks ran narrative pre-positioning campaigns *before* formal regulatory decisions, creating an information environment favourable to aligned operators. The Barrick/Loulo-Gounkoto dispute in Mali is a documented case: Alto tracked two simultaneous narrative framings — one for Russian/French-language African audiences (sovereignty milestone), one for English-language financial media (expropriation risk) — operating around the same factual events. The narrative shaping preceded the contractual outcome.

2. **Commodity pricing and investment decisions:** A Los Pelambres (Chile) supervisors' union dispute was reframed into a global copper supply crisis narrative across three language environments within 72 hours, contributing to pricing dislocations exceeding the actual supply impact. Mandarin-language policy signals around Chinese steel decarbonisation standards moved commodity sentiment on iron ore before English-language analysts had processed the same signals.

3. **Social license to operate / permitting:** At the Salar de Atacama lithium project, genuine local water-rights advocacy was amplified by geopolitical commentary networks and reframed as "green colonialism" — exacerbating permit scrutiny well beyond the operational realities at the site.

4. **Anti-competitive narrative targeting of strategic supply chains:** Dragonbridge — a Chinese state-linked CIB network — ran fake-account operations posing as Texas residents to oppose the Lynas Rare Earths processing facility, explicitly targeting US efforts to build non-Chinese rare earth processing capacity.

5. **ESG and joint-venture stakeholder decisions:** At Las Bambas (Peru, Chinese-operated copper mine), Russian state-aligned media reframed community opposition as evidence of resistance to Chinese investment, while Chinese channels reframed the same events as the Peruvian state favouring multinationals over local livelihoods — two opposing frames, both amplified simultaneously by APM networks with no connection to Cotabambas communities.

6. **Financing and development institution decisions:** At Reko Diq (Pakistan/Balochistan), three simultaneous narrative threads — security liability, geopolitical instrument, contested sovereignty — converged across different actor groups and language environments to create compound risk for capital allocation.

The Oregon Group's April 2026 analysis confirms this is now a sector-wide phenomenon: "disinformation is no longer just a PR nuisance for mining investors and companies, but is a direct investment risk".[^5]

#### Diaspora, Minority, and Transnational Communities (strict and loose definition)

Transnational repression targeting diaspora and minority communities is a globally documented pattern that combines strict-definition cyber operations with loose-definition influence. China's operations against Uyghur communities (AS-1 in the dataset: BadBazaar trojanised apps for device-level surveillance) and Iran's repression of Baluchi, Kurdish, and Turkic activists (AS-4: account compromise, SIM disabling, fake content, Telegram group infiltration) are the dataset's clearest examples. The US Congress' 2025 hearing on transnational repression documented coordinated Indian disinformation campaigns aligned with Hindu nationalist extremism targeting diaspora institutions, Canadian authorities documented a Chinese state operation targeting MP Michael Chiu and other community members, and the FBI has identified Russia, China, Iran, Ethiopia, and Rwanda as the leading practitioners. The Freedom House 2025 Transnational Repression report identifies 38 governments engaged in some form of transnational repression.[^6][^7][^8]

The targeted decisions in this category are: whether dissidents speak publicly, whether diaspora communities mobilise politically, whether journalists publish critical reporting, and whether foreign governments maintain political relationships with target states.

#### The Sony Pictures Precedent: Corporate Reputation and Artistic Expression as Targets

NA-13 (Sony Pictures) established that a state actor will target a private entertainment company to suppress artistic expression — the specific targeted decision was whether *The Interview* would be released. 100TB of data was exfiltrated and released in staged dumps, combined with a Shamoon-variant wiper and a "Guardians of Peace" false-flag persona. This is the earliest dataset example of a hybrid operation targeting corporate reputation as a coercion mechanism against both the company and its downstream partners (cinema chains).

***

## Part 2: Africa — Sectors, Communities, and Processes Targeted

### 2.1 From the PDF Dataset

Africa's qualifying incidents split into two distinct targeting clusters, as the continental observations explicitly note:

**Cluster 1 — CIB/political influence (11 cases, predominantly Russian-linked or domestic political-PR networks):** These are *not* in the qualifying dataset at ≥0.7 because they lack an intrusion component, but the continental observations explicitly reference them as the dominant influence pattern on the continent.

**Cluster 2 — Criminal double-extortion ransomware against private-sector and infrastructure targets (9 qualifying cases):**

| Incident | Target sector | Targeted decision/impact |
|---|---|---|
| AF-14 Transnet | Ports/logistics/critical infrastructure (SOE) | Force-majeure on container operations; supply chain coercion |
| AF-15 TransUnion | Financial services / credit bureau | Insurance-fee extortion of downstream banks; consumer data |
| AF-16 Experian | Financial services / credit bureau | Pure influence-enabled intrusion via client impersonation |
| AF-17 Cell C | Telecommunications | Customer data; reputational extortion |
| AF-18 Sibanye-Stillwater | Mining | Global IT disruption of a major gold/platinum group metals operator |
| AF-19 Astral Foods | Agriculture / food supply chain | Processing and delivery disruption |
| AF-20 MTN Group | Telecommunications | Pan-African subscriber data across 22 markets |
| AF-9 Kenya Airways | Aviation | Data exfiltration + leak-site reputational extortion |
| AF-6 Industrial cluster (Q4 2024) | Industrial / manufacturing | Multiple organisations; data extortion across industrial sectors |

The PDF's Africa continental observations note that South Africa and Tunisia "account for the most reported attacks in the region" in the Q4 2024 industrial cluster. The Transnet entry makes a notable observation: "the attack came days after the 2021 KwaZulu-Natal unrest, fuelling unverified public speculation of coordinated economic destabilisation — authorities concluded the two events were unrelated". This is an analytically important negative finding: researchers could not distinguish a financially-motivated attack from a state-sponsored one targeting critical infrastructure for destabilisation.

The PDF also notes the specific targeting of financial sector downstream clients in the TransUnion case: "TransUnion's corporate clients were approached separately and asked to pay smaller insurance sums — R1M for large clients, R100K for smaller ones — to be excluded from any future leak". The named targets include Absa, FNB, Standard Bank, Nedbank, Discovery, and TymeBank. This is an unusual pattern where the primary intrusion enables a cascading secondary influence campaign targeting the entire financial sector ecosystem.

### 2.2 Broader Africa Research

#### Elections: The Continent's Primary Influence Operation Target

Africa is now the world's most intensive electoral battleground for hybrid influence operations. Africa Check documents a systematic pattern across the 2023 Nigerian and 2022 Kenyan elections of disinformation specifically targeting three institutions: **independent media, the judiciary, and election management bodies**. The logic is consistent: undermine the credibility of the institutions that adjudicate disputed results before the results are disputed. The research shows that in Nigeria, political support groups announced their leader's victory before the Independent National Electoral Commission had collated results — a direct attempt to shape the "first framing" of the result in public memory.[^4]

The Cambridge Analytica operations in Nigeria (2015: presidential campaign for Goodluck Jonathan) and Kenya (2017: Jubilee Party campaign for Uhuru Kenyatta) established a commercial election-interference model in Africa that predates the Russian-linked operations and is often overlooked in the post-2016 US-focused literature. The targeted decision was the election outcome itself; the methodology was microtargeted data-driven messaging exploiting ethnic and religious cleavages.[^9][^10][^11][^4]

By 2023, the generative AI escalation transformed the scale of electoral targeting. The 2023 Nigerian presidential election experienced AI-generated celebrity endorsements, AI audio of candidates claiming vote-rigging intent distributed hours before polling, and AI-generated videos of fake sanctions threats attributed to US President Biden in the 2024 South African election. Fake Gabon President Ali Bongo videos raised fitness-to-rule questions that contributed to a 2019 coup attempt. Post-coup, AI-generated videos of Burkina Faso's Ibrahim Traore appeared speaking English — a language he has not been documented to speak fluently — providing propaganda content the regime itself may have found useful.[^1]

#### Mining, Natural Resources, and Contract Negotiations

The Alto Intelligence report provides detailed documentation of Russian and Chinese APM operations targeting mining governance specifically in Africa:

- **Niger and Mali (uranium, gold):** APM networks amplified criticism of Western mining operators within themes of exploitation and political interference, with narrative shaping preceding regulatory decisions and contract renegotiations affecting Western operators
- **Mali (Loulo-Gounkoto/Barrick):** Sputnik Africa and Rybar (a Russian military-aligned Telegram channel with over 1.3 million subscribers) framed the government seizure of Barrick's gold stockpiles as a "resource sovereignty milestone" in Russian and French-language African media, while English-language financial media framed the same events as "expropriation risk". The two frames reinforced each other: the sovereignty narrative provided political cover; the expropriation narrative drove market volatility. The dispute ultimately resulted in Barrick suspending operations in January 2025, the arrest warrant for CEO Mark Bristow, seizure of 3 metric tons of gold, and a protracted arbitration before a settlement in November 2025[^12][^13]
- **DRC (Kibali):** Labour tensions at Kibali (Barrick/AngloGold Ashanti joint venture) were "picked up and redistributed through French-language African media and geopolitical commentary channels at a velocity inconsistent with organic discourse," layering reputational exposure onto localised operational friction
- **Central African Republic:** Local media voices and community channels circulated messaging supportive of Russian engagement while portraying Western-backed operators as "misaligned with national interests" — narrative shaping that preceded and influenced permitting and contract decisions
- **Syama (Mali, Resolute Mining):** Alto identifies this highly-automated mine (80% autonomous operations) as a "concentrated target surface" for APM campaigns around job displacement, digital sovereignty, and foreign-control narratives — no targeted campaign detected yet, but the operational profile creates a ready-made credible narrative for APM exploitation

The China Africa critical minerals analysis from the ACSS (acknowledging its DoD funding) confirms that "African communities are responding with increasing sophistication — deploying local monitoring teams, countering disinformation" — suggesting that the information environment around Chinese mining investment is itself now a managed narrative contest. The Stimson Center's May 2026 analysis notes that the US–China competition for African critical minerals "has intensified to the point where narrative framing around specific projects now directly affects investment decisions".[^14][^15]

#### Critical Infrastructure and Financially-Motivated Targets

Africa's critical infrastructure targeting closely mirrors the criminal pattern in the dataset, with South Africa bearing the largest share. The State Security Agency has specifically named telecommunications, finance, transportation, energy, education, and healthcare as the sectors most affected. The National Health Laboratory Service attack (which disrupted blood testing for tuberculosis, HIV/AIDS, and mpox across a country with some of the world's highest rates of these diseases) and the attack on the Government Employees Pension Fund (GEPF — Africa's largest pension fund, >$85 billion) illustrate the unique severity of targeting healthcare and financial infrastructure in a developing-economy context.[^16][^17]

#### Community-Level and Civil Society Targeting

Africa Check's analysis of Nigerian and Kenyan elections identifies ethnicity, culture, and religion as the primary community-level cleavages exploited in influence operations. This is not incidental — elections in many African countries function as ethnic censuses, and influence operators systematically target ethnic solidarities to suppress cross-ethnic coalition-building and amplify intra-group polarisation. The Journal of African Elections (2025) confirms that "election misinformation on all major social media platforms is aimed at intimidating voters, certain ethnic groups, and party officials" across multiple African countries.[^18][^4]

***

## Part 3: South Africa — Sectors, Communities, and Processes Targeted

### 3.1 From the PDF Dataset

Nine of the dataset's twenty Africa incidents are South African, all strictly-defined criminal double-extortion operations:

| Incident | Target | Specific targeted decision/impact |
|---|---|---|
| AF-14 Transnet | Port and rail SOE | Force-majeure on container terminals; >60% of SA container traffic disrupted for a week; supply chain coercion; speculative post-KZN unrest narrative |
| AF-15 TransUnion | Credit bureau + downstream banks | Insurance-fee extortion of entire SA financial sector ecosystem; 54M records claimed; 200 corporate clients |
| AF-16 Experian | Credit bureau | Influence-enabled via fraudulent-client impersonation; consumer credit data |
| AF-17 Cell C | Telecoms | RansomHouse double-extortion; customer data leak |
| AF-18 Sibanye-Stillwater | Mining (gold/PGMs) | Global IT disruption affecting a JSE/NYSE-listed major |
| AF-19 Astral Foods | Agriculture / poultry | Processing and delivery downtime; food-supply chain disruption |
| AF-20 MTN Group | Telecoms (pan-African) | Subscriber data breach across 22 markets; headquartered in SA |
| AF-6 (cluster) | Industrial / infrastructure | Multiple SA industrial organisations in Q4 2024 cluster |

The PDF makes an important observation about the TransUnion extortion structure: the attack targeted not just TransUnion, but used TransUnion's data as leverage to mount a secondary extortion campaign against "Absa, FNB, Standard Bank, Nedbank, Discovery, TymeBank and others" — effectively weaponising the credit bureau's centrality to the entire financial sector. This is a specific feature of South Africa's concentrated financial architecture: a small number of chokepoint institutions (credit bureaus, payment processors, core SOEs) serve as natural amplification nodes for criminal hybrid operations.

The dataset's continental observations explicitly identify South Africa as "the centre of the continent's emerging double-extortion-ransomware epidemic" and note that "customer datasets used by major SA banks" have suffered "substantial regulatory and reputational fallout".

### 3.2 Broader South Africa Research

#### Government and State-Owned Enterprises: The Highest-Volume Target

Check Point's June 2025 threat intelligence report identified South Africa's government and military institutions as facing the highest number of cyberattacks per organisation per week on the continent at **3,480 attacks per week per organisation**, with a year-on-year increase of 69%. This represents a critical concentration: the sector that most needs public trust to function is simultaneously the most targeted by operations designed to erode it.[^19]

Specific 2024 public-sector incidents documented beyond the PDF dataset include:[^17][^20]
- **National Health Laboratory Service** — blood testing for TB, HIV/AIDS, mpox disrupted
- **Government Employees Pension Fund (GEPF)** — LockBit released 668GB in March 2024 after GEPF initially denied any data compromise
- **Companies and Intellectual Property Commission** — business registration and IP records
- **State Security Agency** — hacked days before the 2023 BRICS summit
- **South African Airways** — government/parastatal entity
- **South African Weather Service** — aviation and marine forecasting capability disrupted

The targeting of the SSA days before the BRICS summit is particularly significant: it is the closest case in the South African dataset to a potential geopolitical timing coincidence. The weather service attack disrupting aviation forecasting is notable because it affects one of the country's critical links to the global economy.

Kaspersky's 2025 research reports that in H1 2025, South Africa endured more than 6 million online attack attempts and 10.3 million malware-related incidents, with backdoor attacks up 123%, banking trojans up 136%, and spyware infections up 360%. South Africa loses approximately ZAR 1.8 billion annually to cyber-enabled financial fraud, with only 544 formal police reports filed — a gap of several orders of magnitude that signals both the under-capacity of enforcement and the near-complete impunity of attackers.[^21]

#### Elections and Domestic Political Influence: The 2024 Cycle

The 2024 South African general election was the first in which AI-generated electoral content played a documented role. AI-generated videos of US President Joe Biden threatening sanctions over South Africa's ICJ case circulated widely on social media. ISS research on the election information environment found evidence of domestic paid-influencer networks operating for both the MK Party and EFF, with at least one individual claiming payment for R50 per engagement to amplify destabilisation narratives. The ISS's 1.2-million X document and 177,000+ Facebook document sample identified both parties' online communities as having "benefitted from paid influencers including those ideologically aligned to the party".[^22][^23][^1]

The **targeted process** in this case was the GNU coalition formation — the specific decisions about which parties would enter government with the ANC and on what terms. Influence operations designed to maximise polarisation and minimise the ANC's ability to form a stable centrist coalition are a rational objective for multiple external actors (Russia: to prevent pro-Western alignment; domestic radicals: to force ANC–EFF or ANC–MK formations; commercial operators: to serve whichever client was paying).

#### Financial Sector Architecture as a Chokepoint

The TransUnion/Experian targeting pattern reveals a specific feature of South African targeting logic: the country's concentrated financial architecture (four major banks hold over 85% of banking assets; two credit bureaus hold essentially all consumer credit data) means that compromising a small number of entities creates leverage over the entire financial ecosystem. The insurance-fee secondary extortion campaign — approaching Absa, FNB, Standard Bank, Nedbank, Discovery, and TymeBank separately after the TransUnion breach — is only possible because of this architectural concentration.

This targeting logic is being exploited not just by criminal groups. The deliberate disruption of the financial sector's data trust infrastructure — even without an intrusion — can serve state-level strategic objectives. An adversary seeking to undermine South Africa's economic stability ahead of a BRICS summit, ICJ hearing, or major investment decision would find the financial sector's chokepoint architecture highly amenable to hybrid exploitation.

#### Mining and Resource Sector

South Africa's mining sector represents the intersection of the criminal targeting pattern (Sibanye-Stillwater, AF-18) and the APM narrative targeting documented by Alto. The country is the world's leading producer of platinum group metals, a major gold producer, and host to significant manganese, chrome, vanadium, and coal operations — all increasingly subject to the "critical minerals competition" narratives that Alto documents as shaping mining governance globally.

The Alto report's documentation of narrative operations targeting Sibanye's peer competitors (Barrick in Mali/DRC) and the broader "resource nationalism vs. foreign investment" narrative contest in Africa are directly relevant to South Africa's mining sector. South Africa's Expropriation Act, the Mining Charter, and BEE ownership requirements in the mining sector are all live narrative targets for the same APM networks that operated around Loulo-Gounkoto in Mali — they map almost perfectly onto the "sovereignty vs. investment" narrative architecture that Alto documents. The AfriForum/Trump narrative campaign already exploited the Expropriation Act in exactly this way, reaching US mining and agricultural investors through the Heritage Foundation and Tucker Carlson networks.[^24][^25][^5]

#### Community-Level Targeting: Race, Ethnicity, and the White-Minority Narrative

The Trump/AfriForum/Musk narrative campaign documented in the previous session is, in targeting terms, a **community-level influence operation** aimed at white Afrikaner communities within South Africa and Afrikaner-diaspora and conservative-sympathiser communities in the US. The targeted decisions are: (a) whether Afrikaners in South Africa remain politically aligned with the GNU or are recruited toward a separatist-nationalist narrative that weakens the coalition; (b) whether the US government and investment community treats South Africa as a hostile state; and (c) whether international mining and agricultural investors perceive South Africa's policy environment as expropriatory.

The ISS 2024 report found that the May 2024 election's information environment included disinformation specifically targeting Black South African voters through ethnic and class-based resentment narratives — a mirror of the white-community targeting, operating through different channels and serving different political objectives. South Africa's information environment is simultaneously targeted from multiple community angles, by actors with opposing political objectives, all converging on the same underlying vulnerability: the country's historically deep ethnic and racial cleavages.[^23]

***

## Part 4: The Strict/Loose Distinction by Target Category

The strict vs. loose definition distinction applies differently across victim categories:

| Target category | Strict-definition (intrusion required) focus | Loose-definition (no intrusion) focus |
|---|---|---|
| Elections / voters | Hack-and-leak of candidate material; intrusion into election infrastructure | CIB, AI-generated content, paid-influencer networks, deepfakes — dominant operationally |
| Government / parliament | Espionage (APT spearphish); credential theft → data exfiltration | Narrative operations targeting trust in institutions |
| Military-support decisions | DDoS against financial sector as political signalling (EU-40) | Coordinated messaging targeting public will to support Ukraine/military operations |
| Media / broadcasters | Hostile takeover (TV5Monde), account compromise (Ghostwriter) | Fake domains, impersonation of outlets, RT/Sputnik-style narrative injection |
| Financial sector | Ransomware double-extortion; DDoS | Narrative operations targeting trust in banking system |
| Mining / extractive | Ransomware targeting mining companies (Sibanye) | APM narrative campaigns targeting social license, contract negotiations, investment decisions — dominant |
| Diaspora / minorities | Surveillance malware, SIM disabling, account compromise | Smear campaigns, fake content, mass reporting of accounts |
| Healthcare | Ransomware disruption (NHLS, Change Healthcare) | Disinformation about medical topics (adjacent, not dataset-documented) |
| Electoral communities (ethnic/religious) | Not applicable | AI-generated ethnic targeting, paid influencer networks — entirely loose-definition |

The most important analytical observation for the keynote: **the loosely-defined category is, by volume, dominant in Africa and South Africa** — because elections, community-level social cohesion, and resource governance are the sectors most targeted, and these are operated almost entirely without intrusion components. The intrusion-threshold bias of the Hybrid Incidents dataset captures the criminal tail accurately but misses the political head of the distribution.

***

## Part 5: Non-English and Global South Perspectives on Targeting

The availability bias noted throughout this research series specifically affects the targeting picture. Several under-documented targeting patterns become visible only through non-Anglophone and Global South sources:

**Arabic/French-language targeting in Sahel:** Al Jazeera and Forbidden Stories document how Sahel populations are targeted by Russian-language narrative campaigns that are then translated into French and local languages by Wagner-linked "ghost reporters" — the primary audience being Francophone African publics whose political choices about French military presence and Western partnerships are the real targeted decision.[^26][^27]

**Mandarin-language commodity and policy signal targeting:** Alto's identification of Mandarin-language policy signals moving commodity sentiment before English-language markets react is a form of information asymmetry exploitation specific to China's state media architecture. The targeted decision is investor and analyst positioning, not public opinion.

**Swahili/Hausa/Zulu language targeting:** Democracy in Africa's analysis confirms that "social media platforms' safeguards, designed primarily for dominant languages like English, leave gaping holes in protection for African users" — meaning that in-language targeting of Hausa, Swahili, and Zulu audiences is structurally invisible to conventional monitoring. The targeted decisions being shaped in these unmonitored channels include electoral choices, labour relations, and community responses to foreign investment.[^1]

**Brazil/Latin America critical minerals (Global South parallel):** Alto's documentation of the Los Pelambres (Chile), Salar de Atacama (Chile), Cerrejón (Colombia), Las Bambas (Peru), and Bolivia lithium cases shows that the same APM infrastructure targeting African mining governance is operating across Latin American critical mineral supply chains — a fully Global South targeting picture that receives almost no attention in Anglophone security research.

**The BRICS information environment as a targeted arena:** South Africa's 2023 BRICS summit was accompanied by the SSA hack (timing possibly coincidental), intense narrative contestation over South Africa's "active neutrality" on Ukraine, and documented paid-influencer operations. The BRICS information environment is itself a targeted process — with multiple external actors seeking to shape what BRICS membership means for South Africa's foreign policy choices.[^28][^29][^17]

---

## References

1. [AI-Generated Propaganda Threatens African Democracy](https://democracyinafrica.org/ai-generated-propaganda-threatens-african-democracy/) - As generative artificial intelligence becomes increasingly accessible, African democracies face an u...

2. [When Democracy Gets Deepfaked As six African nations head to the ...](https://www.forus-international.org/en/news/when-democracy-gets-deepfaked-as-six-african-nations-head-to-the-polls-in-2027-ai-generated-disinformation-is-already-reshaping-the-electoral-battlefield) - With six African nations — Nigeria, Kenya, Angola, Gambia, Equatorial Guinea, and the Republic of th...

3. [4th EEAS Report on Foreign Information Manipulation ... - MediaWell](https://mediawell.ssrc.org/news-items/4th-eeas-report-on-foreign-information-manipulation-and-interference-threats/) - FIMI continues to adapt to technological advances, particularly in Artificial Intelligence (AI). AI-...

4. [A cloudy outlook? What we are learning about election ...](https://africacheck.org/fact-checks/blog/cloudy-outlook-what-we-are-learning-about-election-disinformation-africa-and-what) - As nearly a dozen countries prepare to hold presidential elections, the spread of disinformation is ...

5. [Disinformation war erupts in global mining - The Oregon Group](https://theoregongroup.com/investment-insights/disinformation-war-erupts-in-global-mining/) - Investment risk and cost of fake news. For mining investors and companies, the implications are star...

6. [Engaging the Community: Combating Transnational Repression in ...](https://freedomhouse.org/report/transnational-repression/canada/2025) - It became clear in early 2023, that Chiu was not the only target of the Chinese government. Kenton T...

7. [[PDF] Hearing on 'Transnational Repression: Trends and Policy Approaches'](https://humanrightscommission.house.gov/sites/evo-subsites/humanrightscommission.house.gov/files/evo-media-document/20250624_sikhcoalition_sfr.pdf) - institutions have been targeted by coordinated Indian disinformation campaigns that are aligned with...

8. [Transnational repression is a global problem. The intimidation ...](https://www.facebook.com/FBIHonolulu/posts/transnational-repression-is-a-global-problem-the-intimidation-harassment-and-at-/821420287703057/) - Transnational repression may take the following forms: Stalking Online disinformation campaigns Hara...

9. [Cambridge Analytica's role in African elections was real but overstated](https://qz.com/africa/1242223/cambridge-analytica-facebook-had-little-impact-on-kenya-nigeria-elections) - Election manipulation is a hot story. In the last few days, Cambridge Analytica, which claims to use...

10. [How the Nigerian and Kenyan media handled Cambridge Analytica](https://theconversation.com/how-the-nigerian-and-kenyan-media-handled-cambridge-analytica-128473) - Kenyan president Uhuru Kenyatta recently signed into law the Data Protection Bill. Passed after seve...

11. [The spectre of Cambridge Analytica still haunts African elections](https://www.aljazeera.com/opinions/2019/2/15/the-spectre-of-cambridge-analytica-still-haunts-african-elections) - Funding for social media advertising and manipulation could determine the outcome of Nigeria's Febru...

12. [Barrick resolves dispute with Mali government over Loulo-Gounkoto ...](https://www.reuters.com/sustainability/sustainable-finance-reporting/barrick-resolves-dispute-with-mali-government-over-loulo-gounkoto-mining-complex-2025-11-24/) - October 31, 2025: World Bank arbitration body rejects a request by Barrick to expedite its internati...

13. [Barrick Announces Resolution of its Disputes with Mali](https://www.barrick.com/English/news/news-details/2025/barrick-announces-resolution-of-its-disputes-with-mali/default.aspx) - All charges brought against Barrick, its affiliates and employees will be dropped and the legal step...

14. [China's Critical Minerals Strategy in Africa](https://africacenter.org/spotlight/china-africa-critical-minerals/) - African communities are responding with increasing sophistication—deploying local monitoring teams, ...

15. [Competing for Africa's Resources: How the US and China Invest in ...](https://www.stimson.org/2025/competing-for-africas-resources-how-the-us-and-china-invest-in-critical-minerals/) - This piece will examine the drivers, key projects, and funding methods between the US and China in A...

16. [South Africa Faces Escalating Cybersecurity Threats to Critical ...](https://ats.co.za/2025/01/28/cybersecurity-threats/) - The SSA warns that threats to South Africa's critical information infrastructure are likely to escal...

17. [South Africa Faces Increased Cyberattacks Against Government ...](https://adf-magazine.com/2025/02/south-africa-faces-increased-cyberattacks-against-government-agencies/) - Cyberattacks are also increasingly targeting the nation's critical infrastructure, including health ...

18. [Fake News, Election-Related Disinformation Laws, and Citizens ...](https://journals.co.za/doi/10.20940/JAE/2025/v24i1a1) - In some African countries, election misinformation on all major social media platforms is aimed at i...

19. [South Africa's government and military organisations face 3480 ...](https://www.intelligentcio.com/africa/2025/06/02/south-africas-government-and-military-organisations-face-3480-attacks-per-week/) - The recent cyberattack on SAA highlights the vulnerability of Government and para-governmental insti...

20. [South Africa's Public Sector Faces a Surge in Cyberattacks](https://stormwarning.co.za/index.php/cybersecurity-news/south-africas-public-sector-faces-a-surge-in-cyberattacks-the-role-of-stormwarning) - South Africa's public sector faced a surge in cyberattacks in 2024, highlighting the need for advanc...

21. [Cybersecurity in South Africa: rising attacks, weak defences, and ...](https://nationalsecuritynews.com/2025/09/cybersecurity-in-south-africa-rising-attacks-weak-defences-and-growing-urgency/) - Research by Kaspersky shows that in the first half of 2025 South Africa endured more than six millio...

22. [Africa's democracies must guard against local online ...](https://issafrica.org/iss-today/africa-s-democracies-must-guard-against-local-online-influencer-networks) - New research shows that key figures in South Africa’s domestic online influence industry are engaged...

23. [Under the influence? Online mis/disinformation in South Africa's May ...](https://issafrica.org/research/southern-africa-report/under-the-influence-online-mis-disinformation-in-south-africa-s-may-2024-election) - This report spotlights the tactics, narratives and actors who drive such campaigns and offers lesson...

24. [From South Africa to the US, white victimhood knows no borders](https://www.aljazeera.com/opinions/2025/3/24/from-south-africa-to-the-us-white-victimhood-knows-no-borders) - ... Afriforum, Ernst Roets. Afriforum is a right-wing South African NGO dedicated to advancing the i...

25. [U.S. and Foreign Governments Should Be Skeptical of AfriForum's ...](https://www.cfr.org/articles/us-and-foreign-governments-should-be-skeptical-afriforums-lobbying) - Tyler McBrien is a research associate for education at the Council on Foreign Relations. The land re...

26. [Propaganda Machine: Russia's information offensive in the Sahel](https://forbiddenstories.org/propaganda-machine-russias-information-offensive-in-the-sahel/) - In the Sahel and the Central African Republic, Moscow's disinformation agents spare no expense in ma...

27. [The 'ghost reporters' writing pro-Russian propaganda in West Africa](https://www.aljazeera.com/features/2025/3/20/the-ghost-reporters-writing-pro-russian-propaganda-in-west-africa) - Disinformation researcher Nina Jankowicz said she was “quite surprised they chose someone who has di...

28. [BRICS Summit 2025: will slow and steady actually win the race?](https://issafrica.org/iss-today/brics-summit-2025-will-slow-and-steady-actually-win-the-race) - Dr Samir Puri, Chatham House's Centre for Global Governance and Security Director, says: 'BRICS has ...

29. [BRICS: BRICS 2025 - Friedrich-Naumann-Stiftung](https://www.freiheit.org/brics-what-are-key-issues-2025) - ... security, development and human rights policy. Global Security Hub · EN · DE · Global World Orde...

