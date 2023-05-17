from netmiko import ConnectHandler
from getpass import getpass

# net_connect = ConnectHandler(
#     host = 'sandbox-iosxe-recomm-1.cisco.com',
#     username = 'developer',
#     #password = getpass(),
#     password = 'lastorangerestoreball8876',
#     device_type = 'cisco_ios',
# )

csr1000v = {
    'device_type': 'cisco_xe',
    'host':     'sandbox-iosxe-recomm-1.cisco.com',
    'username': 'developer',
    'password': 'lastorangerestoreball8876',
}
xr9000v = {
    'device_type':  'cisco_xr',
    'host':     'sandbox-iosxr-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
}

all_devices = [csr1000v, xr9000v]
for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('sh ip int br | ex unass')
    print(device['host'])
    print("=" * len(device['host']))
    print(output)



#net_connect = ConnectHandler(**device)

#hostname
#print(net_connect.find_prompt())

