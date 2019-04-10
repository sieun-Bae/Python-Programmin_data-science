
'''
#using new mutable value and store ==> not change
def addInterest(amounts, rate):
	newAmounts = []
	for i in range(len(amounts)):
		newAmounts.append(amounts[i]*(1+rate))
	amounts = newAmounts

def test():
	amounts = [1000,2200, 800, 360]
	rate = 0.05
	addInterest(amounts, rate)
	print(amounts)
'''
#using immutable value and store ==> not change
def addInterest(amount, rate):
	amount = amount*(1+rate)
	
def test():
	amount=1000
	rate=0.05
	addInterest(amount, rate)
	print (amount)

test()
