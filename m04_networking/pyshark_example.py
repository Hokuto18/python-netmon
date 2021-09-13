import pyshark


def print_packet_summary(pkt):
    print("    ", str(pkt)[:120])


# CAPTURE EVERYTHING AND PRINT PACKET SUMARIES
print("\n------ Packet summaries ------------------")
capture = pyshark.LiveCapture(interface='Wi-Fi', only_summaries=True)
capture.sniff(packet_count=10)
for packet in capture:
    print_packet_summary(packet)

# CAPTURE DNS AND PRINT PACKETS
print("\n------ DNS packet summaries ------------------")
capture = pyshark.LiveCapture(interface='Wi-Fi', only_summaries=True, bpf_filter='udp port 53')
capture.sniff(packet_count=10)
for packet in capture:
    print_packet_summary(packet)

# CAPTURE AND PRINT COMPLETE PACKETS
print("\n\n------ All packets, complete ------------------")
capture = pyshark.LiveCapture(interface='Wi-Fi')
capture.sniff(packet_count=10)
for packet in capture:
    print(packet)

#