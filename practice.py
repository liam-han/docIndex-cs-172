import glob
import sys
from collections import Counter

import time
from collections import defaultdict
import math





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
def readFiles() -> []:
	Documents = []
	#path = '/Users/liamhan/Desktop/data/*.txt'
	#path = (path + '/*.txt')
	file = 'ap89_collection'
	print(len(file))
	try:
		with open(file, 'r') as f:
		
			t = str.maketrans(".,'`:;", "      ")
			counter = 0
			for line in f:
				counter += 1
				for word in line.lower().split():
					word = word.translate(t)
					word = word.replace(" ", "")
					Documents.append(word)
				
	except IOError:
		print("Unexpected error:", sys.exc_info()[0])

	print(counter)
	return Documents

g = readFiles()
print(g)