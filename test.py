import docIndex as d



def query_execution(documents):

    wordIndex1 = d.wordIndex(documents) #initialize wordIndex for documents
    wordIndex2 = d.wordIndex(documents) #initialize wordIndex for queries
    wi = wordIndex1.word_index() #word_index
    wi2 = wordIndex2.word_index()

    ps = d.PorterStemmer()
    data = []
    queries = d.read_query()
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
    queries = d.read_query()
    for query in queries:
        temp2 = []
        for doc in documents:
            temp = []
            for word in query:
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
            temp2.append(temp)
        data.append(temp2)
        # print(data)
    return data

    
def main():
  
    documents = d.read_collection('ap89_collection')
    queries = d.read_query()
    data2 = d.query_execution(queries)
    data = d.query_execution2(documents)
    print(len(data2[0]))
    print(len(data[0][0]))
    

if __name__ == "__main__":
    main()
