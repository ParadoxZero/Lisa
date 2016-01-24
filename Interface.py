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
import os
#import Interpreter
import splash
import reply_engine
class Lisa :
	lisa_reply = None
	def init(self):
		os.system("clear")
		#splash.splash()
		self.lisa_reply = reply_engine.reply_engine()
		self.lisa_reply.init()
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
			self.display(self.lisa_reply.get_reply(user_input))
		

if __name__ == "__main__":
	i = Lisa()
	i.init()
	i.run()