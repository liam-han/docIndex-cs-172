import docIndex as d


def main():
    #path = input('Enter document(s) file path: (i.e /Users/liamhan/Desktop/data): ')
    #files = d.readFiles(path)
    documents = d.read_collection('ap89_collection')

    queries = d.read_query()
    wordIndex1 = d.wordIndex(documents) #initialize wordIndex for documents
    wordIndex2 = d.wordIndex(documents) #initialize wordIndex for queries
    wi = wordIndex1.word_index() #word_index
    wi2 = wordIndex2.word_index()
    ps = d.PorterStemmer()
    #while (1):
    data = []
    query = queries[1]
    print(query)
    for doc in documents:
        temp = []
        #for word in doc:
        for word in query:
            user_input = word
            user_input = ps.stem(user_input)
            if user_input not in doc:  #add 0 if query term does not exist in document
                    temp.append(0)
                    continue
            '''user_input = input('Enter a word: ')
            user_input = ps.stem(user_input)
            
            if user_input == "QUIT" or user_input == "quit":
                exit()'''
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
            
                    #temp.append((word, str([x, y]), t_f, i_d_f, tf_idf))
                    #temp.append(tf_idf)
                    # result[1] are the postings for words
                # result[1].print()
                #print('[' + str(user_input) + ']' + " appears in " + '' + str(result[0]) + " document(s) ")
            except:
                pass
                
        data.append(temp)
    l = len(data)
    print('\n')
    print(data[0])
    print(len(data[0]))

    

 

if __name__ == "__main__":
    main()
