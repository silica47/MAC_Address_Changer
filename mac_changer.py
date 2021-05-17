#!/usr/bin/python3

import subprocess
import optparse


print('''
███╗   ███╗ █████╗  ██████╗     ██████╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗██╔════╝    ██╔════╝██║  ██║██╔══██╗████╗  ██║██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║██║         ██║     ███████║███████║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║         ██║     ██╔══██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║╚██████╗    ╚██████╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                          '''

)




def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface")
    parser.add_option("-m", "--mac", dest="macAddress", help="MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error('''<+> Please specify an interface to continue
                        Type --help for help''')
    if not options.macAddress:
        parser.error('''<+> Please specify a MAC Address
                        Type --help for help''')
    return options

def change_mac(interface, macAddress):
    print("<+> Changing MAC Address for: "+interface)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", macAddress])
    subprocess.call(["ifconfig", interface, "up"])
    print("<+> Changed MAC Address to: "+macAddress)
    print("<+> Type ifconfig to see the changes")

options = get_arguments()
change_mac(options.interface, options.macAddress)

