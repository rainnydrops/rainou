---
title: System - Linux
updated: 2024-02-25 20:19:27Z
created: 2023-03-04 08:13:20Z
latitude: 43.65322600
longitude: -79.38318430
altitude: 0.0000
---

# Linux System Note

# System file format
### Password
- /etc/passwd
- `Username:Password:User ID:Group ID:User ID Info:Home directory:Command/shell`
- `test:x:0:0:root:/root:/bin/bash`
- this command is required to store directly in passwd file, `openssl passwd -1 -salt new 123` or store/update the hash to shadow file
### Crontab
- /etc/crontab
- [ID] [Minute] [Hour] [Day of the month] [Month] [Day of the week] [user:What user the command will run as] [command]
- `# m h dom mon dow user command`
- `17 *   1  *   *   *  root  cd / && run-parts --report /etc/cron.hourly`


## Server on Ubuntu
Ubuntu has a build in pyhton http server that can be run by using the following command:

	python3 -m http.server

serving from a directory called server, it does not have ha way to index or listing the file

---

# Repository
- developper sibmit software to apt repository, only gets to release to public when approved
- "apt" is operation system's repository
	- part of the package management software
	- contain a whole suite of tool to manage packages and source of the software
- can add community repository using following command:
```
add-apt-repository /*or listing another provider*/
```

## Package Control
The process of downloading sublime text 3 manually
1. Add GPG key for the developers of Sublime Text 3 
	- The integrity of the downloaded software is checked using GPG (Gnu Privacy Guard) keys.
``` 
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
```
	download GPG key & use apt-key to trust it
2. Add Sublime Text 3's repository: always have seperate file for different 3rd-party tool added
	- Create /etc/apt/sources.list.d/sublime-text.list
		- /etc/apt/sources.list.d for repository list
		- sublime-text.list for the repository
	- The content of sublime-text.list is the link to the repository
		- "deb https://download.sublimetext.com apt/stable/"
3. Use the apt command to update the repository
```
	apt update
```
4. Install the package
```
	apt install sublime-text
```

**Command to remove the repository**
```
add-apt-repository --remove ppa:PPA_Name/ppa
```
or manually delete the file

**Command to remove software**
```
apt remove [software-name-here]
```

---

# Logs

- located in /var/log directory
- Two main area of interest:
	- access log
	- error log

---

# Command
`locate`:  locate the location of a command or file
`ldd`: check shared libraries are used by the program
`string`: print the printable character in files

