import requests
url="kvkashipur.com"
def req(url):
        try:
                return requests.get("http://" + url)
        except Exception ,e:
                print("[-] No Repsonse By -->" + url)

with open("/root/Downloads/sub.txt","r") as f:
        for x in f:
                word=x.strip()
                turl=url + "/" + word
                resp=req(turl)
                if resp:
                        print("[+] Discovered URL --> " + turl + "\t\t\t\t\t\t\t" + str(requests.get("http://" + turl)))
