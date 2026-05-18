---
layout: default
---

## Incident Summary

**Title:** Cell C RansomHouse double-extortion and customer-data leak  
**Date:** Late 2024 (intrusion detected 20 December 2024; ransom demand 11 April 2024 per researchers; data published on dark web 28 December 2024; public confirmation by Cell C 8 January 2025; further confirmation of leak 9 April 2025)  
**Targets:** Cell C, the third-largest mobile operator in South Africa, and approximately 7.7 million subscribers along with employees, partners and a former senior executive  
**Continent:** Africa  
**Perpetrator:** RansomHouse data-extortion group (active since late 2021 / early 2022; previous victims include AMD, Keralty, and South African retailer Shoprite)  
**Motivation:** Financial extortion through threatened publication of stolen customer and corporate data, exploiting Cell C's role as a major SA telecoms provider holding rich identity and financial data  

## Cyberattack Details

- **Nature:** Multi-pronged data-extortion intrusion typical of RansomHouse — exfiltration-focused with no widespread encryption; reportedly preceded by phishing campaigns in 2023 according to researchers (disputed by Cell C)
- **Systems Attacked:** Unstructured-data repositories within Cell C's corporate IT environment; researcher analysis of leaked credentials suggested possible exposure of FTTH ordering, provisioning and billing portals linked to fibre operators (MetroFibre, Openserve, Vumatel)
- **Data Held:** Full names, contact details, email addresses, phone numbers, ID numbers, banking information, driver's licence numbers, medical records, passport details, and personal records of a former senior executive
- **Availability Impact:** Limited — Cell C network services and billing systems remained operational; the impact was predominantly on data confidentiality and corporate reputation
- **Data Exfiltration/Alteration:** Approximately 2TB of data exfiltrated and subsequently published on RansomHouse's dark-web leak site after Cell C did not engage with the ransom demand
- **Estimated Impact:** Significant identity-theft, SIM-swap and phishing risk for millions of Cell C subscribers; regulatory engagement with the South African Information Regulator; reputational damage during a sensitive period of corporate restructuring
- **Investigators:** Cell C's external cybersecurity advisers, threat-intelligence firm TFI (which mapped leaked data and exfiltration timeline), SentinelOne analysis of RansomHouse tradecraft, Information Regulator and SAPS
- **Remediation:** Containment and isolation of affected systems; engagement of external cybersecurity experts; public information-hub launched to advise stakeholders on protective registration via SAFPS; no ransom paid

## Disinformation Details

- **Nature:** Coercive leak-site doxing campaign — RansomHouse markets itself publicly as a "force for good" exposing corporate security failings, a posture designed to add reputational pressure beyond conventional ransom demands
- **Narratives:** Cell C cannot protect customer data; the company concealed the incident's true scope; releasing data is "ethical disclosure" rather than crime
- **Deception:** Selective publication of records on the leak site; messaging framing exfiltration as a public-interest act; partial disclosure designed to maximise media uptake
- **Platforms:** RansomHouse dark-web leak site; downstream coverage by Connecting Africa, TechCentral, BleepingComputer, Security Affairs and The Record
- **Reach:** National (SA mass-market subscribers) and international (telecoms sector and threat-intelligence community)
- **Impact:** Sustained negative press coverage during a delicate period for Cell C's corporate finances; renewed attention to ransomware risks in African telecoms; consumer alarm despite Cell C's assertion that core billing and authentication systems were not breached
- **Disinfo Investigators:** TFI, SentinelOne, FalconFeeds.io, Connecting Africa, TechCentral and other sector press
- **Remediation:** Public statements correcting RansomHouse's narrative framing; investor and regulator communications; information-hub for affected stakeholders
- **Link to Cyberattack:** The reputational pressure depended entirely on the exfiltrated data; the influence component is wholly cyber-enabled

## References

[1](https://therecord.media/south-african-telecom-provider-discloses-data-breach-ransomware): *The Record (Recorded Future News)*, "South African Telecom Provider Serving 7.7 Million Confirms Data Leak Following Cyberattack"  
[2](https://securityaffairs.com/176509/data-breach/south-african-telecom-provider-cell-c-disclosed-a-data-breach.html): *Security Affairs*, "South African Telecom Provider Cell C Disclosed A Data Breach"  
[3](https://techcentral.co.za/cell-c-was-hit-by-ransomware-gang/257477/): *TechCentral*  
[4](https://www.connectingafrica.com/cybersecurity/cell-c-confirms-customer-data-leak-by-ransomhouse): *Connecting Africa*, "Cell C Confirms Customer Data Leak By RansomHouse"  
[5](https://worldofcellc.co.za/information-hub): *Cell C Investor Relations*, "Cell C Information Hub: Cybersecurity Incident"  
