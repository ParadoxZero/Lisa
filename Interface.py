#
#
#
# Project name : Lisa
#
# A simple chat-Bot.
#
#
# 
import time
import sys
import Interpreter
import splash

class Lisa :

	def display(self,data):
		sys.stdout.write("Lisa : ")
		for d in data:
			sys.stdout.write(d)
			sys.stdout.flush()
			time.sleep(0.1)
		print ""	
	def run(self) :
		while True:
			user_input = raw_input("You :")
			lisa_reply = Interpreter.interpreter().interpret(" " + user_input)
			self.display(lisa_reply)
		

if __name__ == "__main__":
	splash.splash()
	Lisa().run()
