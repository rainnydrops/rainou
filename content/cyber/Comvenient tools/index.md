---
title: Comvenient tools
updated: 2024-03-06 00:17:38Z
created: 2024-03-05 22:55:59Z
---

# Comvenient tools

## Bluetooth device
### l2flood
Dependencie: Bluez
flood a bluetooth device with ping: [l2flood](https://github.com/kovmir/l2flood?tab=readme-ov-file)
Usage: `l2flood [MAC address] `
Usage: `l2flood -n 50 [MAC address]`  # with 50% CPU
get a second card to get flood efficiency
`BT_ADDR='00:00:00:00:00:00'` # Set the target address.
`l2flood -i hci0 $BT_ADDR`
`l2flood -i hci1 $BT_ADDR`
*l2ping options work.

### hcitool
`hcitool` : bluetooth connection command
`hcitool dev` show local device
`hcitool -i hci0 scan` use this device to scan **broadcasting bluetooth device**

### Missing files
if no bluetooth.h
install the dev version: sudo apt-get install libbluetooth-dev

### On Mac
Show connected and disconnected devices `system_profiler SPBluetoothDataType`
does not have bluetooth interface, use PacketLogger instead (released by xcode), This is included under the additional tools of xcode


### Other tools
[Bluediving](https://github.com/balle/bluediving)