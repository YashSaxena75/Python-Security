#change the MAC Address
import subprocess
import optparse
import re


def oldmac(interface):
	h=subprocess.check_output(["ifconfig", options.interface])
	n=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",h)
	if n:
		return n.group(0)
	else:
		print("Can't fetch the MAC")



def changemac(interface):
	print("Changing MAC address of "+interface)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["service", "network-manager", "stop"])
	subprocess.call(["macchanger", "-r", interface,])
	subprocess.call(["service", "network-manager", "start"])
	#print("[+] MAC of " + interface + " Changed Successfuly!")

def parser():
	parser=optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
	parser.add_option("-m", "--mac" ,dest="mac" ,help="New MAC address")
	(options,arguments)=parser.parse_args()
	if not options.interface:
		parser.error("[-] Please Specify an interface, Use --help for more info.")
	#if not options.mac:
	#	parser.error("[-] Please specify a MAC"):
	return options

def mac(interface):
	x=subprocess.check_output(["ifconfig" ,options.interface])
	m=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", x)
	if m:
		return m.group(0)
	else:
		print("Can't fetch the MAC")

options=parser()
changemac(options.interface)
omac=oldmac(options.interface)
cmac=mac(options.interface)
print("Current MAC:",cmac)

if omac==cmac:
	print("[+] MAC changed.")
else:
	print("[-] Can't change the MAC.")
