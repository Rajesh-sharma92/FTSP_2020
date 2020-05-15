# List Comprehension in Python :- 
Ex :- 

l1 = [10,20,'Andy',20.5,-101]
l2 = [] # empty list

for i in l1:
    l2.append(i)
print(l2)

# List Comprehension
# Syntax :- [expr for val in data Condn]

l2 = [i for i in l1]
print(l2)

# Square of list elements.
l1 = [1,2,3,4,5]
l2 = [] # empty list

for i in l1:
    l2.append(i*i)
print(l2)

# List Comprehension

l2 = [i*i for i in l1]
print(l2)

l2 = [i**2 for i in l1]
print(l2)

# Even Nos. from list.

l1 = [4,12,21,25,20]
l2 = [] # empty list

for i in l1:
    if i%2==0:
        l2.append(i)
print(l2)        

# List Comprenhesnsion

l2 = [i for i in l1 if i%2==0]
print(l2)




