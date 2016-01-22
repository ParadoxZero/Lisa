#
#
# Text interpretor Module for Lisa
#
#

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
				tmp = tmp + data[i]
		i = i + 1	
	return tmp


class interpreter :
	# these are the names of operations Lisa can detect
	function_list = [' add ', ' subtract ', ' multiply ' , ' divide ']
	operator_list = ['+','-','*','/']
	# the words Lisa should ignore from list to get purely numeric string
	#unwanted_words = [' and ', ' by ', ' from ' ,' to ',' them ']	
	def interpret(self, data):
		for f in self.function_list :
			index = data.find(f)
			if index != -1 :
				data = " " + data[index + len(f):]
				data = removeNonNumeric(data).split()
				if(len(data) < 2):
					return data + " less"
				return data
		for f in self.operator_list :
			index = data.find(f)
			if index != -1:
				return removeNonNumeric(removeSubstring(data,f)).split()
		return data + " not possible"

	






if __name__ =="__main__":
	c = interpreter()
	d = raw_input()
	d = " " + d + " "
	print c.interpret(d)