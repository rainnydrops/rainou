---
title: Team Blue
updated: 2024-02-13 06:15:14Z
created: 2023-03-05 23:48:58Z
latitude: 43.65322600
longitude: -79.38318430
altitude: 0.0000
---

# Defender 

## Digital Forensics

- every ducument has their meta data 
	- pdf meta data: pdfinfo
	- photo EXIF meta data: exiftool tool


## SOC

- Find vulnerability on the network
- Detected unauthorized activity
- Discover policy violation
- Detect intrusions
- Support with the incident response

## Terms

Defence in Depth: use of multiple various layer to provide a security redundancy in an organization's security parameter 

## Security Model
The CIA:
- confidentiality
- integrity
- availability
Other model
- The Bell-La Padula Model: no write down (but can read down), no read up
	- used in military and require a large amount of trust
- The Biba Model: no write up, no read down: can create/write **object** below their level, and can only read **object** above their level
	- used when integrity > confidentiality

## Threat Modelling & Incident response
- The process of reviewing improving and testing the security protocols
- Critical stage: identifying likely threats
- Breach of security are called **incident**, actions taken to resolve the incident are called **Incident Response (IR)**
- IR are dealed by a computer security incident response team (CSIRT)
- **Threat modelling** is similar to a risk assessment, but the principles all turn to:
	- preparation
	- identification
	- migrations
	- review
	- other complex process that require dedicate teams
		- threat intelligence
		- asset identification
		- mitigation capabilities
		- risk assessment
- There are framework to help with these threat:
	- **STRIDE**: identify thread
		- spoofing: use of false identify
		- tampering: false integrity
		- repudiation: logging of activity
		- information disclosure: information are viewable to non-permitted personel
		- denial of service: abuse of the service to bring down the system
		- elevation of privilege: escalate their authorization
	- **PASTA**: incident response steps
		- preparation: prepare resources and plan to deal with incidents
		- identification: identify thread actor
		- containment: contained the thread to prevent other system from getting infected
		- eradication: remove the active threat
		- recovery: return the impacted business as usual operation
		- lesson learned: what to learn from incident