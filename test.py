a = ['apple', 'peach', 'apple']
b = ['apple']
a.remove('apple')
print(a)
words = set(a) & set(b)
print(words)