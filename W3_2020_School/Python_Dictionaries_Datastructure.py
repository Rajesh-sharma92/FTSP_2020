# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:26:54 2020

@author: Rajesh
"""
'''
Python Dictionaries Datastructure :- 
-----------------------------------
A dictionary is a collection which is unordered, changeable and indexed. 
In Python dictionaries are written with curly brackets, and they have keys and values.
'''

# How to create the Dictionary.
emp = {
       'ename':'Rajesh',
       'eid':'forsk123',
       'esal':25000
       }

'''
Accessing Items :- 
-----------------
You can access the items of a dictionary by referring to its key name, inside square brackets.
'''

emp['ename'] # 'Rajesh'
emp['eid'] # 'forsk123'
emp['esal'] # 25000

NOTE :- There is also a method called get() that will give you the same result.

emp.get('ename') # 'Rajesh'
emp.get('eid') # 'forsk123'
emp.get('esal') # 25000

'''
Change Values :- 
----------------
You can change the value of a specific item by referring to its key name.
'''
Ex :- Now we will be changing the emp name & salary also.

print(emp) # {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 25000}

emp['ename'] = 'Usha_Babu'

emp['esal'] = 35000

print(emp) # {'ename': 'Usha_Babu', 'eid': 'forsk123', 'esal': 35000}


'''
Loop Through a Dictionary :- 
-------------------------------
You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys of the dictionary, 
but there are methods to return the values as well.
'''
NOTE :- Print all the keys from dictionary one by one.
Ex :- 
for x in emp:
    print(x)
---- Result ----
ename
eid
esal

NOTE :- Print all the values from dictionary one by one.
Ex :- 
for x in emp:
    print(emp[x])
    
NOTE :- We can also use the keys() & values() methods to get the keys & values from dictionary.
    
for x in emp.keys(): # To get the keys.
    print(x)
    
    
for x in emp.values(): # To get the values.
    print(x)
    


NOTE :- Loop through both keys and values, by using the items() function.
Ex :- 

for x,y in emp.items():
    print(x,y)
---- Result ------
ename Usha_Babu
eid forsk123
esal 35000


'''
Check if Key Exists :-
--------------------
To determine if a specified key is present in a dictionary use the in keyword.
'''    
Ex :- 

print(emp) # {'ename': 'Usha_Babu', 'eid': 'forsk123', 'esal': 35000}

if 'eid' in emp:
    print('Yes!! , This key is available into dictionary')
---------  Result -----------    
Yes!! , This key is available into dictionary


'''
Dictionary Length :-
-------------------
To determine how many items (key-value pairs) a dictionary has, use the len() method.
'''
print(emp) # {'ename': 'Usha_Babu', 'eid': 'forsk123', 'esal': 35000}

print(len(emp)) # 3


'''
Adding Items :- 
---------------
Adding an item to the dictionary is done by using a new index key and assigning a value to it.
'''
Ex :- 
print(emp) # {'ename': 'Usha_Babu', 'eid': 'forsk123', 'esal': 35000}

# How to add new key value pair to emp dict.
emp['address'] = 'Jaipur'

print(emp) # {'ename': 'Usha_Babu', 'eid': 'forsk123', 'esal': 35000, 'address': 'Jaipur'}
    
print(len(emp)) # 4

# How to change or replace the old value to new value in dict.
emp['address'] = 'Bangalore'

print(emp) # {'ename': 'Usha_Babu', 'eid': 'forsk123', 'esal': 35000, 'address': 'Bangalore'}


'''
Removing Items :- 
----------------
There are several methods to remove items from a dictionary.
'''
Ex :- pop() method

print(emp) # {'ename': 'Usha_Babu', 'eid': 'forsk123', 'esal': 35000, 'address': 'Bangalore'}

emp.pop('eid') # 'forsk123'

print(emp) # {'ename': 'Usha_Babu', 'esal': 35000, 'address': 'Bangalore'}

Ex :- popitem() method

emp.popitem() # ('address', 'Bangalore')

print(emp) # {'ename': 'Usha_Babu', 'esal': 35000}


Ex :- The del keyword removes the item with the specified key name.

del emp['esal']

print(emp) # {'ename': 'Usha_Babu'}

Ex :- 

The del keyword can also delete the dictionary completely.

del emp

print(emp) # NameError: name 'emp' is not defined # Coz it doesn't exist.


NOTE :- The clear() method empties the dictionary.

# How to create the Dictionary.
emp = {
       'ename':'Rajesh',
       'eid':'forsk123',
       'esal':25000
       }

print(emp) # {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 25000}

emp.clear() # It clears the dict fully.

print(emp) # {} # Empty dictionary.


'''
Copy a Dictionary :- 
--------------------
'''
Ex :- 
emp1 = {
       'ename':'Rajesh',
       'eid':'forsk123',
       'esal':25000
       }

print(emp1) # {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 25000}

emp2 = emp1
    
print(emp2) # {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 25000}

emp2['address'] = 'Jaipur'

print(emp1)  # {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 25000, 'address': 'Jaipur'}
    
print(emp2)  # {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 25000, 'address': 'Jaipur'}
    
# Now we make the copy of the dict1 like new copy dict2.
emp2 = emp1.copy()

emp2.pop('address')

print(emp2) # {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 25000}

print(emp1) # # {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 25000, 'address': 'Jaipur'}

emp1['esal'] = 50000

print(emp1) # {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 50000, 'address': 'Jaipur'}

print(emp2) # {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 25000}


NOTE :- Another way to make a copy is to use the built-in method dict().

# We can make another copy of dict.
new_dict = dict(emp1)
print(new_dict)  # {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 50000, 'address': 'Jaipur'}

'''
Nested Dictionaries :- 
------------------------
A dictionary can also contain many dictionaries, this is called nested dictionaries.
'''
University = {
        'CS_Dept' : {'subject':'Python' , 'Marks':75} ,
        'IS_Dept' : {'subject':'ML' , 'Marks':95} , 
        'Tech_Dept' : {'subject':'DL' , 'Marks':65}
        }


new_university = University.copy()
print(new_university)

University['CS_Dept'] # {'subject': 'Python', 'Marks': 75}

University['CS_Dept']['subject'] # 'Python'

University['CS_Dept']['Marks'] # 75


'''
Dictionary Methods :- 
---------------------
Python has a set of built-in methods that you can use on dictionaries.
'''

fromkeys() method :-
--------------------    
Ex :- 

NOTE :- The fromkeys() method returns a dictionary with the specified keys and the specified value.

x = ('key1', 'key2', 'key3')
y = 0

dict1 = dict.fromkeys(x, y)

print(dict1)


setdefault() :- 
-----------------
The setdefault() method returns the value of the item with the specified key.

If the key does not exist, insert the key, with the specified value, see example below

Ex :-

emp1 = {
       'ename':'Rajesh',
       'eid':'forsk123',
       'esal':25000
       }

x = emp.setdefault("ename", "sharma")
print(x)

print(emp1) # {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 25000}

Ex :- 

x = emp.setdefault('address','Jaipur')
print(x) # Jaipur

print(emp1) # {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 25000}

'''
The update() method inserts the specified items to the dictionary.

The specified items can be a dictionary, or an iterable object.
'''
Ex :- 

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}

Ex :-

emp1 = {
       'ename':'Rajesh',
       'eid':'forsk123',
       'esal':25000
       }

emp1.update({'address':'Jaipur'})

print(emp1)

# {'ename': 'Rajesh', 'eid': 'forsk123', 'esal': 25000, 'address': 'Jaipur'}

