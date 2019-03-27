# exception handling__more

import math

def main():
	print("This program finds the real solutions to a quadratic\n")

	try:
		a=float(input("Enter coefficient a: "))
		b=float(input("Enter coefficient b: "))
		c=float(input("Enter coefficient c: "))
		discRoot = math.sqrt(b*b-4*a*c)
		root1 = (-b+discRoot)/(2*a)
		root2 = (-b-discRoot)/(2*a)
		print("\nThe solutions are:", root1, root2)
	except ValueError as excObj:
		if str(excObj) == "Math domain error":
			print("No Real Roots")
		else:
			print("Invlid coefficient given.")
	except:
		print("\nSomethibng went wrong, sorry!")


try:
	x=int(input("Please enter a number: "))

###use this to know which error caused
except Exception as err:
	print(type(err))
	print(err)

else: print('Only when there is no exception, this will excuted.')

try:
	x=int(input("Please enter a number: "))
except ValueError:
	print("That was no valid number. Try again...")
finally: print("Thank you!")