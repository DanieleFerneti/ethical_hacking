import scapy.all as scapy


def scan(ip_address):
    #scapy.arping(ip_address)

    broadcast = scapy.Ether(dst = "FF:FF:FF:FF:FF:FF")

    arp_request = scapy.ARP()
    arp_request.pdst = ip_address

    #scapy.ls(scapy.ARP)

    arp_request_broadcast = broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast,timeout = 1)[0]
    print('----------------------------------------')
    print('IP\t\t\tMAC address\t|')
    print('----------------------------------------')
    for ans in answered:
        ris = ans[1].psrc + '\t' + ans[1].src + '\t|'
        #ans[1].show()
        print(ris)



def main():
    ip_add = '192.168.186.0/24'
    scan(ip_add)


if __name__ == '__main__':
    main()