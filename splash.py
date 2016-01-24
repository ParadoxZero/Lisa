#
# Splash text for Lisa
#
#




import sys
import time

def type(data,delay = 0.1):
	for d in data:
		sys.stdout.write(d)
		sys.stdout.flush()
		time.sleep(delay)
def splash():
	type("Loading",0.05)
	type("...\n",0.3)
	type("initializing system core",0.05)
	type(".............\n",0.16)
	type("loading modules:\n",0.05)
	type("* Machine learning system ",0.05)
	type(".............",0.16)
	type("OK\n",0.05)
	type("* Laguage processor ",0.05)
	type(".............",0.16)
	type("OK\n",0.05)
	type("* Logic processing system",0.05)
	type(".............",0.16)
	type("OK\n",0.05)
	type("Running system diagnostics.........\n")
	type("All systems OK\n",0.05)
	type("Instantiating BOT\nTraining Lisa for Human interaction",0.05)
	type("....\n",0.2)
	type("Training done (100%) OK\n",0.05)
	type("Deploying Lisa ",0.05)
	type("......................\n\n\n")
	type("Lisa Version 2.7 \n")
	type("Running natural language interface.\n\n")
