# quadratic3.py
# A program that computes the real roots of a quadratic equation.
#    Illustrates use of a two-way decision

import math

def main():
	print ("This program finds the real solutions to a quadratic\n")
	a = float(input("Enter coefficient a: "))
	b = float(input("Enter coefficient b: "))
	c = float(input("Enter coefficient c: "))
	discrim = b * b - 4 * a * c
	if (discrim < 0) :
		print("\nThe equation has no real roots!")
	else :
		if (discrim == 0) :
			root = -b / (2 * a)
			print("There is a double root at", root)		 	 
		else :# Do stuff for two roots
			discRoot = math.sqrt(b * b - 4 * a * c)
			root1 = (-b + discRoot) / (2 * a)
			root2 = (-b - discRoot) / (2 * a)
			print ("\nThe solutions are:", root1, root2)

main()
   		    