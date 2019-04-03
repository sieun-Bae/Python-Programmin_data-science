'''
###indefinite loop
def indefinite():
     sum = 0.0
     count = 0
     moredata = "yes"
     while moredata[0] == "y":
         x = float(input("Enter a number >> "))
         sum = sum + x
         count = count + 1
         moredata = input("Do you have more numbers (yes or no)? ")
     print("\nThe average of the numbers is", sum / count)



###sentinel loop
def sentinel():
	sum=0.0
	count=0
	xStr=input("Enter a number (<Enter> to quit) >> ")
	while xStr != "":
		x=float(xStr)
		sum = sum+x
		count=count+1
		xStr=input("Enter a number (<Enter> to quit) >> ")
	print("\nThe average of the number is", sum/count)

sentinel()

'''
'''
def readfile():
	fileName = input(" What is your filename? ")
	infile = open(fileName, 'r')
	sum = 0.0
	count = 0
	for line in infile:
		sum = sum + float(line)
		count = count+1
	print("\nThe average of the numbers is", sum/count)

readfile()

###exclude blank line
def readfile_mod():
	fileName = input(" What is. our filename? ")
	infile = open(fileName,'r')
	sum=0.0
	count=0
	line=infile.readline()
	while line != "":
		sum = sum+float(line)
		count=count+1
		line=infile.readline()
	print("\nThe average of the numbers is", sum/count)

'''
###split by comma
def nestedloop():
	fileName = input("What file are the numbers in")
	infile = open(fileName, 'r')
	sum = 0.0
	count = 0
	line = infile.readline()
	while line != "":
		for xStr in line.split(","):
			sum = sum+float(xStr)
			count=count+1
		line = infile.readline()
	print("\nThe average of the number is", sum/count)
nestedloop()






















