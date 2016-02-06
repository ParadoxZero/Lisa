#
#
#
# Project name : Lisa
#
# A simple chat-Bot.
#
# espeak  -ven+f5 'Hey, handsome. Did you just spill soda on my designer bag?' -p67
# 
import time
import sys
import os
import subprocess
import Interpreter
import splash
import reply_engine

processes = set()
class Lisa :
	lisa_reply = None
	def init(self):
		os.system("clear")
		#splash.splash()
		self.lisa_reply = Interpreter.interpreter() 
	def display(self,data):
		processes.add(subprocess.Popen(["espeak",data,"-ven+f5","-p67"]))
		sys.stdout.write("Lisa : ")
		for d in data:
			sys.stdout.write(d)
			sys.stdout.flush()
			time.sleep(0.1)
		print ""	
	def run(self) :
		while True:
			user_input = raw_input("You : ")
			self.display(self.lisa_reply.interpret(" "+ user_input))
		

if __name__ == "__main__":
	i = Lisa()
	i.init()
	i.run()