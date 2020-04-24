# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:59:23 2020

@author: Rajesh
"""
'''
Python JSON :- 
--------------
'''
JSON is a syntax for storing and exchanging data.

JSON is text, written with JavaScript object notation.

NOTE :- Python has a built-in package called json, which can be used to work with JSON data.

Import the json module:

import json

Parse JSON - Convert from JSON to Python :- 
-------------------------------------------
If you have a JSON string, you can parse it by using the json.loads() method.

Ex :- Convert from JSON to Python.

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y['name']) # John
print(y['age']) # 30
print(y['city']) # New York

Ex :- 

import json

# some JSON:
x = '{"name":"Usha_Babudaya" , "Age":25 , "city":"Sikar,Rajasthan,India"}'

y = json.loads(x)

print(y['name']) # Usha_Babudaya
print(y['Age']) # 25
print(y['city']) # Sikar,Rajasthan,India

'''
Convert from Python to JSON :- 
------------------------------
'''
If you have a Python object, you can convert it into a JSON string by using the 
json.dumps() method.

Ex :- 

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y) 
# {"name": "John", "age": 30, "city": "New York"}

y # '{"name": "John", "age": 30, "city": "New York"}'

'''
NOTE :- You can convert Python objects of the following types, into JSON strings :- 
------------------------------------------------------------------------------------
'''
1) dict
2) list
3) tuple
4) str
5) int
6) float
7) True
8) False
9) None

NOTE :- Convert Python objects into JSON strings, and print the values.

Examples :- 

import json

print(json.dumps({"name": "John", "age": 30})) # {"name": "John", "age": 30}

print(json.dumps(["apple", "bananas"])) # ["apple", "bananas"]

print(json.dumps(("apple", "bananas"))) # ["apple", "bananas"]

print(json.dumps("Hello")) # "Hello"

print(json.dumps(42)) # 42

print(json.dumps(31.76)) # 31.76

print(json.dumps(True)) #true

print(json.dumps(False)) # false

print(json.dumps(None)) # null

NOTE :- When you convert from Python to JSON, Python objects are converted into 
the JSON (JavaScript) equivalent:

Python	     JSON
dict	     Object
list	     Array
tuple	     Array
str	         String
int	         Number
float	     Number
True	     true
False	     false
None	     null


NOTE :- Convert a Python object containing all the legal data types.

Ex :- 

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
----------- Result -------
{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

'''
Format the Result :- 
------------------------
The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.

The json.dumps() method has parameters to make it easier to read the result.
'''
NOTE :- Use the indent parameter to define the numbers of indents.
Ex :- 

json.dumps(x , indent=4)
x
----------- Result------
{'name': 'John',
 'age': 30,
 'married': True,
 'divorced': False,
 'children': ('Ann', 'Billy'),
 'pets': None,
 'cars': [{'model': 'BMW 230', 'mpg': 27.5},
  {'model': 'Ford Edge', 'mpg': 24.1}]}
 

NOTE :- You can also define the separators, default value is (", ", ": "), which means
using a comma and a space to separate each object, and a colon and a space to separate 
keys from values.

Ex :- Use the separators parameter to change the default separator.

print(json.dumps(x , indent=4 , separators = (". ", " = ")))
---------- Result ---------
{
    "name" = "John". 
    "age" = 30. 
    "married" = true. 
    "divorced" = false. 
    "children" = [
        "Ann". 
        "Billy"
    ]. 
    "pets" = null. 
    "cars" = [
        {
            "model" = "BMW 230". 
            "mpg" = 27.5
        }. 
        {
            "model" = "Ford Edge". 
            "mpg" = 24.1
        }
    ]

}


'''
Order the Result :-
----------------------
The json.dumps() method has parameters to order the keys in the result.
'''
Ex :- Use the sort_keys parameter to specify if the result should be sorted or not.

print(json.dumps(x , indent=4 , sort_keys=True))
---------- Result ---------

{
    "age": 30,
    "cars": [
        {
            "model": "BMW 230",
            "mpg": 27.5
        },
        {
            "model": "Ford Edge",
            "mpg": 24.1
        }
    ],
    "children": [
        "Ann",
        "Billy"
    ],
    "divorced": false,
    "married": true,
    "name": "John",
    "pets": null
}



