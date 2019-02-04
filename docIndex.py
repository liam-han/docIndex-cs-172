import glob
import sys


def readFiles():

    Documents = []
    path = '/Users/liamhan/PycharmProjects/untitled6/data/*.txt'
    files = glob.glob(path)
    files.sort()
    for document in files:
        try:
            with open(document, 'r') as f:
                temp = []
                for line in f:
                    for word in line.split():
                        temp.append(word)
                Documents.append(temp)
        except IOError:
            print("Unexpected error:", sys.exc_info()[0])

    return Documents



def remove_stop_words(document):
    stop_words_txt = 'stoplist.txt'
    stop_words = []

    with open(stop_words_txt, 'r') as f:
        for line in f:
            for word in line.split():
                stop_words.append(word)

    #similar_words = set(stop_words) & set(document)

    for a in stop_words:
        for b in document:
            if a == b:
                document.remove(a)




g = readFiles()
test = g

print(test)
for x in test:
    remove_stop_words(x)

print(test)