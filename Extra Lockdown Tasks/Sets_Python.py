'''
Sets in Python :- 
---------------
'''

1) It is denoted by {}.
Ex :- 

s1 = set()
print(s1)
print(type(s1))

Ex :-

s1 = {10,20,30,40,50,20,10}
print(s1)

s1[0]
s1[2] = 'Raj'

s1.add(2020)
print(s1)

s1.remove(50)
print(s1)

s1 = {10,20,30,40}
s2 = {10,20,50,99}

s1.union(s2)

s1.intersection(s2)

Ex :- 

list1 = [10,20,30,40,20,10,30,50]

s1 = set(list1)
print(s1)
print(type(s1))

list1 = list(s1)
print(list1)
print(type(list1))


















