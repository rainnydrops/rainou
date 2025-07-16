---
title: "Cryptography Introduction"
date: 2025-01-11
draft: false
---

# Cryptography

# Hash
Hash: An one way encryption, usually used for integrity purpose

## Hash cracker
Available hash cracker
- [Online hash cracker](https://crackstation.net/)
- [Online hash cracker (Recommend)](https://hashes.com/en/decrypt/hash)

## Recognize different Hash
- Hash recognition [tool](https://pypi.org/project/hashID/) do exist, but they are unreliable for many format
- Use [this website](https://hashcat.net/wiki/doku.php?id=example_hashes) to distinguish different hash characteristic for example hashes, good for hash that have a prefix
- Hashes usually have some sort of prefix:
![Prefixes](../../_resources/Screenshot%202024-01-13%20at%2010.13.12 PM.png){width=75%}
- Tools like Hashcat and John the Ripper turns the string into hash and do the compareson
### Hash type Identifier
- [Online tool - Hashes (recommended)](https://hashes.com/en/tools/hash_identifier)
- [Online tool 2 - md5](https://md5hashing.net/hash/)
- [Online tool 3 - tunnelsup](https://www.tunnelsup.com/hash-analyzer/)
- [python tool Hash_identifier (recommended)](https://gitlab.com/kalilinux/packages/hash-identifier/-/tree/kali/master)
	- `wget https://gitlab.com/kalilinux/packages/hash-identifier/-/raw/kali/master/hash-id.py`
	- run with `python3 hash-id.py`

### Hashcat Command
- `--force` for hashcat can lead to false positive and false negative
- Use `hashcat --help` to find more
- Usecase #1: **Password hash cracking**
- Example command line:
- `hashcat -m 3200 -a 0 -o ~/Downloads/cracked.txt ~/Downloads/hash.txt ~/Downloads/rockyou.txt`
	- `-m 3200`: type of hash
	- `-a 0`: dictionary crack
	- `-o ~/Downloads/cracked.txt`: cracked hash save to
	- `~/Downloads/hash.txt`: hashes to crack
	- `~/Downloads/rockyou.txt`: dictionary used
- Usecase #2: Integrity Checking
- HMACs (Hash-based Message Authentication)
	- A way to check if the hash has been altered

## John the ripper
- A password cracking tool
- [Installation](https://gist.github.com/fijiwebdesign/0a56ec28f1f23412fc16cca70f48d8e0) and [Official install](https://www.openwall.com/john/doc/INSTALL.shtml), read INSTALL for installation on MACOS
> git clone https://github.com/magnumripper/JohnTheRipper jumbo
> cd jumbo/src
> ./configure 
> make clean && make -s
	- alternate configure: `./configure CPPFLAGS="-I$(brew --prefix openssl)/include" LDFLAGS="-L$(brew --prefix openssl)/lib" --disable-pkg-config`
- `john [options] [path to file]`
- cracked password is located in `~/.john/john.pot`
- Automatic cracking: 
	- `john --wordlist=[path to wordlist] [path to file]`
	- e.g. `john --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt`
- Crack with format (need to ass `-raw` for standard hashing)
	-  `john --format=[format] --wordlist=[path to wordlist] [path to file]`
	- `john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt`
- To check john's available supporing encryption format
	- `john --list=formats`
	- `john --list=formats | grep -iF "md5"`

## Other password tools
### Hydra
- [Hydra](https://github.com/vanhauser-thc/thc-hydra): online password cracking tool which can perform rapid dictionary attacks. Adaptive password attacks against of many different services
- example command: `hydra -t 4 -l dale -P /usr/share/wordlists/rockyou.txt -vV 10.10.10.6 ftp`
	- `hydra`: Runs the hydra tool
	- `-t 4`: Number of parallel connections per target
	- `-l [user]`: Points to the user who's account you're trying to compromise
	- `-P [path to dictionary]` Points to the file containing the list of possible passwords
	- `-vV` Sets verbose mode to very verbose, shows the login+pass combination for each attempt
	- `[machine IP]` The IP address of the target machine
	- `[protoco]`: Sets the protocol

## NTHash / NTLM
This is the hash format where Windows system stores user password in hash form
*Previous Window hashing format is known as LM, hence NT/LM
*NT reffered to new technology
- By using *Mimikatz* or from the *Active Directory database*, we can dump NTHash/NTLM hashes stored in SAM database: **NTDS.dit**
- Possible attack method:
	- conduct a "pass the hash" attack
	- we can conduct hash cracking if weak password policy existed

## Linux password file
-  `/etc/shadow`: stors hashes, includes last password change and password expiration information
-  `/etc/passwd`: is usually required for the shadow file to be cracked
-  unshadow is the tool built-in in JTR: `unshadow [path to passwd] [path to shadow]`
	-  e.g. `unshadow local_passwd local_shadow > unshadowed.txt`
-  unshadow accept both file or inline usage:
	-  e.g.  `/etc/passwd` line for the root user: `root:x:0:0::/root:/bin/bash`
	-  e.g. `/etc/shadow` line for the root user: `root:$6$2nwjN454g.dv4HN/$m9Z/r2xVfweYVkrr.v5Ft8Ws3/YYksfNwq96UL1FX0OJjY1L6l.DS3KEVsZ9rOVLB/ldTeEL/OIhJZ4GMFMGA0:18576::::::`
		*Field separated by `:` are called Gecos
-  Then we can crack the `unshadowed.txt` produced by unshadow command
	-  e.g. `john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt`
	*Usually the format doesn't need to be specified
### Crack mode: Single Crack
- Word Mangling: Generate different version of password based-of off username
- e.g. username Markus, the possible variation include:
	- Markus1, Markus2, Markus3 (etc.)
	- MArkus, MARkus, MARKus (etc.)
	- Markus!, Markus$, Markus* (etc.)
- Example Code: `john --single --format=[format] [path to file]`
	- e.g. `john --single --format=raw-sha256 hashes.txt`
- File Formats in Single Crack Mode: `mike:1efee03cdcb96d90ad48ccc7b8666033`
- Word Magling rules can be customized
	- path to the john.conf: `/opt/homebrew/Cellar/john-jumbo/1.9.0_1/share/john/john.conf`
	- [Wordlist Rule Syntax](https://www.openwall.com/john/doc/RULES.shtml)
	e.g. The custom rule can be called using the following command: `john --wordlist=[path to wordlist] --rule=PoloPassword [path to file] `, If the rules looks like this: 
		> [List.Rules:PoloPassword] 
		> cAz"[0-9] [!£$%@]"

## Crack the password of a Compressed file
### Crack Zip file
- Turn the zip file into john's hash
- `zip2john [options] [zip file] > [output file]`
- e.g. `zip2john zipfile.zip > zip_hash.txt`
### Crack rar file
- rar file into hash
- `rar2john [rar file] > [output file]`
- e.g. `rar2john rarfile.rar > rar_hash.txt`

## Crack SSH Keys Password
- `ssh2john [id_rsa private key file] > [output file]`
- python version is available `python3 /opt/ssh2john.py` or `python /usr/share/john/ssh2john.py`
- Then `john --wordlist=used/rockyou.txt encry.txt`
- Note that ssh2john is located in:   `/Users/ryn/Documents/Tools/jumbo/run/ssh2john`

# Encryption
- Encryption storage standards: [PCI-DSS](https://listings.pcisecuritystandards.org/documents/PCI_DSS_for_Large_Organizations_v1.pdf)
- Symmetric encryption: same key to encrypt and decrypt
	- DES, 56 bits long, later became Triple DES (3DES)
	- AES, 128 or 256 bit long
- Asymmetric encryption: one for encrypt, other for decrypt
	- RSA typically uses 2048 to 4096 bit
	- Elliptic Curve cryptography
## RSA
Use the same mathematical theoretical problem that "its hard to find the two prime number multiplied to get the number 14351" (i.e. it's hard to calculate and know that these two numbers: 113 and 127 is the answer of 14351). RSA uses this properly to encrypt data, 113 can be the public key, and 127 can be the private key.
- Some of the RSA crack tool:
	- [RsaCtfTool](https://github.com/RsaCtfTool/RsaCtfTool)
	- [rsatool](https://github.com/ius/rsatool)
-  The key variables RSA in CTFs are p, q, m, n, e, d, and c.
	-  “p” and “q” are large prime numbers
	-   “n” is the product of p and q.
	-   The public key is n and e.
	-   The private key is n and d.
	-   “m” is used to represent the message (in plaintext)
	-   “c” represents the ciphertext (encrypted text).
-   [More about RSA encryption](https://muirlandoracle.co.uk/2020/01/29/rsa-encryption/)

# Note
- HTTPS certificate is a symmetric encryption, where the shared key is send asymetricly at the beginning of the session. [How HTTP works](https://robertheaton.com/2014/03/27/how-does-https-actually-work/)
- **Key Exchange**: A way for two party to exchange the key without observer being able to get the keys: common symmetric keys without actual sending over
	- **[Diffie Hellman Key Exchange](https://www.youtube.com/watch?v=NmM9HA2MQGI)**:
		- create the public keys with the private key
		- public variable both party agreed: g (generator) and n (a prime number usually for mathematic calculation reason 1000-4000 bits long), a (Alice) and b (Bob). All of these are under the assumption that the **mathematic formula works when the order of calculating a or b does not matter**.
			1. Alice: private key + g = ag
			2. Bob: private key + g = bg
			3. Exchange the ag and bg
			4. Alice private + bg = abg
			5. Bob private + ag = abg
			6. Both Alice and Bob has the same key: abg, they can then encrypt and decrypt message via key abg.
- **PGP**: Pretty Good Privacy, software that implements encryptions for encrypting files, digital signing and more
- **[GPG](https://gnupg.org/)**: 
	- Mainly used to decrypt files in CTFs
	- Private keys can be protected with passphrases with GPG
		- if key are protected by passphrases, they can be cracked by JTR and gpg2john
	- [GPG man page](https://www.gnupg.org/gph/de/manual/r1023.html)
- **DES**:
	- Data Encryption Standard
	- Symmetric-key encryption, same key of encryption and decryption
	- It's obsolete betcause it is 56-bit, 56-bit key became very easy to crack using brute force.
- **AES**: Most popular today
	- Advanced Encryption Standard, replacement for DES
	- Sometime are called Rijndael after its creator
	- Operate on blocks of data
	- [How AES works](https://www.youtube.com/watch?v=O4xNJsjtN6E)
- Quantom Computer and Encryption
	- To prevent to the havoc of Quantom Computer and Encryption: 
	- use RSA-3072 or better for asymmetric encryption
	- use AES-256 or better for symmetric encryption
	- [More about it](https://nvlpubs.nist.gov/nistpubs/ir/2016/NIST.IR.8105.pdf)
	- More to read: "Cryptography Apocalypse" By Roger A. Grimes

