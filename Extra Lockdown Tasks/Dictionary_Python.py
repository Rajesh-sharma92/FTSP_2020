# Dictionary in Python :- 
d1 = {} # empty dictionary
print(d1)
print(type(d1))

# key , values = dict

emp = {'empid':1001,
 'empname':'Akshat',
 'esal':10000
 }

print(emp)
print(type(emp))

emp['empid']

for x in emp.keys():
    print(x)
    
for y in emp.values():
    print(y)
    
for x,y in emp.items():
    print(x,y)
    
print(emp)    

emp['Address'] = 'India'

print(emp)
    


    
    
    

























