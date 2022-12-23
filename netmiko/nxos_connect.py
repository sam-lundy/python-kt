#!/usr/bin/env python
import os
from netmiko import ConnectHandler
from getpass import getpass


password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

nx01 = {
	"host": 'nxos1.lasthop.io',
	"username": 'pyclass',
	"password": password,
	"device_type": 'cisco_nxos',
}

nx02 = {
	"host": 'nxos2.lasthop.io',
	"username": 'pyclass',
	"password": password,
	"device_type": 'cisco_nxos',
}

for device in (nx01, nx02):

	net_connect = ConnectHandler(**device)
	print(net_connect.find_prompt())

