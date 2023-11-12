import scapy.all as scapy
from scapy.layers import http
from mac_address_lezione import cambio_mac_optparse as mac_changer


def sniff(interface):
    packet = scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
    process_sniffed_packet(packet)


def process_sniffed_packet(packets):
    if packets.haslayer(http.HTTPRequest):
        packets.show()


def main():
    interface = 'eth0'
    sniff(interface)


if __name__ == "__main__":
    main()
