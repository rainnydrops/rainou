---
title: _Command
updated: 2024-02-21 17:30:32Z
created: 2024-01-20 20:27:18Z
---


# Mac
## Homebrew
- Check the path of the package: `brew --prefix [package name]`
- The formula are installed within `/opt/homebrew/Cellar`

--- 

# Website
## curl
- Sending POST request
```
curl -X POST http://10.10.111.51/challenges/chall1.php -d'file=/etc/flag1'
```

The difference between POST and GET request is the different line of 
`Content-Type: application/x-www-form-urlencoded
Content-Length: 36
Origin: http://10.10.8.191`

--- 

# Linux

## Commun command
```
history
```
`id`  
### grep
`-c` This prints only a count of the lines that match a pattern
`-h` Display the matched lines, but do not display the filenames.
`-i` Ignores, case for matching
`-l` Displays list of a filenames only.
`-n` Display the matched lines and their line numbers.
`-v` This prints out all the lines that do not matches the pattern
`-e exp` Specifies expression with this option. Can use multiple times.
`-f file` Takes patterns from file, one per line.
`-E` Treats pattern as an extended regular expression (ERE)
`-w` Match whole word
`-o` Print only the matched parts of a matching line, with each such part on a separate output line.
`-A n` Prints searched line and nlines after the result.
`-B n` Prints searched line and n line before the result.
`-C n` Prints searched line and n lines after before the result.

## Sending files 
any source or destination should be in the format of:

	user@ip_address:[directory_path]
```
wget [source]
scp [source] [destination]
```

## Other commands
- Create new hash with salt `openssl passwd -1 -salt new 123`


---

## Networking
```
curl 
```
Transfering any data that is using the internet protocol

```
netcat -lvp 80
```

---

## Processes Control

```
ps /*show current user processes*/
ps aux /* how all user processe*/
top /*real-time statistics*/
kill [PID number]
/*Some signal to processes:
- sigterm: cleanup task
- sigkill: no cleanup
- sigstop: stop/suspend
*/
systemctl [option] [service] /*options are start, stop, enable and disable*/
[command] & /*Run the command in the background*/
fg /*bring the last background process to front ground*/
```

ctrl + c to stop a processes
ctrl + z to background a processes

---

## Automation
cron: scheduled processes
Crontabs: collection of cron
[Crontabs generation website](https://crontab-generator.org/)

```
crontab -e /*edit crontabs*/
[MIN HOUR DOM(Day of month) MONTH DOW(day of week)] [SCRIPT]
```

Example:
```
	0 *12 * * * cp -R /home/cmnatic/Documents /var/backups/
	@reboot /vat/opt/processes.sh
```

---

# Others

listening port 9001
`nc -nlvp 9001`

# Tools

## SQLite
client command: sqlite3
`sqlite3 <database-name>`
`.tables`
`PRAGMA table_info(customers);`
`SELECT * FROM customers;`


## VSCode
Open a file from terminal using VScode
`code [file_name]`

## Mac system
- add PATH: `export PATH=$PATH:[extra_path]`
- Command directory to path should be added through `/etc/paths`

## CMD command

- hostname
- whoami
- ipconfig
- help command: **/?**, **/help**
- cls
- netstat
- **net**: manage network resources
- 