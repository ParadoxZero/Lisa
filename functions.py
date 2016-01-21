#
#
# A small library of functions
#

def removeSubstring(data,str):
		index = data.find(str)
		if index==-1:
			data = unicode(data, "utf-8")
			return data
		tmp = data[index+len(str):]
		data = data[:index] + " " + tmp
		data = unicode(data, "utf-8")
		return data

class calculation :

	def function(self, data):
		if data.find(" add ") != -1 :
			index = data.find(" add ")
			data = data[index + len(" add "):]
			data = removeSubstring(data," and ")
			print data.isnumeric() 
			if data.isnumeric() :
				print ".yay."
				data = data.split()
			return data
		else :
			return "lame"


if __name__ =="__main__":
	c = calculation()
	print c.function(" add 6 and 5")