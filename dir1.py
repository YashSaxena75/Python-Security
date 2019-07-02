import requests,time
ul=""
ull=[]

import urlparse,optparse

print("""

WW      WW EEEEEEE BBBBB    SSSSS  IIIII TTTTTTT EEEEEEE  MM    MM   AAA   PPPPPP  PPPPPP  EEEEEEE RRRRRR
WW      WW EE      BB   B  SS       III    TTT   EE       MMM  MMM  AAAAA  PP   PP PP   PP EE      RR   RR
WW   W  WW EEEEE   BBBBBB   SSSSS   III    TTT   EEEEE    MM MM MM AA   AA PPPPPP  PPPPPP  EEEEE   RRRRRR
 WW WWW WW EE      BB   BB      SS  III    TTT   EE       MM    MM AAAAAAA PP      PP      EE      RR  RR
  WW   WW  EEEEEEE BBBBBB   SSSSS  IIIII   TTT   EEEEEEE  MM    MM AA   AA PP      PP      EEEEEEE RR   RR
															""")


def parser():
	parser=optparse.OptionParser()
	parser.add_option("-t", "--target", dest="ul", help="URL of the website to attack")
	(options,arguments)=parser.parse_args()
	if not options.ul:
		parser.error("[-] Please Specify an URL, Use --help for more info.")
	return options

def url(ul):
	resp=requests.get(ul)
	import re
	return re.findall('(?:href=")(.*?)"',resp.content)

def req(ul):
        try:
		print("Testing URL -->" + ul)
		return requests.get(ul)
        except Exception:
                print("[-] No response by --> " + ul)


with open("/root/Downloads/sub.txt","r") as f:
        for x in f:
		options=parser()
                word=x.strip()
		ul=options.ul
                turl=ul + "/" + word
                resp=req(turl)
                if resp:
			f=open('/root/Desktop/report','a+')
			f.write(turl)
			f.write("\n")
			print("[+] Discovered URL --> " + turl)

def crawl(ul):
	print("Crawler opened!")
	href=url(ul)
	for link in href:
		link=urlparse.urljoin(ul,link)
		if '#' in link:
			link=link.split('#')[0]

		if ul in link and link not in ul:
			ull.append(link)
			print(link)
			crawl(link)
options=parser()
crawl(options.ul)
