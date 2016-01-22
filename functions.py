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


class calculation :
	function_list = [' add ', '+', ' subtract ','-' , ' multiply ' , '*',' divide ','/']
	unwanted_words = [' and ', ' by ', ' from ' ,' to ']	
	def function(self, data):
		for f in self.function_list :
			if data.find(f) != -1 :
				index = data.find(f)
				data = data[index + len(f):]
				for rem in self.unwanted_words:
					data = removeSubstring(data,rem)
				data = data.split()
				return data


if __name__ =="__main__":
	c = calculation()
	d = raw_input()
	d = " " + d 
	print c.function(d)