import glob
import sys


def remove_stop_words(stopwords_txt, document):
    stop_words = []


    with open(stopwords_txt, 'r') as f:
        for line in f:
            for word in line.split():
                stop_words.append(word)

    #similar_words = set(stop_words) & set(document)
    for doc in document:
        for a in stop_words:
            for b in doc:
                if a == b:
                    doc.remove(b)

    return document
 
 
def readFiles(path):
    Documents = []
    #path = '/Users/liamhan/Desktop/data/*.txt'
    files = glob.glob(path)
    files.sort()
    stop_words = files[-1]
    files.remove(stop_words)

    #files.remove('/Users/liamhan/Desktop/data/stoplist.txt')


    for document in files:
        
        try:
            with open(document, 'r') as f:
                temp = []
                for line in f:
                    for word in line.lower().split():
                        temp.append(word)
                Documents.append(temp)
        except IOError:
            print("Unexpected error:", sys.exc_info()[0])

    remove_stop_words(stop_words, Documents)

    return Documents


g = readFiles(path)
print(g[0])