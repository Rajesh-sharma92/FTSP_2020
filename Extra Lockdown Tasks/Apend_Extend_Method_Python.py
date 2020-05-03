'''
.apend() & .extend() Methods in Python :- 
-------------------------------------------
'''

l1 = [10,20,30,40,50]

l1.append(99)

print(l1)

l2 = [2019,2020]

l1.append(l2)
print(l1)

#NOTE :- Use the extend method to add 2 lists.

l1.extend(l2)
print(l1)

# NOTE :- + operator .

l3 = l1 + l2 
print(l3)

l1 = [10,20,30]

l2 = ['Rahul','Python']

l3 = l1 + l2

print(l3)



