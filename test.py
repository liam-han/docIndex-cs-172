from collections import Counter


stuff = {'boob' : [1,3,4,4], 'penis': [5,6,7,7]}
appearances = []
for x in range(len(stuff)):
    for key, values in stuff.items():
        for value in values:
            if value not in appearances:
                appearances.append()


