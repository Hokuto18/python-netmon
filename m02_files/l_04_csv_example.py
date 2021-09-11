from l_00_inventory import csv_inventory
import csv
from pprint import pprint
from tabulate import tabulate
import filecmp

# PART 1: ----- Same procedure as fo JSON, YAML, XML --------------------

# CONVERT INVENTORY TO CSV AND WRITE TO FILE
with open("l_00_inventory.csv", "w") as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerows(csv_inventory)

# READ CSV INVENTORY FROM FILE
with open("l_00_inventory.csv", "r") as csv_in:
    csv_reader = csv.reader(csv_in)
    saved_csv_inventory = list()
    for device in csv_reader:
        saved_csv_inventory.append(device)

# PRINT CSV INVENTORY STRING
print("L_00_inventory.csv file:\n", saved_csv_inventory)

# PRETTY PRINT
print("\ncsv pretty version:")
pprint(saved_csv_inventory)

# COMPARE INVENTORY WE READ, WITH ORIGINAL INVENTORY, TO MAKE SURE THEY ARE EQUIVALENT
print("\n----- compare saved inventory with original --------------------")
if saved_csv_inventory == csv_inventory:
    print("-- worked: saved inventory equals original")
else:
    print("-- failed: saved inventory different from original")

# TURN LIST OF LISTS INTO DICTIONARY
devices = list()
for device_iindex in range(1, len(csv_inventory)):
    device = dict()
    for index, header in enumerate(csv_inventory[0]):
        device[header] = csv_inventory[device_iindex][index]
    devices.append(device)

# PRETTY PRINT DEVICES AS LIST OF DICTS
print("\n----- Devices as list of dicts ---------------------")

# PART II: ------ Read CSV file created by spreadsheet -------------------

# READ FROM CSV FILE CREATED BY SPREADSHEET

# READ FROM CSV FILE CREATED BY SPREADSHEET
with open("devices_for_csv_example.csv", "r") as csv_in:
    csv_reader = csv.reader(csv_in)
    from_spreadsheet_csv_inventory = list()
    for device in csv_reader:
        from_spreadsheet_csv_inventory.append(device)

# TURN LIST OF LISTS INTO DICTIONARY
devices = list()
for device_iindex in range(1, len(from_spreadsheet_csv_inventory)):
    device = dict()
    for index, header in enumerate(from_spreadsheet_csv_inventory[0]):
        device[header] = from_spreadsheet_csv_inventory[device_iindex][index]
    devices.append(device)

# PRETTY PRINT DEVICES AS LIST OF DICTS
print("\n----- Devices from spreadsheet ----------------------")
pprint(devices)

print("\n----- tabulate output of devices form spreadsheet -------------")
print("\n", tabulate(devices, headers="keys"))

# CONVERT PYTHON DATA BACK INTO CSV
headers = devices[0].keys()
with open("l_00_inventory_back_to_csv.csv", "w") as csv_out:
    csv_writer = csv.DictWriter(csv_out, headers)
    csv_writer.writeheader()
    csv_writer.writerows(devices)

print("\n------ compare spreadsheet data with our version ----------")
if filecmp.cmp("devices_for_csv_example.csv", "l_00_inventory.csv"):
    print("-- worked: spreadsheet devices euqals our version")
else:
    print("-- failed BUT EXPECTED TO FAIL: spreadsheet devices different: from our version")



