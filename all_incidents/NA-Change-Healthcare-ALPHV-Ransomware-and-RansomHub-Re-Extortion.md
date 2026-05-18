---
layout: default
---

## Incident Summary

**Title:** Change Healthcare ALPHV / BlackCat ransomware, exit-scam and RansomHub re-extortion  
**Date:** Initial intrusion 11-12 February 2024; nine-day lateral movement; ransomware deployed 21 February 2024; US$22 million ransom paid early March 2024; ALPHV exit-scam and RansomHub re-extortion through April-May 2024  
**Targets:** Change Healthcare (a UnitedHealth Group subsidiary processing approximately half of all US medical claims for around 900,000 physicians, 33,000 pharmacies, 5,500 hospitals and 600 laboratories); ultimately compromised the personal, health, and financial information of approximately 100 million Americans  
**Continent:** North America  
**Perpetrator:** ALPHV / BlackCat ransomware-as-a-service operation; an affiliate of the group performed the actual intrusion and then was reportedly cheated by ALPHV's "exit scam"; the affiliate subsequently took the stolen data to a second ransomware group, RansomHub, for further extortion  
**Motivation:** Financial extortion through ransomware, with double-extortion mechanics; opportunistic targeting of a high-value healthcare-data processor with critical national role  

## Cyberattack Details

- **Nature:** Credential-based intrusion into an unprotected Citrix remote-access portal lacking multi-factor authentication, followed by nine days of lateral movement, then ALPHV / BlackCat ransomware deployment; further compounded by post-payment RansomHub re-extortion
- **Systems Attacked:** Change Healthcare's nationwide medical-claims, billing and prescription-processing systems, plus broader UnitedHealth Group infrastructure (UnitedHealth severed connectivity to Change's data center to prevent malware spread to wider corporate systems)
- **Data Held:** Personal, health, and financial information of approximately 100 million individuals — names, contact details, Social Security numbers, driver's licence numbers, health information, insurance information, billing information, patient diagnoses, treatment information and health-insurance member IDs
- **Availability Impact:** Severe — weeks-long disruption of pharmacy operations, medical-claims processing, billing and prescription services across the US; patients forced to pay out-of-pocket for medications; thousands of physician practices, pharmacies and small healthcare providers faced cash-flow crises
- **Data Exfiltration/Alteration:** Approximately 6TB of data exfiltrated and held first by the ALPHV affiliate, then by RansomHub after the affiliate moved to that group following the exit-scam
- **Estimated Impact:** Largest healthcare data breach in US history; approximately US$2.87 billion in response costs incurred by UnitedHealth Group in 2024; over US$6 billion in financial assistance provided to affected healthcare providers; US$22 million ransom paid to ALPHV; second extortion demand from RansomHub (not paid); major reputational and political consequences, including testimony from UnitedHealth CEO Andrew Witty before Congress on 1 May 2024 confirming the ransom payment
- **Investigators:** Mandiant (incident response), FBI, CISA, US Department of Health and Human Services Office for Civil Rights (HIPAA breach investigation); subsequent state-level investigations including Nebraska Attorney-General lawsuit
- **Remediation:** US$22 million ransom paid by UnitedHealth Group to ALPHV with the goal of preventing data publication; ALPHV exit-scammed its affiliate, who retained the data; affiliate took stolen data to RansomHub which made a second extortion demand (not paid); UnitedHealth provided large-scale provider financial assistance; congressional hearings; multi-state class-action and AG litigation; HHS-OCR HIPAA enforcement

## Disinformation Details

- **Nature:** Multi-layered extortion-and-coercion campaign with substantial reputational and public-narrative dimensions; the ALPHV exit-scam and RansomHub re-extortion produced an unusually public threat-actor-versus-threat-actor disinformation episode
- **Narratives:** (1) ALPHV's pay-or-publish coercion against UnitedHealth; (2) ALPHV's post-payment public statement and shutdown narrative designed to disguise an exit-scam against its own affiliate; (3) RansomHub's framing of itself as legitimate inheritor of the stolen data and as authorised re-extortionist; (4) public-narrative pressure on UnitedHealth via congressional and media accountability for the payment decision
- **Deception:** ALPHV's fake "law enforcement seizure" claims on its own leak site, designed to convince its affiliate community that the operation had been disrupted and to hide the exit-scam; RansomHub's claim of legitimate authority to extort with the stolen data
- **Platforms:** ALPHV and RansomHub dark-web leak sites, US Department of Justice / FBI public statements, congressional testimony (Senate Finance Committee and House Energy and Commerce subcommittee), mainstream press coverage (Krebs on Security, IBM, BlackFog, HIPAA Journal)
- **Reach:** Massive — directly affected approximately 100 million Americans and a substantial portion of the US healthcare-payment system; saturated US news coverage for months
- **Impact:** Public discrediting of ransomware-payment-as-protection model; explicit congressional testimony admitting the futility of the payment ("did not get its data back"); broader policy debate about banning ransom payments; ALPHV ceased operations, RansomHub emerged as a major new player partly absorbing ALPHV affiliates
- **Disinfo Investigators:** Krebs on Security, IBM Security, BlackFog, HIPAA Journal, Holland & Knight legal analysis, Aviatrix, Hyperproof, congressional staff and law-enforcement; Nebraska AG litigation discovery
- **Remediation:** Public disclosure by UnitedHealth CEO; congressional accountability; HHS-OCR HIPAA enforcement; broader US healthcare-sector security reforms
- **Link to Cyberattack:** Every influence and coercion element depended on the underlying intrusion and exfiltration; this incident is a particularly stark example of how ransomware extortion campaigns are simultaneously cyber attacks and influence operations

## References

[1](https://krebsonsecurity.com/2024/03/blackcat-ransomware-group-implodes-after-apparent-22m-ransom-payment-by-change-healthcare/): *Krebs on Security*, "BlackCat Ransomware Group Implodes After Apparent $22M Payment By Change Healthcare"  
[2](https://www.ibm.com/think/news/change-healthcare-22-million-ransomware-payment): *IBM Think*, "Change Healthcare Discloses $22M Ransomware Payment"  
[3](https://www.hklaw.com/en/insights/publications/2024/06/change-healthcare-cybersecurity-incident-financial-impact): *Holland & Knight*, "Change Healthcare Cybersecurity Incident: Financial Impact And Resulting Litigation"  
[4](https://www.hipaajournal.com/change-healthcare-responding-to-cyberattack/): *HIPAA Journal*, "Nebraska AG's Lawsuit Against Change Healthcare Survives Motion To Dismiss"  
[5](https://www.blackfog.com/change-healthcare-landmark-cybersecurity-breach/): *BlackFog*, "The Change Healthcare Ransomware Attack: A Landmark Cybersecurity Breach"  
[6](https://aviatrix.ai/threat-research-center/what-ransom-note-doesnt-say-change-healthcare-2024/): *Aviatrix Threat Research Center*, "What The Ransom Note Doesn't Say: Change Healthcare 2024"  
