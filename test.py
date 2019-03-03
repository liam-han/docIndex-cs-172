import docIndex as d


def main():
    #path = input('Enter document(s) file path: (i.e /Users/liamhan/Desktop/data): ')
    #files = d.readFiles(path)
    files = d.read_collection('ap89_collection')
    queries = d.read_query()
    wordIndex1 = d.wordIndex(files) #initialize wordIndex for documents
    wordIndex2 = d.wordIndex(queries) #initialize wordIndex for queries
    wi = wordIndex1.word_index() #word_index
    wi2 = wordIndex2.word_index()   
    ps = d.PorterStemmer()
    #while (1):
    data = []
    print(queries[0])
    for x in range(1):
        query = queries[0]
        for word in query:
            temp = []
            user_input = word
            user_input = ps.stem(user_input)
            '''user_input = input('Enter a word: ')
            user_input = ps.stem(user_input)
            
            if user_input == "QUIT" or user_input == "quit":
                exit()'''
            try:

                result = wi.get(user_input)
                freq = result[0]
                di = d.docIndex(files)
                r = result[1].getvalue()

                result2 = wi2.get(user_input)
                freq2 = result2[0]
                di2 = d.docIndex(queries)
                r2 = result2[1].getvalue()
    
                for x, y in r2:
                    idf = round(wordIndex1.idf(di, freq), 5)
                    tf = round(wordIndex1.term_frequency(y, len(files[x - 1])), 5)     
                    tfidf = round(wordIndex1.tfidf(tf, idf), 5)

                    idf2 = round(wordIndex2.idf(di2, freq2), 5)
                    tf2 = round(wordIndex2.term_frequency(y, len(files[x - 1])), 5)     
                    tfidf2 = round(wordIndex2.tfidf(tf2, idf2), 5)

                    print(str(user_input),(str([x, y]), tf2, idf2, tfidf2))     
                    temp.append(tfidf2)
                
                data.append(temp)

                    #temp.append((word, str([x, y]), t_f, i_d_f, tf_idf))
                    #temp.append(tf_idf)
                    # result[1] are the postings for words
                # result[1].print()
                #print('[' + str(user_input) + ']' + " appears in " + '' + str(result[0]) + " document(s) ")
            except:
                #print('Entered word is not in the word index, try again:')
                pass

 

if __name__ == "__main__":
    main()
