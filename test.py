from collections import Counter


stuff = {'boob' : [1,3,4,4], 'penis': [5,6,7,7]}
appearances = []
counter = 0
for key, values in stuff.items():
    count = 0
    for value in values:
        print(value)
        if value not in appearances[counter]:
            appearances.append(None)
            appearances[counter] = (value, count)
        else:
            print('else ')
            appearances[counter].append(value, count + 1)

    counter += 1
print(appearances)



