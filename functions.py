#
#
# A small library of functions
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
	while(i < len(data)):
		if((data[i]>'9') or (data[i] < '0')):
			if(strt == -1):
				strt = i 
			if(data[i]==" " and strt != (-1)):
				data = data[:strt] + data[i:]
				strt = -1
		i = i + 1	
	return data

class calculation :
	# these are the names of operations Lisa can detect
	function_list = [' add ', ' subtract ', ' multiply ' , ' divide ']
	operator_list = ['+','-','*','/']
	# the words Lisa should ignore from list to get purely numeric string
	#unwanted_words = [' and ', ' by ', ' from ' ,' to ',' them ']	
	def function(self, data):
		flag = 0
		for f in self.function_list :
			index = data.find(f)
			if index != -1 :
				flag = 1
				data = " " + data[index + len(f):]
				data = removeNonNumeric(data).split()
				if(len(data) < 2):
					return data
				return data
		for f in self.operator_list :
			index = data.find(f)
			if index != -1:
				flag = 1
				return removeNonNumeric(removeSubstring(data,f)).split()
				return data
		if not flag:
			return data + " not possible"

	






if __name__ =="__main__":
	c = calculation()
	d = raw_input()
	d = " " + d + " "
	print c.function(d)