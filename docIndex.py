import glob
import sys
from collections import Counter
import time
from collections import defaultdict
import math
import nltk
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')



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


def remove_stop_words(stopwords, document):
    '''stop_words_txt = 'stoplist.txt'
    stop_words = []

    with open(stop_words_txt, 'r') as f:
        for line in f:
            for word in line.split():
                stop_words.append(word)
    '''
    # similar_words = set(stop_words) & set(document)

    for a in stopwords:
        for b in document:
            if a == b:
                document.remove(a)


def readFiles(path: '/Users/liamhan/Desktop/data') -> []:
    Documents = []
    #path = '/Users/liamhan/Desktop/data/*.txt'
    path = (path + '/*.txt')
    files = glob.glob(path)
    files.sort()
    porter_stemmer = PorterStemmer()

    for document in files:
        try:
            with open(document, 'r') as f:
                temp = []
                for line in f:
                    for word in line.lower().split():
                        word.rstrip(".',")
                        stem_word = porter_stemmer.stem(word)
                        temp.append(stem_word)
                Documents.append(temp)
        except IOError:
            print("Unexpected error:", sys.exc_info()[0])

    stop_words = Documents[-1]
    del Documents[-1]
    for doc in Documents:
        remove_stop_words(stop_words, doc)
    
    

    return Documents

def read_collection(file) -> []:
    Documents = []
    #path = '/Users/liamhan/Desktop/data/*.txt'
    #path = (path + '/*.txt')  
    ps = PorterStemmer()
    try:
        with open(file, 'r') as f:
            
            t = str.maketrans(".,'`:;", "      ")
            counter = 0
            temp = []
            
            for line in f:
                if line.lower().startswith('</doc>'):
                    Documents.append(temp)
                    temp = []
                if line.startswith('<'):
                    continue
                counter += 1
                for word in line.lower().split():
                    '''if word == '</doc>':
                            Documents.append(temp)
                            temp = []'''
                    word = word.translate(t)
                    word = word.replace(" ", "")
                    stem_word = ps.stem(word)
                    temp.append(stem_word)  
                        
    except IOError:
        print("Unexpected error:", sys.exc_info()[0])
    stop_words = 'stoplist.txt'
    for doc in Documents:
        remove_stop_words(stop_words, doc)
    
    return Documents

def read_query() -> []:
    Queries = []
    file = 'query_list.txt'
    ps = PorterStemmer()
    query_number = []
    try:
        with open(file, 'r') as f:
            t = str.maketrans(".,'`:;", "      ")
            for line in f.readlines():
                temp = []
                for word in line.lower().split():
                    word = word.translate(t)
                    word = word.replace(" ", "")
                    stem_word = ps.stem(word)
                    temp.append(stem_word)
                query_number.append(temp[:1])
                Queries.append(temp[1:])
                
    except IOError:
        print("Unexpected error:", sys.exc_info()[0])

    stop_words = 'stoplist.txt'
    for query in Queries:
        remove_stop_words(stop_words, query)
    return Queries, query_number


def docIndex(document) -> dict():

    docIndex = dict()
    for doc in document:
        length = len(doc)
        ind = (document.index(doc)) + 1
        docIndex[ind] = length
    return docIndex

def query_execution(documents):

    wordIndex1 = wordIndex(documents) #initialize wordIndex for documents
    wordIndex2 = wordIndex(documents) #initialize wordIndex for queries
    wi = wordIndex1.word_index() #word_index
    wi2 = wordIndex2.word_index()

    ps = PorterStemmer()
    data = []
    q = read_query()
    queries = q[0]
    for doc in documents:
        temp = []
        for word in doc:
            user_input = word
            user_input = ps.stem(user_input)
            if user_input not in doc:  #add 0 if query term does not exist in document
                    temp.append(0)
                    continue
            try:
                result2 = wi2.get(user_input)
                freq2 = result2[0]
                di2 = docIndex(documents)
    
                r2 = result2[1].getvalue()
                
                for x, y in r2:
                    if x  == documents.index(doc) + 1:  
                        idf2 = round(wordIndex2.idf(len(documents), freq2), 5)

                        tf2 = round(wordIndex2.term_frequency(y, len(doc)), 5)   
                        tfidf = round(wordIndex2.tfidf(tf2, idf2), 5)
                        #print(str(user_input),(str([x, y]), tf2, idf2))     
                        temp.append(tfidf)
                        continue
            except:
                pass
                
        data.append(temp)

       # print(data)
    return data

def query_execution2(documents):

    wordIndex1 = wordIndex(documents) #initialize wordIndex for documents
    wordIndex2 = wordIndex(documents) #initialize wordIndex for queries
    wi = wordIndex1.word_index() #word_index
    wi2 = wordIndex2.word_index()

    ps = PorterStemmer()
    data = []
    q = read_query()
    queries = q[0]
    for query in queries:
        temp2 = []
        for doc in documents:
            temp = []
            for word in query:
                user_input = word
                user_input = ps.stem(user_input)
                if user_input not in doc:  #add 0 if query term does not exist in document
                        temp.append(0)
                        continue
                try:
                    result2 = wi2.get(user_input)
                    freq2 = result2[0]
                    di2 = docIndex(documents)
        
                    r2 = result2[1].getvalue()
                    
                    for x, y in r2:
                        if x  == documents.index(doc) + 1:  
                            idf2 = round(wordIndex2.idf(len(documents), freq2), 5)

                            tf2 = round(wordIndex2.term_frequency(y, len(doc)), 5)   
                            tfidf = round(wordIndex2.tfidf(tf2, idf2), 5)
                            #print(str(user_input),(str([x, y]), tf2, idf2))     
                            temp.append(tfidf)
                            continue
                except:
                    pass        
            temp2.append(temp)
        data.append(temp2)
        # print(data)
    return data

class wordIndex(object):
    def __init__(self, doc):
        self.doc = doc

    def word_index(self) -> dict():
        doc = self.doc

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
            test_2 = Counter(value)              #Groups occurrences of words in dictionary via Counter func. 
            list = LinkedList()                   #initialize linked-list
            temp = []
            for key2, value2 in test_2.items():  
                list.add([key2, value2])
                temp.append([key2, value2])
            sumdocuments = list.sum_documents()
            postings.append(list)
        
            temp_postings.append(temp)
            wordIndex[key] = [sumdocuments, postings[c]]        #assign [#documents word appears, pointer to postings list] to wordIndex
            c += 1

        return wordIndex

    def term_frequency(self, frequency, total_num_of_terms):
        
        tf = (frequency / total_num_of_terms)

        return tf


    def idf(self, total_num_of_documents, num_of_documents_with_term) -> float:
    
        idf = 1 + math.log2(total_num_of_documents / num_of_documents_with_term)

        return idf


    def tfidf(self, tf, idf) -> float: 
        tfidf = tf * idf
        return tfidf
