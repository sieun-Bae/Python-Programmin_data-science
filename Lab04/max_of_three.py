#max of three

def main():

	x1, x2, x3 = eval(input("Please enter three values: "))
###sol1
	if x1 >= x2 and x1 >= x3:
		maxval = x1
	elif x2 >= x1 and x2 >= x3:
		maxval = x2
	else:
		maxval = x3
###sol2
	if x1 >= x2:
		if x1 >= x3:
			maxval = x1
		else:
			maxval = x3
	else:
		if x2 >= x3:
			maxval = x2
		else:
			maxval = x3
###sol3
	maxval = x1
	if x2 > maxval:
		maxval = x2
	if x3 > maxval:
		maxval = x3
###sol4
	maxval = max(x1, x2, x3)

	print("The largest value is", maxval)