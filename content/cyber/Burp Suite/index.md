---
title: Burp Suite
updated: 2024-02-13 05:51:41Z
created: 2023-05-03 20:52:29Z
---

# Burp Suite

### General
**Macro**: an automated action performed by burp before each of the request send via HTTP.

Onestopshop framework for web application penetration testing. can also be used for mobile application due API that also powered the mobile apps. [More](https://tryhackme.com/room/burpsuitebasics)
[Download Page](https://portswigger.net/burp/releases/professional-community-2023-3-5?requestededition=community&requestedplatform=)

Allows extensions written in Java, Python ot Ruby. **Burp Suite Extender module** allows easily load extensions into the framework and places to download download **third-party modules**. Most requires professional version, but some can be integrated with community e.g. Logger++ module.

**Burp Suite professional**: unrestricted version of Burp Suite Community
**Burp Suite Enterprise**: used for continuous scanning by the large coorporation.
**Burp Suite Community**: free and contain essential tools.

**Burp Suite Community Features:**

- **Proxy**: allows us to intercept and modify requests/responses
- **Repeater**: capture, modify, then resend the same request numerous times (SQLi)
- **Intruder**: spray an endpoint with requests (brute force)
- **Decoder**: transforming data
- **Comparer**: compare two pieces of data at either word or byte level
- **Sequencer**: assessing the randomness of tokens such as session cookie values
	
	
## Proxy
- **FoxyProxy**: Firefox extension that allowed to save the proxy setting. Standard version gives more control over what traffic gets sent through the proxy.
- Burp proxy works by opening a web interface on `127.0.0.1:8080`
- Configure the proxy to send the request to `127.0.0.1:8080` (where burp suite can control the flow of the request)
- If visiting a **site with site with TLS enabled**. Solution: manually add the burp CA certificate ([Portswigger Certificate Authority](http://burp/cert)) to the list of trusted certificate authorities in Firefox browser.
- **the chromium browser that comes with burp cannot be run with root user**; alternative is to allow it to run without sandbox. (the latter option can cause a huge security concern; if the brower is hacked, the whole machine will be hacked)
- remember to use scope and targeting to filter the traffic needed: after enabling `And URL Is in target scope` in the proxy option to only capture the scoped traffic.

## Repeater
Take a request captured in the proxy and edit it, and send the same request with desired time. The time to send the request is based on user and **user will get the http requests' response in detail with the ability to edit both send request and received request**.
- Query Parameters: data
- Body Parameters: same thing as query parameter, but for the post request
- request cookies: cookies
- Request Headers: header of the request
- Response Headers: headers that the server sent back

## Intruder
Take a request as a template, automating request using it. **user send this http request in bulk with different input to achieve certain thing**
Useful when fuzzing or bruteforcing
To use the full speed of intruder requires Burp professional
- in-build fuzzing tool
- Community version of Burp Suite has a speed limitation (rate limited), it requires pro version to unlock full limitation
- Target: configure the target address
- Position: select attack type and insert payload to template. 
- Payloads: select the value to fill. This is highlighted in `§` symbol
- Resource Pool: divide resources between tasks (not so useful in Burp community)
- Options (settings): configure the attack behaviour

### Attack types
- **Sniper**: one set of payload (one single file list), try each of the word in the list for a single spot. Good for single-position attack
- **Battering** ram: one set of payload, try each of the word in the list for all the spot.
- **Pitchfork**: uses one payload set per position and iterate all at once
- **Cluster bomb**: allow multiple set of payload, it will try each and every combination of values between each of the payload. (try every possibilities between lists) A X B (matrix persceptive)

## Other modules

### Decoder
Work with encoded text

### Comparer
compare sets of text

### Sequencer
analyse the randomness of captured tokens. Allow the measure of **entropy** (malware contexts/token, they are mostly random because they need to hide the malware content) or analyse the randomness of a session cookie, etc.
**Live capture**: given a post request to the sequencer section, sequencer will send this request a thousands time to get the cookie sample to analyse
**manual load**: load manua samples

### Organizer
Store and annotate copies of HTTP requests that you may want to revisit later

### Extension
To integrate python, a separate Jython interpreter JAR archive file in needed (Jython is a Java implementation of Python)
[Jython standalone version](https://www.jython.org/download)

[PortSwigger](https://portswigger.net/burp/extender/writing-your-first-burp-suite-extension) is a reference for coding extensions for Burp Suite

