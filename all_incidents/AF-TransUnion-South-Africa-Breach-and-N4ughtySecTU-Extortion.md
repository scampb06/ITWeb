---
layout: default
---

## Incident Summary

**Title:** TransUnion South Africa breach and N4ughtySecTU "insurance fee" extortion campaign  
**Date:** March 2022 (with renewed extortion demands in November 2023 and further claims in 2024)  
**Targets:** TransUnion South Africa, its corporate clients (Absa, FNB, Standard Bank, Nedbank, Discovery, TymeBank and others), and millions of South African consumers whose credit data was hosted on the breached server  
**Continent:** Africa  
**Perpetrator:** N4ughtySecTU (later N4ughtySecGroup), a self-identified Brazilian extortion crew  
**Motivation:** Financial extortion of TransUnion through ransom demand, plus secondary extortion of TransUnion's downstream corporate clients via threatened release of their customer records  

## Cyberattack Details

- **Nature:** Brute-force attack against an internet-facing SFTP server using stolen / weak client credentials reportedly protected by the password "Password", leading to bulk data exfiltration; no ransomware encryption
- **Systems Attacked:** A TransUnion South Africa server holding credit-bureau data, accessed via a compromised authorised-client account
- **Data Held:** Names, ID numbers, dates of birth, gender, contact details, marital status, financial and credit-related records; attackers claimed access to records of 54 million individuals and approximately 200 corporate clients
- **Availability Impact:** Limited — TransUnion took some services offline as a precaution but credit-bureau core operations resumed within days
- **Data Exfiltration/Alteration:** Up to 4TB of records claimed by the attackers; TransUnion later confirmed at least 3 million South African consumers were directly impacted, with approximately 6 million additional ID numbers identified
- **Estimated Impact:** Loss of sensitive credit-history data for millions of South Africans; secondary exposure of customer datasets used by major SA banks; substantial regulatory and reputational fallout; renewed extortion of $30M each from TransUnion and Experian in November 2023
- **Investigators:** TransUnion incident-response team, external cybersecurity / digital-forensic experts, South African Information Regulator and law enforcement
- **Remediation:** TransUnion publicly refused to pay; free identity-protection products offered to affected consumers; access by the compromised client was suspended

## Disinformation Details

- **Nature:** Double-extortion-style coercion combined with a novel "insurance fee" campaign — TransUnion's corporate clients were approached separately and asked to pay smaller "insurance" sums (~$1M for large clients, $100K for smaller ones) to be excluded from any future leak
- **Narratives:** TransUnion's data is in the attackers' hands; downstream institutions cannot protect their customers' records; payment is the only protection
- **Deception:** Claims of continued persistent access through 2023 and 2024 (disputed by TransUnion and Experian), use of multiple Telegram and Session channels for negotiation, and weaponised lists of allegedly affected client institutions
- **Platforms:** ITWeb / MyBroadband / TimesLive / DataBreaches.net press coverage; Telegram and Session for direct contact with victims
- **Reach:** National (every adult South African with a credit record is plausibly affected) and international through credit-bureau interconnections
- **Impact:** Sustained reputational pressure on TransUnion, Experian and the South African financial-services sector; public anxiety driven by claims of ongoing access; political pressure on the Information Regulator
- **Disinfo Investigators:** MyBroadband, ITWeb, BleepingComputer, BitDefender, Stellenbosch University researchers Joel Cedras and Veer Gosai (separate but related SASSA-fraud disclosures)
- **Remediation:** Public refusal to pay; ongoing Information Regulator engagement; consumer protective-registration services via SAFPS
- **Link to Cyberattack:** The "insurance fee" influence layer depended directly on the original intrusion and on credible claims of held data

## References

[1](https://www.bleepingcomputer.com/news/security/hackers-claim-to-breach-transunion-south-africa-with-password-password/): *BleepingComputer*, "Hackers Claim To Breach TransUnion South Africa With "Password" Password"  
[2](https://www.securityweek.com/transunion-confirms-data-breach-south-africa-business/): *SecurityWeek*, "TransUnion Confirms Data Breach At South Africa Business"  
[3](https://www.databreaches.net/transunion-hackers-demand-r224-million-ransom-threaten-to-leak-absa-fnb-standard-bank-data/): *DataBreaches.net*, "TransUnion Hackers Demand R224-Million Ransom — Threaten To Leak Absa, FNB, Standard Bank Data"  
[4](https://cyberscoop.com/south-africa-transunion-data-breach/): *CyberScoop*, "South Africa Credit Bureau Breached, Data Reportedly Held For $15M Ransom"  
[5](https://dailyinvestor.com/technology/68250/hackers-claim-to-have-access-to-south-african-citizens-financial-data/): *Daily Investor*, "Hackers Claim They Have Access To South African Citizens' Financial Data"  
[6](https://www.security.org/identity-theft/breach/transunion/): *Security.org*, "TransUnion Data Breach: What Happened And How To Protect Yourself"  
