from collections import Counter
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.length = 1

    def add(self, value):
        self.length+=1
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

    def len(self):
        return self.length

    def print(self):
        node = self.head
        while node is not None:
            print (node.value)
            node = node.next

   
  

'''
stuff = {'boob' : [1,3,4,4], 'penis': [5,6,7,7]}
appearances = [[[]]]
counter = 0
for key, values in stuff.items():
    count = 0
    for value in values:
        print(stuff[key].count(value))
            if value not in appearances[counter][0]:
            appearances[counter].append(None)
            appearances[counter].append([value, count])
        else:
            print('else ')
            appearances[counter][-1] = [value, count + 1 ]

    counter += 1

'''
test = {'word': [1,2,3,4,4], 'anotherword': [2,2,4,4,5]}
postings = []
for key, value in test.items():
    test_2 = Counter(value)
    list = LinkedList(len(test_2))
    for key, value in test_2.items():
        list.add([key, value])
    postings.append(list)
    
for x in postings:
    x.print()
    print('break')
