import docIndex as d

def main():
    while (1):
        user_input = input('Enter a word: ')
        if user_input == "QUIT" or user_input == "quit":
            exit()  
        try:
            result = d.wordIndex.get(user_input)
            freq = result[0]
            di = d.docIndex(d.doc)
            
            #tf = d.term_frequency()
            idf = d.idf(di, freq)  #result[1] are the postings for words
            
            w = str(user_input)
            result[1].print()

            print('[' +  w  +  ']' +  " appears in " + '' + str(result[0]) + " document(s) ")
        except:
            print('Entered word is not in the word index, try again:')
            pass

if __name__ == "__main__":
    main()