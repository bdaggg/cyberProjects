import scapy.all as scapy

ipAdress = input("enter the ip you want to scan: ")

arp_request = scapy.ARP(pdst=ipAdress)
#scapy.ls(scapy.ARP()) you can get help about function
broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#scapy.ls(scapy.Ether()) you can get help about function
full_packet = arp_request/broadcast
(answer,unanswer) = scapy.srp(full_packet,timeout=1)
answer.summary()
