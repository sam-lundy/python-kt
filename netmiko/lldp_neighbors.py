import os
from getpass import getpass
from netmiko import ConnectHandler
from pprint import pprint

password = os.getenv("PYNET_PASSWORD") if os.getenv("PYNET_PASSWORD") else getpass()

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**cisco4)
output = net_connect.send_command("show lldp neighbors", use_textfsm=True)

print("LLDP Data Structure Type: {}".format(type(output)))
print("HPE Switch Connection Port: {}".format(output[0]["neighbor_interface"]))

net_connect.disconnect()

