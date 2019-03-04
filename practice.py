import glob
import sys
from collections import Counter
import re
import time
from collections import defaultdict
import math
import string




'''word_data = """It originated from the idea that there
			  are readers who prefer learning new 
			  skills from the comforts of their drawing rooms"""'''
# First Word tokenization
word_data = ['ok..', 'test.']

#Next find the roots of the word
'''user_input = input('enter string \n')
print('\n')

print(word_data)
user_input = porter_stemmer.stem(user_input)

for w in word_data:
	   print(w.rstrip('.'))
	   if porter_stemmer.stem(w) == user_input:
			  print(porter_stemmer.stem(w))



'''
'''def read_query() -> []:
	Queries = []

	file = 'query_list.txt'
	try:
		with open(file, 'r') as f:
			t = str.maketrans(".,'`:;", "      ")
			for line in f.readlines():
				temp = []
				for word in line.lower().split():
					word = word.translate(t)
					word = word.replace(" ", "")
					temp.append(word)
				Queries.append(temp[1:])
				
	except IOError:
		print("Unexpected error:", sys.exc_info()[0])

	return Queries


def read_collection(file) -> []:
	Documents = []
	#path = '/Users/liamhan/Desktop/data/*.txt'
	#path = (path + '/*.txt')

	try:
		with open(file, 'r') as f:
			
			t = str.maketrans(".,'`:;", "      ")
			counter = 0
			temp = []
			
			for line in f.readlines():
				counter += 1
				for word in line.lower().split():
					if word.startswith('<') or word.endswith('>'):
						if word == '</doc>':
							Documents.append(temp)
							temp = []
						del word
						continue
					word = word.translate(t)
					word = word.replace(" ", "")
					temp.append(word)
				
			
				
	except IOError:
		print("Unexpected error:", sys.exc_info()[0])

	print(counter)
	return Documents

file = 'ap89_collection'
g = read_collection(file)
Queries = read_query()
for query in Queries:
	for word in query:
		print(word)

'''


