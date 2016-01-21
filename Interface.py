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
	_replyEngine = replyEngine()
	
	def display(self,data):
		for d in data:
			sys.stdout.write(d)
			sys.stdout.flush()
			time.sleep(0.1)
		print ""

if __name__ == "__main__":
	l = Lisa()

	d = raw_input("")
	l.display(d)
