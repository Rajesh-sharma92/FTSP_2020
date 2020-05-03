'''
Copy() Method in Python :- 
---------------------------
'''
l1 = [10,20,30,40,50]

l2 = l1

print(l1)
print(l2)

l1.append(99)
print(l1)
print(l2)

l2.remove(20)
print(l1)
print(l2)

# copy() method

l1 = [10,20,30,40]

l2 = l1.copy()

print(l1) --- > Original list1
print(l2) ---> Dulpicate list2 -->shallow 

l2.append('Python')
print(l2)
print(l1)

l2.remove(30)
print(l2)
print(l1)



