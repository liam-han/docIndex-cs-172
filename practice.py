import nltk
from nltk.stem.porter import PorterStemmer 
nltk.download('punkt')



porter_stemmer = PorterStemmer()


'''word_data = """It originated from the idea that there
              are readers who prefer learning new 
              skills from the comforts of their drawing rooms"""'''
# First Word tokenization
word_data = ['ok..', 'test.']

#Next find the roots of the word
user_input = input('enter string \n')
print('\n')

print(word_data)
user_input = porter_stemmer.stem(user_input)

for w in word_data:
       print(w.rstrip('.'))
       if porter_stemmer.stem(w) == user_input:
              print(porter_stemmer.stem(w))



