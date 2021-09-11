from pprint import pprint

device1_str = "  r3-L-n7, cisco, catalyst 2960, ios "

# SPLIT
print("STRING STRIP, SPLIT, REPLACE")
device1 = device1_str.split(",")
print("   ", device1)

# STRIP
device1 = device1_str.strip().split(",")
print("device1 using strip and split:")
print("   ", device1)

# REMOVE BLANKS
device1 = device1_str.replace(" ", "").split(",")
print("device1 replaced blanks using split:\n      ", device1)

# REMOVE BLANKS, CHANGE COMMA TO COLON
device1_str_colon = device1_str.replace(" ", "").replace(",", ":")
print("device1 replaced blanks, comma to colon:")
print("   ", device1_str_colon)

# LOOP WITH STRIP AND SPLIT
device1 = list()
for item in device1_str.split(","):
    device1.append(item.strip())
print("device1 using loop and strip for each item:")
print("   ", device1)

# STRIP AND SPLIT, SINGLE LINE USING LIST OF COMPREHENSION
device1 = [item for item in device1_str.split(",")]
print("device1 using list comprehension:")
print("   ", device1)

# IGNORING CASE
print("\n\nINORING CASE")
model = "CR1000v"
if model == "csr1000v":
    print(f"matched: {model}")
else:
    print(f"didn't match: {model}")

model = "CSR1000V"
if model.lower() == "csr1000v".lower():
    print(f"matched using lower(): {model}")
else:
    print(f"didn't match: {model}")

# FINDING SUBSTRING
print("\n\nFINDING SUBSTRING")
version = "Virtual XE Software (X6_64_LINUX_iosd-UNIVERSALK9-H), Version 16.11.1a, RELEASE SOFTWARE (fc1)"
expected_version = "Version 16.11.1a"
index = version.find(expected_version)
if index >= 0:
    print(f"found version: {expected_version} at location {index} ")
else:
    print(f"not found: {expected_version}")

# SEPARATING STRING COMPONENTS
print("\n\nSEPARATING VERSION STRING COMPONENTS")
version_info = version.split(",")
for version_info_part in version_info:
    print(f"version part: {version_info_part.strip()}")

print("\n\nSEPARATING VERSION STRING COMPONENTS WITH ENUMERATE")
for part_no, version_info_part in enumerate(version_info):
    print(f"version part{part_no}: {version_info_part.strip()}")

show_interface_stats = """
GigabitEthernet1
        switching path      Pkts In     chars In    Pkts Out    Chars Out
              Procesor        25376      1529598        8242       494554
           Route cache            0            0           0            0
     Distributed cache       496298      6064794      673003    218461079
                 Total       521674      62177492     681245    218955633
GigabitEthernet2
        Switching path       Pkts In     Chars In    Pkts Out   Chars Out
             Processor            19         1140           0           0
           Route cache             0            0           0           0
     Distributed cache          6077       663304           0           0
                 Total          6096       664444           0           0
Interface GigabitEthernet3 is disabled

Loopback21
        Switching path       Pkts In     Chars In    Pkts Out   Chars Out
             Processor             0            0          43        2806
           Route cache             0            0           0           0
     Distributed cache             0            0           0           0
                 Total             0            0          43        2806
"""

interface_counters = dict()
show_interface_stats_lines = show_interface_stats.splitlines()
for index, stats_line in enumerate(show_interface_stats_lines):
    if stats_line.find('GigabitEthernet', 0) == 0:

        totals_line = show_interface_stats_lines[index + 5]
        interface_counters[stats_line] = totals_line.split()[1:]

print("\n\n------ Interface Counters ----------------")
pprint(interface_counters)

show_arp = """
Protocol    Address        Age (min)   Hardware Addr   Type    Inerface
Internet    10.10.20.48           -    0050.56bb.e99c  ARPA    GigabitEthernet1
Internet    10.10.20.200         14    0050.56bb.8be2  ARPA    GigabitEthernet2
Internet    10.10.20.254          0    0896.ad9e.444c  ARPA    GigabitEthernet3
"""

arp_table = dict()
for arp_line in show_arp.splitlines():
    if arp_line.lower().find("ineternet", 0) == 0:
        arp_table[arp_line[10:25].strip()] = arp_line[38:52]

print("\n\n----- ARP Table --------------------")
pprint(arp_table)