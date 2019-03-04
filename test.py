import docIndex as d
import numpy as np

import math

def query_execution(documents):

    wordIndex1 = d.wordIndex(documents) #initialize wordIndex for documents
    wordIndex2 = d.wordIndex(documents) #initialize wordIndex for queries
    wi = wordIndex1.word_index() #word_index
    wi2 = wordIndex2.word_index()

    ps = d.PorterStemmer()
    data = []
    for doc in documents:
        temp = []
        for word in doc:
            user_input = word
            user_input = ps.stem(user_input)
            if user_input not in doc:  #add 0 if query term does not exist in document
                    temp.append([str(user_input), 0])
                    continue
            try:
                result2 = wi2.get(user_input)
                freq2 = result2[0]
                di2 = d.docIndex(documents)
    
                r2 = result2[1].getvalue()
                
                for x, y in r2:
                    if x  == documents.index(doc) + 1:  
                        idf2 = round(wordIndex2.idf(len(documents), freq2), 5)

                        tf2 = round(wordIndex2.term_frequency(y, len(doc)), 5)   
                        tfidf = round(wordIndex2.tfidf(tf2, idf2), 5)
                        #print(str(user_input),(str([x, y]), tf2, idf2))     
                        temp.append([str(user_input), tfidf])
                        continue
            except:
                pass
                
        data.append(temp)

       # print(data)
    return data

def query_execution2(documents):

    wordIndex1 = d.wordIndex(documents) #initialize wordIndex for documents
    wordIndex2 = d.wordIndex(documents) #initialize wordIndex for queries
    wi = wordIndex1.word_index() #word_index
    wi2 = wordIndex2.word_index()

    ps = d.PorterStemmer()
    data = []
    q = d.read_query()
    queries = q[0]
    print(queries)

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
                    di2 = d.docIndex(documents)
        
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

def norm(data):
    sum = 0
    for x in data:
        sum += x ** 2
    

    return math.sqrt(sum)
def dot_product(q, d):

    g = sum([x*y for x,y in zip(q,d)])
    return g


def main():
  
    documents = d.read_collection('ap89_collection')
    queries = d.read_query()
    data2 = d.query_execution(queries[0])
    data = d.query_execution2(documents)
    

    cs = list ()
    for j in range(len(data2)):
        temp = []
        for i in range(len((data[0]))):
            try:    
                query_norm = norm(data2[j])
                document_norm = norm(data[j][i])
                dp = dot_product(data2[j], data[j][i])
                p = query_norm * document_norm
                cosine_similarity = (dp)/p
                temp.append(cosine_similarity)
            except:
                pass
        
        cs.append(temp)
    
    q = d.read_query()
    query_num = q[1]
    print('file'+str(4))
    for i in range(len(cs)):
        filename = 'results_file'+ str(n)
        file = open(“testfile.txt”,”w”) 

      
if __name__ == "__main__":
    main()
