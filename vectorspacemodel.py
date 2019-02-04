'''
1 VECTOR SPACE MODEL (non-programming)
'''

def readFile(documents):
    D = []
    whole_text = []
    with open(documents, 'r') as f:
        for line in f:
            temp = []
            for word in line.split():
                temp.append(word)
                whole_text.append(word)
            D.append(temp)

    return D, whole_text


g = readFile('documents.txt')
eight_documents = g[0]
whole_document = g[1]
unique_words = set(whole_document)
print(unique_words)