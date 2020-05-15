# Sets Comprehension in Python :- 

s1 = {10,20,30,20,10,40,50}
print(s1)

s2 = set()
print(type(s2))

for i in s1:
    s2.add(i)
    
print(s2)    
    
Ex :- Sets Comprehension.

s2 = {i for i in s1}
print(s2)


Ex :- Square of elemenst in set.

s1 = {1,2,3,4,5,1,4}
print(s1)
s2 = set()


for i in s1:
    s2.add(i*i)
    
print(s2)    

Ex :- sets compre.

s2 = {i*i for i in s1}
print(s2)

Ex :- Even Nos. from sets.

s1 = {2,10,15,14,21,12}
s2 = set()

s2 = { i for i in s1 if i%2==0 }
print(s2)

s1 = {10,21,20,15,16,22}
s2 = set()

s2 = {i for i in s1 if i%3==0 }
print(s2)



