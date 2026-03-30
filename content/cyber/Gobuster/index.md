---
title: Gobuster
updated: 2024-02-13 05:51:28Z
created: 2024-02-13 05:51:18Z
---

# Gobuster
List all the "path"/"directory"/subdomains under a website.
Gobuster is written in [Go](https://go.dev/)
Installation: `sudo apt install gobuster`

Useful flags: [More Here](https://github.com/OJ/gobuster#dir-mode-options)
![Screenshot 2023-08-03 at 2.21.34 AM.png](1.png)

Subdomanins:
![Screenshot 2023-08-03 at 2.30.58 AM.png](2.png)

Listing: `gobuster dir`
Example command 1 (files and directory): `gobuster dir -u http://10.10.10.10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`
Example command 2 (files and directory with restriction): `gobuster dir -u http://10.10.252.123/myfolder -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x.html,.css,.js`

Subdomains: `gobuster dns` , check subdomains against DNS
Example command: `gobuster dns -d mydomain.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt`

subdomains: brute-force virtual hosts: `gobuster vhost`, check subdomains against hosts (usually identifying the hidden subdomains)
Example command: `gobuster vhost -u http://example.com -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt`
* If this is the subdomain of other top domains