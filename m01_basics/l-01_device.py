from pprint import pprint

# DICTIONARY representing a device
device = {
    "name": "sbx-n9kv-ao",
    "vendor": "cisco",
    "model": "Nexus9000 C9300v Chasis",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.1.1.1",
}

# SIMPLY PRINT
print("\n____ SIMPLE PRINT __________")
print("device:", device)
print("device name:", device["name"])

# PRETTY PRINT
print("\n____ PRETTY PRINT ___________")
pprint(device)

# FOR LOOP, NICELY FORMATTED PRINT
print("\n____ FOR LOOP, USING F-STRING ____________")
for key, value in device.items():
    print(f"{key:>16s} : {value}")