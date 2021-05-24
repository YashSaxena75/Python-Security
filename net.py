import scapy.all as scapy
import optparse
import subprocess
import os

'''try:
	if not os.path.exists('/root/Desktop/i'):
		os.system('/usr/sbin/arp -n >> /root/Desktop/i')
except Exception as e:
	print(e)
f=open(r'/root/Desktop/i','r')
h=f.readlines(0)
j=h[1]
x=j[:15]
r=x[:3]
if int(r)>=0 and int(r)<=127:
	x=x+"/8"
elif int(r)>=128 and int(r)<=191:
	x=x+"/16"
elif int(r)>=192 and int(r)<=223:
	x=x+"/24"
x=x.replace(" ",'') 
'''
#print(x)
def scan(ip):
	req=scapy.ARP(pdst=ip)
	#print(req.summary())
	#print(scapy.ls(scapy.ARP())) #to list all functions/argument
	mac=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	#print(scapy.ls(scapy.Ether())) to list all the arguments we can use
	print(mac.summary())
	reqmac=mac/req
	#print(reqmac.summary()) #who has this ip and mac asked by the source 
	#print(reqmac.show())
	#Upto here we have created a packet using src ip and mac which will be sent over the network and the machine which has the
        # particular ip will respond to the src with its MAC
	ans=scapy.srp(reqmac,timeout=1,verbose=False)[0]
	#print(ans.summary())
	#print(x)
	print("IP\t\t\t\tMAC")
	for el in ans:
		print("_____________________________________________________________________________________________________________________")
		print(el[1].psrc+"\t\t"+el[1].hwsrc)
		print("_____________________________________________________________________________________________________________________")

def parser():
	parser=optparse.OptionParser()
	parser.add_option("-i" ,dest="ip",help="specify the network default gateway")
	(options,arguments)=parser.parse_args()
	if not options.ip:
		print("[-]No range is specified,taking your default gateway to scan.")
		options.ip=x
	return options

options=parser()
scan(options.ip)
