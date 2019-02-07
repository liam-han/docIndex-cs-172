from collections import Counter
from collections import deque
'''
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
        while node.next != None:
            node = node.next
        node.next = Node(value)

    def extract(self):
        node = self.head
        while node != None:
            yield node
            print(node.value)
            node = node.next[1]       
            

    def len(self):
        return self.length

    def print(self):
        node = self.head
        while node != None:
            print (node.value)
            node = node.next

    def print_2(self):
        node = self.head
        while node != None: 
            print (node.value) 
            node = node.next

   
    def sum_ll(self):
        node = self.head
        sum = 0
        while node != None:
            sum += node.value[1]
            node  =  node.next[1]
        return sum'''

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

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        n = Node(data)
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def print(self):
        n = self.head
        while n.next != None:
            print (n.data)
            n = n.next
            if n.next is None:
                print(n.data)

    def sum(self):
        n = self.head
        s = 0
        while n.next != None:
            s += n.data[1]
            n = n.next
            if n.next is None:
                s += n.data[1]

        return s
           

test = {'word': [1,2,3,4,4], 'anotherword': [2,2,4,4,5]}
postings = []
for key, value in test.items():
    test_2 = Counter(value)
    list = LinkedList()
    for key, value in test_2.items():
        list.AddNode([key, value])
    postings.append(list)
    
'''for x in postings:
    x.print_2()
    print('break')'''

gasdf = postings[0].sum()
print(gasdf)