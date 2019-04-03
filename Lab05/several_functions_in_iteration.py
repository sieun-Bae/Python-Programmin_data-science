knights = {'gallahad':'the pure', 'robin':'the brave'}
for k,v in knights.items():
	print(k,v)

###enumerate function
i = {'tic', 'tac', 'toe'}
for i,v in enumerate(i):
	print(i,v)


###zip function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('what is your {0}? It is {1}.'.format(q,a))

###reverse function
for i in reversed(range(1,10,2)):
	print(i)

rev = reversed(range(1,10,2))
for i in rev:
	print(i)

basket=['apple', 'orange','apple','pear','orange','banana']
basket_set = set(basket)
print(basket_set)
for f in sorted(set(basket)):
	print(f)