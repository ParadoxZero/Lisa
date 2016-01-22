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

class Lisa :

	def display(self,data):
		print ""
		for d in data:
			sys.stdout.write(d)
			sys.stdout.flush()
			time.sleep(0.1)
		
	

if __name__ == "__main__":
	l = Lisa()
	while True :
		d = raw_input("")
		l.display(d)
