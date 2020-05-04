# Dictionary Methods in Python :- 
1) pop 
2) popitem
3) clear
4) keys
5) values
6) items
7) copy
8) len()

Ex :- 

emp = {
       'empid':2000,
       'ename':'surya',
       'esal':25000
       
       }
emp['empdept'] = 'Python coding'

print(emp)

emp.pop('empdept')
print(emp)

emp.popitem()
print(emp)

print(len(emp))

new_dict = emp.copy()
print(new_dict)

new_dict['Emprank']='Developer'
print(new_dict)
print(emp)

del new_dict['Emprank']
print(new_dict)

new_dict.clear()
print(new_dict)

del new_dict

print(new_dict)

