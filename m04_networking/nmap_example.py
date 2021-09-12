import nmap
from pprint import pprint

nm = nmap.PortScanner()

while True:

    ip = input("\nInput IP address to scan: ")
    if not ip:
        break

    print(f"\n--- begining scan of {ip}")
    output = nm.scan(ip, '22-8780', arguments="-sS -sU -O --host-time 600")
    print(f"--- ---- command: {nm.command_line()}")

    print("----- nmap scan output --------------------")
    pprint(output)

    try:
        pprint(nm[ip].all_tcp())
        pprint(nm[ip].all_udp())
        pprint(nm[ip].all_ip())
    except KeyError as e:
        print(f"   ---> failed to get scan results for {ip}")

    print(f"--- end scan of {ip}")

print("\nExiting nmap sanner")

print("\nScanning all hosts in subnet using port 22")
nm.scan("50.50.50.0/24", arguments="-p 22 --open")
print("--- iterating hosts with open port 22 (ssh)")
for host in nm.all_hosts():
    print("--- ---", host)

print("\nScanning all hosts in subnet using port 80")
nm.scan("50.50.50.0/24", arguments="-p 80 --open")
print("--- iterating hosts with open port 80 (http)")
for host in nm.all_hosts():
    print("--- ---", host)

print("\nScanning all hosts in subnet using ICMP")
nm.scan("50.50.50.0/24", arguments="-PE")
print("--- iterating hosts responding to ICMP echo")
for host in nm.all_hosts():
    print("--- ---", host)


def discovered_host(found_host, scan_result):
    if scan_result['nmap']['scanstats']['uphosts'] == '1':
        print(f"--- --- found host: {found_host} scan: {scan_result['nmap']['scanstats']}")


nma = nmap.PortScannerAsync()
print("\nScanning all hosts in subnet using ICMP with callback")
nma.scan("50.50.50.0/24", arguments="PE", callback=discovered_host)
print("--- iterating hosts responding to ICMP echo")
while nma.still_scanning():
    nma.wait(5)
