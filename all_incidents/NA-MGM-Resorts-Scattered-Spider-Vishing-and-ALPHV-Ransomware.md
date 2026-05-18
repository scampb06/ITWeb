---
layout: default
---

## Incident Summary

**Title:** MGM Resorts Scattered Spider vishing and ALPHV ransomware attack  
**Date:** Initial intrusion 7-8 September 2023; public disclosure 11 September 2023; ransomware deployment 11-17 September 2023  
**Targets:** MGM Resorts International and its more than 30 properties globally, including the MGM Grand, Bellagio, Aria and Cosmopolitan in Las Vegas; subsequent customer-data disclosure affected MGM customers who had used MGM services before March 2019; Caesars Entertainment was hit by the same actors approximately one week earlier  
**Continent:** North America  
**Perpetrator:** Scattered Spider (tracked as UNC3944, a financially motivated English-speaking group with members in the US and UK known for advanced social-engineering) operating as an affiliate of the ALPHV / BlackCat ransomware-as-a-service operation  
**Motivation:** Financial extortion through ransomware-as-a-service, exploiting MGM's high revenue, public profile, and reliance on networked operational systems including slot machines, digital room keys and reservations  

## Cyberattack Details

- **Nature:** Voice-phishing (vishing) of the IT help desk, abuse of identity-and-access management (Okta) for privilege escalation, lateral movement, and finally ALPHV / BlackCat ransomware deployment
- **Systems Attacked:** MGM corporate IT, Okta single-sign-on infrastructure, internal networks, slot-machine networks, digital room-key systems, online reservation systems, email and mobile-services infrastructure
- **Data Held:** Personal customer contact details and government-ID information for customers who had used MGM services before March 2019
- **Availability Impact:** Severe — widespread outages across MGM's Las Vegas properties; ATMs, slot machines, digital room keys, electronic payment systems, TV services and phone lines were affected; staff fell back to pen-and-paper processing for days
- **Data Exfiltration/Alteration:** Customer PII exfiltrated; ALPHV operators threatened to notify HaveIBeenPwned if negotiations failed
- **Estimated Impact:** Approximately US$100 million in lost revenue plus legal, consulting and remediation costs; daily revenue loss of approximately US$8.4 million during the outage; multiple class-action lawsuits; long-term reputational damage; Caesars Entertainment, hit by the same actors a week earlier, reportedly paid an undisclosed ransom (estimated $15M)
- **Investigators:** MGM internal security and IR teams, Mandiant and other external responders, FBI, the vx-underground research community which obtained early threat-actor statements, Okta (which confirmed five clients including MGM were affected)
- **Remediation:** MGM refused to pay the ransom; phased system restoration; significant overhaul of help-desk authentication processes; class-action settlements; industry-wide reassessment of help-desk verification across the hospitality and casino sectors

## Disinformation Details

- **Nature:** Pretext-based social-engineering / impersonation — the influence component was the convincing identity-claim made to the help desk
- **Narratives:** "I am an MGM employee and I need a credential reset"; subsequent ALPHV public statements positioning themselves as professional and ethical operators, including a public "Setting the record straight" statement
- **Deception:** (1) LinkedIn-based reconnaissance to identify a target employee; (2) vishing the IT help desk while impersonating that employee, leveraging English fluency to overcome cultural defences typical of Eastern-European-aligned ransomware actors; (3) ALPHV public statements designed to manage media narrative and pressure MGM into negotiation
- **Platforms:** Telephone (vishing), LinkedIn (reconnaissance), ALPHV public statement on the group's dark-web leak site, vx-underground's social-media platform, mainstream press coverage
- **Reach:** Global business and cybersecurity press; case-study status across the industry
- **Impact:** Catalysed industry-wide rethinking of help-desk authentication; established Scattered Spider as a leading social-engineering threat; demonstrated that vishing of a single employee can defeat enterprise-grade technical controls including MFA and Okta
- **Disinfo Investigators:** vx-underground, BleepingComputer, Krebs on Security, Netwrix, Specops, Cymulate, Reuters, NBC and major financial press
- **Remediation:** MGM internal reforms; sector-wide help-desk authentication hardening; FBI advisories and CISA alerts on Scattered Spider TTPs
- **Link to Cyberattack:** The entire initial-access vector was a social-engineering / impersonation operation — the influence component made the cyber operation possible

## References

[1](https://netwrix.com/en/resources/blog/mgm-cyber-attack/): *Netwrix*, "An Overview Of The MGM Cyber Attack"  
[2](https://zcybersecurity.com/mgm-resorts-data-breach-faq-what-happened-who-was-affected-what-was-the-impact/): *Z Cybersecurity*, "MGM Resorts Data Breach FAQ: What Happened, Who Was Affected, And The Impact"  
[3](https://specopssoft.com/blog/mgm-resorts-service-desk-hack/): *Specops Software*, "MGM Resorts Hack: How Attackers Hit The Jackpot With Service-Desk Social Engineering"  
[4](https://www.cshub.com/attacks/news/a-full-timeline-of-the-mgm-resorts-cyber-attack): *Cyber Security Hub*, "A Full Timeline Of The MGM Resorts Cyber Attack"  
[5](https://cymulate.com/blog/a-grand-attack-on-the-palace/): *Cymulate*, "MGM Resorts And Caesars Palace Cyber Attacks Explained"  
[6](https://westoahu.hawaii.edu/cyber/global-weekly-exec-summary/alphv-hackers-reveal-details-of-mgm-cyber-attack/): *University of Hawaiʻi - West Oʻahu*, "ALPHV: Hackers Reveal Details Of MGM Cyber Attack"  
