import glob
import sys
from collections import Counter
import time
from collections import defaultdict
import math


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 

    def add(self, data):
        n = Node(data)
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def print(self):
        n = self.head
        if n.next is None:
            print(n.data)
            quit
        while n.next != None:
            print(n.data)
            n = n.next
            if n.next is None:
                print(n.data)

    def getvalue(self):

        arr = []
        n = self.head
        if n.next is None:
            nn = n.data
            arr.append(nn)

            quit
        while n.next != None:

            nn = n.data
            arr.append(nn)
            n = n.next
            if n.next is None:
                nn = n.data
                arr.append(nn)
        return arr

    def sum(self):
        n = self.head
        s = 0
        if n.next is None:
            s += n.data[1]
        while n.next != None:
            s += n.data[1]
            n = n.next
            if n.next is None:
                s += n.data[1]

        return s

    def sum_documents(self):
        n = self.head
        s = 0
        if n.next is None:
            s += 1
        while n.next != None:
            s += 1
            n = n.next
            if n.next is None:
                s += 1

        return s

    def find_frequency(self, num):
        n = self.head
        if n.next is None and n.data[0] is num:
            return n.data[1]
        while n.next != None:
            if n.data[0] is num:
                return n.data[1]
            n = n.next
            if n.next is None and n.data[0] is num:
                return n.data[1]


def remove_stop_words(document):
    stop_words_txt = 'stoplist.txt'
    stop_words = []

    with open(stop_words_txt, 'r') as f:
        for line in f:
            for word in line.split():
                stop_words.append(word)

    # similar_words = set(stop_words) & set(document)

    for a in stop_words:
        for b in document:
            if a == b:
                document.remove(a)


def readFiles(path: '/Users/liamhan/Desktop/data') -> 'Documents = []':
    Documents = []
    #path = '/Users/liamhan/Desktop/data/*.txt'
    path = (path + '/*.txt')
    files = glob.glob(path)
    files.sort()
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

    return Documents



def docIndex(documents) -> dict():

    docIndex = dict()
    for doc in documents:
        l = len(doc)
        ind = (documents.index(doc)) + 1
        docIndex[ind] = l

    return docIndex


def term_frequency(document, docfreq):
    freq = docfreq / len(document)

    return freq


def idf(d, occurrence) -> float:
    size = len(d)
    idf = math.log10(size / occurrence)

    return idf


def tfidf(tf, idf) -> float: 
    tfidf = tf * idf
    return tfidf


path = input('Enter document(s) file path: (i.e /Users/liamhan/Desktop/data): ')
files = readFiles(path)

def wordIndex(doc: readFiles) -> dict():
    temp_documentIDs = dict()
    for d in doc:
        for e in d:
            key = e
            if key not in temp_documentIDs:
                temp_documentIDs[key] = [doc.index(d) + 1]
            else:
                temp_documentIDs[key].append(doc.index(d) + 1)

    postings = []
    temp_postings = []
    wordIndex = dict()
    c = 0
    for key, value in temp_documentIDs.items():
        test_2 = Counter(value)
        list = LinkedList()
        temp = []
        for key2, value2 in test_2.items():
            list.add([key2, value2])
            temp.append([key2, value2])
        sumdocuments = list.sum_documents()
        postings.append(list)
        temp_postings.append(temp)
        wordIndex[key] = [sumdocuments, postings[c]]
        c += 1

    return wordIndex
