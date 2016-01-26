


def calculate(input,operation):
	a = []
	for i in input:
		a.append(float(i))
	#Debug: print a
	res = a[0]
	c = a[1:]
	if operation == 0 :
		for i in c :
			res = res + i
	elif operation == 1:
		for i in c :
			res = i - res
	elif operation == 2:
		for i in c :
			res = res * i
	elif operation == 3:
		for i in c :
			res = res / i
	return res

		
