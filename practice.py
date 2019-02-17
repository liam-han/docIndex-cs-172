'''import nltk
from nltk.stem.porter import PorterStemmer
#nltk.download ('punkt')
'''


'''porter_stemmer = PorterStemmer()


word_data = "It originated from the idea that there are readers who prefer learning new skills from the comforts of their drawing rooms"
# First Word tokenization
nltk_tokens = nltk.word_tokenize(word_data)
#Next find the roots of the word
user_input = input('enter string')
user_input = porter_stemmer.stem(user_input)
print(user_input)
for w in nltk_tokens:
       if porter_stemmer.stem(w) == user_input:
              print(porter_stemmer.stem(w))
              print(w)

'''
ok = 2
def test(a: ok, b: dict()) -> str:
       producct = a*b

       return producct


print(test(4,5)
)
