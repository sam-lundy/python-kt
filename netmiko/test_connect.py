from netmiko import ConnectHandler
import os

csr1000v = {
    'host':	'sandbox-iosxe-recomm-1.cisco.com',
    'username':	'developer',
	'password':	'lastorangerestoreball8876',
    'device_type':	'cisco_xe',
}
xr9000v = {
    'host':	'sandbox-iosxr-1.cisco.com',
    'username':	'admin',
	'password':	'C1sco12345',
    'device_type':	'cisco_xr',
}

all_devices = [csr1000v, xr9000v]

for device in all_devices:
    net_connect = ConnectHandler(**device)
    #print(net_connect.find_prompt)
    output = net_connect.send_command('sh ip bgp sum')
    print(output)
    #filename = device['host'] + ".txt"
    #with open(filename, 'w') as f:
    	#f.write(output)
#print("Collected configuration from " + all_devices['host'])


net_connect.disconnect()
    
    