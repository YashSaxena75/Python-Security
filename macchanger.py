#change the MAC Address
import subprocess
import optparse

def changemac(interface):
	print("Changing MAC address of "+interface)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["service", "network-manager", "stop"])
	subprocess.call(["macchanger", "-r", interface,])
	subprocess.call(["service", "network-manager", "start"])
	print("[+] MAC of " + interface + " Changed Successfuly!")

def parser():
	parser=optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
	(options,arguments)=parser.parse_args()
	if not options.interface:
		parser.error("[-] Please Specify an interface, Use --help for more info.")
	return options

options=parser()
changemac(options.interface)
