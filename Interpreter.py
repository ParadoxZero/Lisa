#
#
# Text interpretor Module for Lisa
#
#

import reply_engine
import Logics
def removeSubstring(data,str):
	index = data.find(str)
	if index==-1:
		return data
	tmp = data[index+len(str):]
	data = data[:index] + " " + tmp 
	return data

def removeNonNumeric(data):
	i = 0
	strt = -1
	tmp = ""
	while(i < len(data)):
		if(data[i] in ['1','2','3','4','5','6','7','8','9','0',' ']):
				tmp = tmp  + data[i]
		else:
			tmp = tmp + " "
		i = i + 1	
	return tmp


class interpreter :
	reply = reply_engine.reply_engine()
	reply.init()
	# these are the names of operations Lisa can detect
	function_list = [' add ', ' sum ', ' subtract ',' difference ', ' multiply ' ,' product ' ,' divide ', ' quotent ']
	operator_list = ['+','-','*','/']
	# the words Lisa should ignore from list to get purely numeric string
	#unwanted_words = [' and ', ' by ', ' from ' ,' to ',' them ']	
	def interpret(self, data):
		for f in self.function_list :
			ind = [0,0,1,1,2,2,3,3]
			operator = ind[self.function_list.index(f)]
			index = data.find(f)
			if index != -1 :
				data = " " + data[index + len(f):]
				data = removeNonNumeric(data).split()
				print data, operator
				if(len(data) < 2):
					return "The command needs at least 2 numbers"
				rep = "The answer is " + str(Logics.calculate(data,operator))
				return rep
		for f in self.operator_list :
			index = data.find(f)
			if index != -1:
				data = data.split(f)
				i=0
				while i < len(data):
					data[i] = removeNonNumeric(data[i])
					i = i +1
				operator = self.operator_list.index(f)
				rep = "The answer is " + str(Logics.calculate(data,operator))
				return rep
		data_ab = data[1:]
		return  self.reply.get_reply(data_ab) #"Undefined input: no data available"

	






if __name__ =="__main__":
	c = interpreter()
	d = raw_input()
	d = " " + d + " "
	print c.interpret(d)