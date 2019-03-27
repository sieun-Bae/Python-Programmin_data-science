# exercise overall

def divide(x, y):
	try:
		result = x/y
	except ZeroDivisionError:
		print("division by zero!")
	except TypeError:
		print("There is type error.")
	else: print("result is", result)
	finally:
		print("executing finally clause")

divide("2","0")