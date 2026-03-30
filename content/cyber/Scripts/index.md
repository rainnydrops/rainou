---
title: Scripts
updated: 2024-02-21 04:32:48Z
created: 2024-02-18 05:58:30Z
---

# Scripts

## LinEnum - Privesc
- LinEnum is a simple bash script that performs common commands related to privilege escalation
- [LinEnum script download](https://github.com/rebootuser/LinEnum/blob/master/LinEnum.sh)
- LinEnum output is broken down into following section:
	- If there is `SUID/GUID bit` set: This means that the file or files can be run with the permissions of the file(s) owner/group
		- SUID: rws-rwx-rwx (extra bit “4” is set to user/owner)
		- GUID: rwx-rws-rwx (bit “2” is set to group)
	- Can we read/write sensitive files: usually via `/etc/passwd`
	- Crontab Contents: mainly for cron daemon auto execution
- Available host shell can be seen via `/etc/shells`
- Cronjob: `/etc/cron`
### find SUID file
- `find / -perm -u=s -type f 2>/dev/null`
