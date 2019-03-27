#word Frequency exercise by sieun Bae
#Python programming course_by Yung-Jun Ju

#get the sequence of words from the file

def read_file():
	fname = input("File to analyze:")
	text = open(fname, 'r').read()
	text = text.lower()
	for ch in '!"#$%&()*+,_.?:;<=>?@[\\]^_{|}~':
		text = text.replace(ch, ' ')
	words = text.split()

def count():
	counts = {}
	for w in words:
		counts[w] = counts.get(w,0) + 1 ##not exist, set 0, if exist, plus 1

#get list of words that appear in document
uniqueWords = list(counts.keys())
#put list of words in alphabetical order
uniqueWords.sort()
#print words and associated counts
for w in uniqueWords:
	print(w, counts[w])

####example_case### counts = {'foo':5, 'bar':7, 'spam':376}
items = list(counts.items()) 

##items will be a list of tuples
##if items.sort() ==> sort in alphabetical order by the key 
print(items)

def byFreq(pair):
	return pair[1]

items.sort(key=byFreq, reverse = True)

for i in range(len(items)):
	word, count = items[i]
	print("{0:<15}{1:>5}".format(word, count))