# Zip Function in Python :-

# To coonect the 2 items.
Ex :- 

emp = ('Andy','sandy','Candy','Pandy','Andy')

company = ('TCS','IBM','Wipro','MS','TCS')

z1 = list(zip(emp,company))
print(type(z1))
print(z1)

z2 = set(zip(emp,company))
print(type(z2))
print(z2)


z3 = dict(zip(emp,company))
print(type(z3))
print(z3)

for (x,y) in z1:
    print(x,y)

for (x,y) in z2:
    print(x,y)
    
for (x,y) in z3.items():
    print(x,y)
    
    


