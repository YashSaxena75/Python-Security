import crypt
import time
import sys

def tpass(cryptpass):
        salt=cryptpass[0:2]
        f=open('/root/Desktop/rockyou.txt','r')
        for word in f.readlines():
                word=word.strip('\n')
                cword=crypt.crypt(word,salt)
                print("cword :",cword)
                if cword==cryptpass:
                        print ("[+]Password matched!")
                else:
                        print ("[-]Password not found!")
def main():
        p=open('/root/Desktop/rockyou.txt')
        for line in p.readlines():
                if ":"in line:
                        user=line.split(':')[0] 
                        cryptpass=line.split(':')[1].strip(' ') 
                        print ("[+]Cracking Password for : "+user),
                        sys.stdout.flush()
                        tpass(cryptpass)
if __name__=="__main__":
        main() 
