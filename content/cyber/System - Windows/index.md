---
title: System - Windows
updated: 2024-02-21 05:56:14Z
created: 2023-03-04 21:47:48Z
latitude: 43.65322600
longitude: -79.38318430
altitude: 0.0000
---

# Window Note

## File System Overall
- **FAT16/FAT32** (File Allocation Table) - Mostly external use
- **HPFS** (High Performance File System) - Not much in use
- **NTFS** New Technology File System
	- Kown as journaling file system: **repair folder/files using a log file**
	- Benefits:
		- Supports files **larger than 4GB**
		- Set specific **permissions** on folders and files
		- Folder and file **compression**
		- **Encryption** (Encryption File System or EFS)
		- Alternate Data Streams (**ADS**)
			- Every file contain one data stream ($DATA), ADS allows file to contains more than a data stream: can use ADS to hide data
			- [More on ADS here](https://www.malwarebytes.com/blog/news/2015/07/introduction-to-alternate-data-streams)
- [More on FAT, HPFS, and NTFS File Systems](https://learn.microsoft.com/en-us/troubleshoot/windows-client/backup-and-storage/fat-hpfs-and-ntfs-file-systems)
- **System enviroment variable directory path**: Stores information about operating system enviroment [More on this here](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.3&viewFallbackFrom=powershell-7.1)
```
%Windir%
```
- 	Most important folder in the **Windows** directory is **System32** directory: contains all the Windows system operational files for the Windows OS to function properly


## System Panel
- Local User and Group Management: **lusrmgr.msc**
- System Configuration for advanced troubleshooting for troubleshooting configuration error.: **msconfig**
[More on System configuration here](https://learn.microsoft.com/en-us/troubleshoot/windows-client/performance/system-configuration-utility-troubleshoot-configuration-errors)
- Task manager: **Ctrl+Shift+Esc**
- Control Panel: **Control.exe**
- Computer Management: **compmgmt** **compmgmt.msc**:
	- System Tools 
	- Storage
	- Services and Applications.
		- WMI is a windows management instrumentation sevice
			- Depricated in Win10 and taken over by Powershell
- System Information: **msinfo32** **msinfo32.exe**
	- Hardware Resources: [Click Here to know more](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/hardware-resources#:~:text=Hardware%20resources%20are%20the%20assignable,of%20bus%2Drelative%20memory%20addresses.)
	- Components
	- Software Environment
- Resource Monitor: **resmon.exe**
- Register: **regedit** **regedt32.exe** [More about registery here](https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/windows-registry-advanced-users)

## Security 
[More on Microsoft Security Update Guide](https://msrc.microsoft.com/update-guide)
- Microsoft Defender SmartScreen: protects against phishing, malware website, application and download of malicious files [More on this topic here](https://learn.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-smartscreen/microsoft-defender-smartscreen-overview)
- Bitlocker encryption system [More on this topic here](https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)
-  Volume Shadow Copy Service (VSS): A snapshot of the selected data
	-  Usually gets deleted first when a ransomware is deployed to prevent recovery
-  Antimalware Scan Interface (AMSI): Allows application and service to integrate with any antimalware product. Provide enhanced malware protection [More on this topic](https://learn.microsoft.com/en-us/windows/win32/amsi/antimalware-scan-interface-portal)
-  Windows Hello: Provide a way to get instant access to Windows device using fingerprint/facial recognition/PIN
-  Windows 10 21H1: Most stable realease
	-  Windows Defender Application Guard (WDAG)
		-  Improved to increase document opening time from the use of UNC path and SMB path
-  **Living Off The Land**: use the build-in tools and utility to go undetected within the enviroment. [More on this resource here](https://lolbas-project.github.io/#)

