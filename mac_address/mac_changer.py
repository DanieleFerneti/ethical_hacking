import subprocess
import optparse
import re
"""
def first_method():
    subprocess.call("sudo ifconfig eth0 down", shell=True)
    subprocess.call("sudo ifconfig eth0 hw ether 00:11:22:33:44:66", shell=True)
    subprocess.call("sudo ifconfig eth0 up", shell=True)
    subprocess.call("ifconfig", shell=True)

def second_method():
    interface = "eth0"
    new_mac = "00:11:22:33:44:77"
    subprocess.call("sudo ifconfig " +interface+ " down", shell=True)
    subprocess.call("sudo ifconfig " +interface+ " hw ether "+new_mac, shell=True)
    subprocess.call("sudo ifconfig " +interface+ " up", shell=True)
    subprocess.call("ifconfig", shell=True)

def third_method():
    interface = input("A quale interfaccia vuoi cambiare il MAC address ?")
    new_mac = input("Scrivi il nuovo MAC address : ")
    subprocess.call("sudo ifconfig " + interface + " down", shell=True)
    subprocess.call("sudo ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("sudo ifconfig " + interface + " up", shell=True)
    subprocess.call("ifconfig", shell=True)

def fourth_method():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args()
    interface = options.interface
    mac_address = options.new_mac

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["sudo",  "ifconfig", interface, "up"])
"""


def get_mac_interface():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("The interface value is missing. Use --help for more info")
    if not options.new_mac:
        parser.error("The mac address value is missing. Use --help for more info")

    return options


def change_mac_interface(new_interface, new_mac_address):
    subprocess.call(["sudo", "ifconfig", new_interface, "down"])
    subprocess.call(["sudo", "ifconfig", new_interface, "hw", "ether", new_mac_address])
    subprocess.call(["sudo", "ifconfig", new_interface, "up"])


def fifth_method():
    options = get_mac_interface()
    change_mac_interface(options.interface, options.new_mac)
    ifconfig_output = subprocess.check_output(["ifconfig", options.interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_output))
    if mac_address_search_result.group() == options.new_mac:
        print("Success! The MAC address has been correctly changed")

    else:
        print("Error! The MAC address has NOT been correctly changed")

# first_method()
# second_method()
# third_method()
# fourth_method()
# fifth_method()

def main():
    fifth_method()


if __name__ == "__main__":
    main()




