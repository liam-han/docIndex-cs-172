import docIndex as d


def main():
    path = input('Enter document(s) file path: (i.e /Users/liamhan/Desktop/data): ')
    files = d.readFiles(path)
    wordIndex = d.wordIndex(files)
    while (1):
        user_input = input('Enter a word: ')
        
        if user_input == "QUIT" or user_input == "quit":
            exit()
        try:
            result = wordIndex.get(user_input)
            freq = result[0]
            di = d.docIndex(files)
            r = result[1].getvalue()
            
            for x, y in r:
                i_d_f = round(d.idf(di, freq), 5)
                t_f = round(d.term_frequency(files[x - 1], y), 5)
                tf_idf = round(d.tfidf(t_f, i_d_f), 5)
                # result[1] are the postings for words

                print((str([x, y]), t_f, i_d_f, tf_idf))

            # result[1].print()
            print('[' + str(user_input) + ']' + " appears in " + '' + str(result[0]) + " document(s) ")
        except:
            print('Entered word is not in the word index, try again:')
            pass


if __name__ == "__main__":
    main()
