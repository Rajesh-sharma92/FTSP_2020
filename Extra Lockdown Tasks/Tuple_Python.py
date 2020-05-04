'''
Tuples in Python :- 
-------------------
'''
1) It is denoted by ().
Ex :- 

t1 = () # Empty tuple
print(t1)
print(type(t1))

EX :- 

t1 = (10,20,30,40,50,10,20,10)
print(t1)
print(type(t1))

t1[3]
t1[-1]

t1[1:4]

# t1[0] = 'Python'

t1.index(20)
t1.count(10)

l1 = list(t1)

print(l1)
print(type(l1))

l1.append('Easy')
l1.remove(50)

print(l1)

t1 = tuple(l1)
print(t1)
print(type(t1))


