# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 13:06:57 2020

@author: Rajesh
"""
" There are some basic python programs. "

print("Hello, world!") # Valid code.

print('Hello, world!') # Valid code.

print('Hello, world!'); # Valid code.

#################     Python Indentation   #############################

if 5 > 2:
    print('Five is greater than two !') # Valid code coz there is indentation mentioned.
    
###################################################    
    
    if 5 > 2:
    print('Five is greater then two !') # Not Valid coz expected an indented block.
    
#####################################################

    if 5 > 2:
        print('Five is greater than two !')
        if 5 > 2:
            print('Five is greater than two !') # Valid code coz proper Indentation given into code.
            
#########################################################

if 5 > 2:
    print("Five is greater than two!")
          print("Five is greater than two!") # unexpected indent block error.
          

#########################################################

if 5 > 2:
    print("Five is greater than two!")
    print("Five is greater than two!") # It is valid code coz there is proper indentation mentioned.
    print("Hello, World")
    print("Forsk jaipur !!!")    
    
#########################################################

if (10 > 5):
    print('TRUE') # It is valid code and you can use the paraenthesis for condition.
    
##############    Python variables  ######################################
# NOTE :- In python, variables are created when you assign a value to it.
  
x = 5
y = 'Hello , World!'
print(x)
print(y)    
print(type(x))
print(type(y))
    
#################### Comments ######################
# This is single comment line.
print('forsk jaipur, sitapura') # It is valid code.
    
'rajesh sharma'    # It is valid code.

'''
This is multi commamd line.
codes are available in this file.
'''

"""
This is multi commamd line.
codes are available in this file.
"""

print("Hello, World!") # This is a comment.

# print("Hello, World!") --> It won't execute coz single line comment is there.
print("Cheers, Mate!") --> It will execute.

############## Multiline Comments ####################
#This is a comment
#written in
#more than just one line
print("Hello, World!") # specially, in python there is no multiline cooments. we can use like this
# put into triple quotes means multiline strings.

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

"""     
            ###### NOTE #########
Comments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.

"""

####################   Creating Variables  ##################################


Variables are containers for storing data values.

Unlike other programming languages, Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.

x = 5
y = "John"
print(x)
print(y)

#################

NOTE :- whenever you want you can re-assign the value to variables.
x = 4 # x is type od int.
x = "Rajesh" # now, X is type of string.
print(x)                    # O / P :- Rajesh

###############    String Variables    ############

NOTE :- String variables can be declared either by using single or double quotes.

x = "forsk jaipur"
print(x)

x = 'Rajesh sharma'
print(x)

################  Variable Names ######################

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"

NOTE :- Remember that variable names are case-sensitive.

##################  Assign Value to Multiple Variables  #####################

NOTE :- Python allows you to assign values to multiple variables in one line.

x , y , z = 'Orange' , 'Banana' , 'Cherry'
print(x)
print(y)
print(z)
print(x,y,z)

a , b , c = 10, 20 , 30
print(a,b,c)

####################  Assign the same value to multiple variables in one line ########
x = y = z = 'Orange'

print(x)
print(y)
print(z)
print(x,y,z)
print(type(x))
------------------------------------
raj = ravi = suri = 10000

print(raj)
print(ravi)
print(suri)
print(raj,ravi,suri)
print(type(suri))

###################### Output Variables #####################

The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character.

x = 'Awesome'
print('Python is very ' + x)


s = 'Jaipur,(Rajasthan)'
print('Forsk technologies in ' + s)

#############################

You can also use the + character to add a variable to another variable.

x = "Python is "
y = "Very Awesome"
z =  x + y
print(z)

######################################################

For numbers, the + character works as a mathematical operator.

x = 5
y = 10
print(x + y)

######################################################

If you try to combine a string and a number, Python will give you an error.

x = 5 ---> Int Type
y = "John" ----> Str Type
print(x + y) ---> It gives error like unsupported operand type(s) for +: 'int' and 'str'.

#####################   Global Variables  ###########################################

Variables that are created outside of a function are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.

Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc(): # functionn defining.
  print("Python is " + x)

myfunc()

-----------------------------------
s = 'forsk coding school' # Global variable coz it is outside the function declared.

def student_details(): # functionn defining.
    print('Rajesh sharma from '+s) # using inside the function and its working fine.No issue at all.
student_details()   
print('There are so many students from  '+s) # using inside the function and its working fine.No issue at all.
 
########################### Local Variables ###############################

If you create a variable with the same name inside a function, this variable will be local, 
and can only be used inside the function.The global variable with the same name will 
remain as it was, global and with the original value.Create a variable inside a function, 
with the same name as the global variable.

x = "awesome" # Global variable coz it is outside the function declared.
y = 'forsk'
def myfunc(): # function defining.
  x = "fantastic" # Local variable coz it is inside the function declared.
  
  print("Python is " + x)
  print("Python is very easy and  " + x)
  print('Coding school at jaipur ' + y)

myfunc()

print("Python is " + x)
print("Python is Excellent and  " + x)
print('Coding school at jaipur ' + y)

#######################  global Keyword   ######################

Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
If you use the global keyword, the variable belongs to the global scope.

def myfunc(): # functionn defining.
    global x # local variable but its working as global coz we have used global keyword inside function.
    x = "fantastic"
    print("Python is " + x)
  
myfunc()

print("Python is " + x) # This is outside the function.

################# change value of global variable inside a function #################

global keyword if you want to change a global variable inside a function.
To change the value of a global variable inside a function, 
refer to the variable by using the global keyword.

x = "awesome" # Global variable.

def myfunc(): # function defining.
  global x
  x = "fantastic" # local variable but it works as global coz we changed the scope of it inside function.

myfunc()

print("Python is " + x)

#######################  Python Data Types  ############################

Built-in Data Types :- 

In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories.

Text Type:	     str
Numeric Types:	 int, float, complex
Sequence Types:	 list, tuple, range
Mapping Type:	 dict
Set Types:	     set, frozenset
Boolean Type:	 bool
Binary Types:	 bytes, bytearray, memoryview

Getting the Data Type :- 
You can get the data type of any object by using the type() function.

x = 10
print(x)
print(type(x))

x = 20.20
print(x)
print(type(x))

x = 'forsk jaipur'
print(x)
print(type(x))

x = 10+20j
print(x)
print(type(x))

#################################################################

x = str("Hello World")	----> str	
x = int(20)	---->int	
x = float(20.5)	---->float	
x = complex(1j)	---->complex	
x = list(("apple", "banana", "cherry")) ---->	list	
x = tuple(("apple", "banana", "cherry"))	----> tuple	
x = range(6)	----> range	
x = dict(name="John", age=36) ----> 	dict	
x = set(("apple", "banana", "cherry"))	 ----> set	
x = frozenset(("apple", "banana", "cherry"))	----> frozenset	
x = bool(5)	----> bool	
x = bytes(5)	----> bytes	
x = bytearray(5)	----> bytearray	
x = memoryview(bytes(5)) ---->	memoryview	

######################   Python Numbers   ##################

There are three numeric types in Python.

 ----> int
 ----> float
 ----> complex
 
Variables of numeric types are created when you assign a value to them:


x = 1    # int
y = 2.8  # float
z = 1j   # complex

To verify the type of any object in Python, use the type() function.

print(type(x))
print(type(y))
print(type(z))

------------------------------------------

Int :- 
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


-------------------------------------------------------
Float :-
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

-------------------------------------------------------------
Complex :-
Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

########################  Type Conversion  ######################

You can convert from one type to another with the int(), float(), and complex() methods.

Convert from one type to another:

x = 1 # int
y = 2.8 # float
z = 1j # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

Note: You cannot convert complex numbers into another number type.

###############################  Random Number  ###########################
Random Number :-
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

Import the random module, and display a random number between 1 and 9:

import random

print(random.randrange(1,10))
























































































































































    











































































































































    














    
    
    















            
            
            
            
            