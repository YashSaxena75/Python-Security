import requests
url="dituniversity.edu.in"

def req(url):
	try:
		return requests.get("http://" + url)
	except Exception ,e:
		pass

with open("/root/Downloads/sub.txt","r") as f:
	for x in f:
		word=x.strip()
		turl=word + "." + url
		resp=req(turl)
		if resp:
			print("[+] Discovered subdomain --> " + turl + "\t\t" + str(requests.get("http://" + turl)))

