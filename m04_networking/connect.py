from netmiko import ConnectHandler

cisco_sandbox_devices = {
    "ios": {
        "device_type": "cisco_ios",
        "hostname": "192.168.188.16",
        "port": 22,
        "username": "n1mbu5",
        "password": "n3tw0rks",
    },
    # "nxos": {
    #     "device_type": "cisco_nxos",
    #     #"hostname": "name switch",
    #     "port": 22,
    #     "username": "n1mbu5",
    #     "password": "n3tw0rks",
    #     "host": "192.168.188.24"
    # }
}


def netmiko_connect(device_type):

    # cisco_sandbox_device = {
    #     "csr": {
    #         "device_type": "cisco_ios",
    #         #"hostname": "ios ble....",
    #         "port": 22,
    #         "username": "n1mbu5",
    #         "password": "n3tw0rks",
    #         "host": "192.168.188.16"
    #     },
    #     "nxos": {
    #         "device_type": "cisco_nxos",
    #         #"hostname": "name switch",
    #         "port": 22,
    #         "username": "n1mbu5",
    #         "password": "n3tw0rks",
    #         "host": "192.168.188.24"
    #     }
    # }

    print(
        f"\n\nConnectin to :{cisco_sandbox_device[device_type]['port']}"
    )
    print("... this may take a little while.")

    connection = ConnectHandler(
        #cisco_sandbox_device[device_type]["hostname"],
        device_type=cisco_sandbox_device[device_type]["device_type"],
        port=cisco_sandbox_device[device_type]["port"],
        username=cisco_sandbox_device[device_type]["username"],
        password=cisco_sandbox_device[device_type]["password"],
        host=cisco_sandbox_device[device_type]["host"]
    )

    return connection

def disconnect(connection):
    connection.disconnect()
