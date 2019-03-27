# raising errors

id_list = ['data', 'science','python']
try:
	x = input('Please enter an ID')
	if x in id_list:
		raise NameError(x)
except NameError as err:
	print("ID already exists!", err.args[0])