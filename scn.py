import optparse
from socket import *
import socket,sys

def scan(tgthost,tgtport):
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((tgthost,tgtport))
		print "[+] tcp port : " +" "+ str(tgtport) + " "+"state:open"
		banner=s.recv(1024)
		print banner
		s.close()
	except Exception as e:
		print "[-] " , e

def pscan(tgthost,tgtport):
	try:
		tgtIP=socket.gethostbyname(tgthost)
	except:
		print "[-] can't resolve hostname"
	try:
		tgname=socket.gethostbyaddr(tgtIP)
		print "[+]Scan Results for :" + tgtname[0]
	except:
		print "[+]Scan Results for : " + tgtIP
	setdefaulttimeout(1)
	for tgtport in tgtport:
		print "[+] scanning port " +tgtport
		scan(tgthost,int(tgtport))

def main():
        parser=optparse.OptionParser()
        parser.add_option('-H',dest="tgthost",help="Specify Target host")
        parser.add_option('-p',dest='tgtport',help='Specify target port')
        options,argumentss=parser.parse_args()
        tgthost=options.tgthost
        tgtport=str(options.tgtport).split(',')
        if tgthost==None or tgtport==None:
		print "[-]Error"
                
	pscan(tgthost,tgtport)

if __name__ == '__main__':
	main()
