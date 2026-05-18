---
layout: default
---

## Incident Summary

**Title:** Transnet ransomware attack and force-majeure disruption of South African ports  
**Date:** 22 July 2021  
**Targets:** Transnet SOC Ltd; container terminals at Durban, Cape Town, Port Elizabeth and Ngqura; South African and regional supply chains for mining, agricultural and manufactured exports  
**Continent:** Africa  
**Perpetrator:** Threat actor deploying ransomware linked by CrowdStrike to the "Death Kitty" / "HelloKitty" / "Five Hands" family, assessed by researchers to originate in Russia or Eastern Europe  
**Motivation:** Financial extortion through encryption and threatened publication of stolen data, against a high-value state-owned operator of critical maritime and rail infrastructure  

## Cyberattack Details

- **Nature:** Network intrusion, file encryption, and double-extortion ransomware deployment with a 1TB exfiltration claim
- **Systems Attacked:** Transnet's IT environment, including the Navis container operating system used at port terminals; corporate, port, rail, pipeline and engineering systems were variously affected
- **Data Held:** Ransom note claimed exfiltration of approximately 1TB of personal data, financial reports and other internal documents
- **Availability Impact:** Severe — Transnet declared force majeure across container terminals and switched to a paper-based manual clearance process; Port of Durban was reported operating at 10% capacity at the height of the disruption, with truck turnaround times exceeding 14 hours
- **Data Exfiltration/Alteration:** Attackers claimed encryption of files and exfiltration of 1TB; Transnet later stated no raw customer data had been compromised
- **Estimated Impact:** Disruption of more than 60% of South Africa's container traffic for over a week; regional knock-on effects for landlocked neighbours and for SA's mining and agricultural exports; force-majeure declaration limiting Transnet's contractual liability
- **Investigators:** Transnet incident-response team, South African government (Department of Public Enterprises), CrowdStrike (attribution analysis), Bloomberg and ISS Africa reporting
- **Remediation:** No ransom paid; Active Directory rebuild, Microsoft E5 stack deployment fast-tracked, OS upgrades and patching, deployment of WAF / reverse-proxy / anti-DDoS infrastructure for public sites; ~90% of IT systems restored within two weeks

## Disinformation Details

- **Nature:** Coercive leak-site / ransom-note extortion rather than ideological influence operation
- **Narratives:** Pay or stolen records will be released; the company's critical infrastructure cannot be defended without negotiation
- **Deception:** Use of dark-web negotiation portal, ambiguity around volume and sensitivity of exfiltrated data, and reliance on operational fear (force-majeure conditions) to pressure payment
- **Platforms:** Ransom note on victim systems, dark-web negotiation portal, downstream press coverage
- **Reach:** National and international through extensive South African and global press coverage of the force-majeure event
- **Impact:** Even without payment, the public disruption to a flagship state-owned enterprise had reputational and political fallout; the attack came days after the 2021 KwaZulu-Natal unrest, fuelling unverified public speculation of coordinated economic destabilisation (authorities concluded the two events were unrelated)
- **Disinfo Investigators:** Public-sector spokespersons, journalists at Bloomberg / Reuters / Daily Maverick / TechCentral, and ISS Africa analysts
- **Remediation:** Public attribution analysis by CrowdStrike; government communications; ongoing parliamentary and regulatory scrutiny
- **Link to Cyberattack:** The coercive pressure depended entirely on the encryption of operational systems and the threat of releasing exfiltrated data

## References

[1](https://en.wikipedia.org/wiki/Transnet_ransomware_attack): *Wikipedia*, "Transnet Ransomware Attack"  
[2](https://www.bloomberg.com/news/articles/2021-07-29/-death-kitty-ransomware-linked-to-attack-on-south-african-ports): *Bloomberg*, "Death Kitty Ransomware Linked To Attack On South African Ports"  
[3](https://issafrica.org/iss-today/cyber-attacks-expose-the-vulnerability-of-south-africas-ports): *ISS Africa*, "Cyber Attacks Expose The Vulnerability Of South Africa's Ports"  
[4](https://www.scielo.org.za/scielo.php?pid=S2077-72132023000200004&script=sci_arttext): *SciELO South Africa*, "The Centrality Of Cybersecurity To Socioeconomic Development Policy: A Case Study Of Transnet"  
[5](https://resilientmaritimelogistics.unctad.org/guidebook/case-study-17-port-durban-south-africa): *UNCTAD*, "Case Study 17: Port Of Durban, South Africa"  
