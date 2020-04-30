
Python Indentation :- 
-----------------------
x = 10 

y = 25 

if x < y:
    print('Yes!! X is lesser than y')

    
if x < y:
print('Yes!! X is lesser than y')

if x < y:
                    print('Yes!! X is lesser than y')


Ex :- 

list1 = [10,20,30,40,50]

for x in list1:
    print(x)
    
    
for x in list1:
    print(x , end=' ')


for item in list1:
    print(item)



Python Comments :- 
----------------

1) Single Line Comments :- It represeted by # symbol in Python.
-------------------------

print('This is Simple program')

# print('This is Easy Program')

# print('This is Complex program')

Ex :- 

x = 100 # Interger Value

y = 20.5 # Floating point Value

print('The Value of X :', x)

print('The Value of Y :', y)


2) Multi Line Comments :-
-------------------------- It is respresented by ''' codes '''. 

Ex :- 

'''
This is Basic Program.

This class is Taken by Tech Guys Coding Studio People.
'''

print('This is Tech Guy here')

Ex :- To get the square of Numbers.


def square(n): # Function defning / FFunction definition / Function Creation.
    ''' It takes the number and do the sqauare of it.'''
    return n**2


square(2) # Function Calling.


NOTE :- DocStrings is nothing Document Strings.

Ex :- 

__doc__

print(square.__doc__)
    
Ex :- 

class Dog:
    ''' This is like our Family Person.'''
    
print(Dog.__doc__)    
    












