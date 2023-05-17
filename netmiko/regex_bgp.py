from netmiko import ConnectHandler
from getpass import getpass
import re

ip = input("Enter device IP: ").strip()
username = input("Please enter your username: ").strip()
password = getpass("Please enter your password: ")

device = {
    'ip':   ip,
    'username':	username,
	'password':	password,
    'device_type':	'arista_eos',
}

net_connect = ConnectHandler(**device)
print(net_connect.find_prompt)
output = net_connect.send_command('show ip bgp neighbors')

#print(output)

# for device in all_devices:
#     net_connect = ConnectHandler(**device)
#     print(net_connect.find_prompt)
#     output = net_connect.send_command('show ip bgp neighbors')
#     print(output)
# net_connect.disconnect()

pattern = r"BGP neighbor is (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}), remote AS \d+, internal link\n\s+BGP state = Established"
matches = re.findall(pattern, output)

for match in matches:
    print(match)