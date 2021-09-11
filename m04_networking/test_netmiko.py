from netmiko import ConnectHandler

cisco_881 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.188.26',
    'username': 'n1mbu5',
    'password': 'n3tw0rks',
    'port' : 22,          # optional, defaults to 22
    'secret': 'n3tw0rks',     # optional, defaults to ''
}

net_connect = ConnectHandler(**cisco_881)
net_connect.enable()
print(net_connect.find_prompt())
output = net_connect.send_command('show running-config')
print(output)