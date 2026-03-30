---
title: _Terms & Methodology
updated: 2024-02-13 06:18:34Z
created: 2023-04-05 05:31:36Z
---

# General Terms

**Rule of Engagement**: **rules to follow** before an engagement:
	- Permission: both party sign a document for clear permission for the intended actions.
	- Test Scope: defines what target and environment are being tested against
	- Rules: defines the type of behaviour a penetration tester will employ

**Methodology**: The **steps** to take **during an engagement**. A good methodology would be the step taken are relevant to the current situation

**OSSTMM** - [The Open Source Security Testing Methodology Manual](https://www.isecom.org/OSSTMM.3.pdf): provides a detail framework of testing strategy in a various of aspects. specialized in **telecommunications**, **wired networks**, **wireless communications**

**[OWASP](https://owasp.org/)**: community draven framework specialized in **web application services**.

**[NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)**: provides a framework that improve organizations **cyber security standards** and manage the risk of cyber threats.

**NCSC CAF** - [Cyber Assessment Framework](https://www.ncsc.gov.uk/collection/caf/caf-principles-and-guidance): extensive framework of 14 principles, assess the risk of cyber threats and organization's defence against these principles.

**Entropy**: The measure of randomness of data in a file.

**Cookies**: They are key-value pairs that a web application will store on the user's browser and that will be automatically repeated on each request to the website that issued them. Note that the cookies are saved on the users browser, hence they are easily modifiable. **JSON Web Tokens (JWT)** can prevent cookies from tampering (signature and key system). (Note that JWT used to have none algorithm vulnerability)

---

# Encoding Terms

**URL Encoding**: make data (special symbol) safe to transfer in the URL of a web request. usually hex preceded + % symbol e.i. `/` -> `%2f` 

**HTML**: make data (special symbol) safe to render in the HTML pages. Usually `&` + a hex or a dedicated character + `;`

**base64**: encode any data in an ASCII-compatible format. designed to take binary data (e.g. images, media, programs) [more can be read here](https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/)

**ASCII HEX**: converts data between ASCII representation and hexadecimal representation

**Gzip**: provide a way to compress data, widely used to reduce the size

---

# Network Security - Methodology

**Recon**: information gathering

**Weaponization**: prepare the tools and script to gain access

**Delivery**: send the malicious script

**Exploitation**: when the malicious file runs on the target system (try to break in and gain access)

**Installation**: Install the access methods, such as back door, for the remote user

**Command & Control**: the fun begins, the remote user can do anything they wants

**Action on Objectives**: achieve their objective
