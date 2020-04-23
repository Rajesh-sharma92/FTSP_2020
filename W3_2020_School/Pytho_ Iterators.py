# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:18:32 2020

@author: Rajesh
"""
'''
Python Iterators :- 
---------------------
'''
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through 
all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, 
which consist of the methods __iter__() and __next__().

Iterator vs Iterable :- 
-------------------------
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator.

Ex :- 

tuple1 = (10,20,'Rajesh','forsk','school',2020)

myit = iter(tuple1)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
-------- Result -----------
10
20
Rajesh
forsk
school
2020

NOTE :- Even strings are iterable objects, and can return an iterator.

Strings are also iterable objects, containing a sequence of characters.

Ex :- 

str1 = 'RAJ'

myit = iter(str1)

print(next(myit))
print(next(myit))
print(next(myit))
-------- Result -----------
R
A
J

Looping Through an Iterator :- 
-----------------------------
We can also use a for loop to iterate through an iterable object.

Ex :- 

str1 = 'FORSK'

for x in str1:
    print(x)
-------- Result -----------
F
O
R
S
K    
    

Ex :- 

list1 = ['Rajesh',1001,'forsk',2020,99]

for x in list1:
    print(x)
-------- Result -----------
 Rajesh
1001
forsk
2020
99

NOTE :- The for loop actually creates an iterator object and executes the next() 
method for each loop.
   
'''
Create an Iterator :-
-----------------------
To create an object/class as an iterator you have to implement the methods __iter__() 
and __next__() to your object.

As you have learned in the Python Classes/Objects chapter, all classes have a function 
called __init__(), which allows you to do some initializing when the object is being created.

The __iter__() method acts similar, you can do operations (initializing etc.), 
but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the next item 
in the sequence.
'''
Ex :- 

Create an iterator that returns numbers, starting with 1, and each sequence will increase \
by one (returning 1,2,3,4,5 etc.)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a = self.a + 1
        return x
    
mn = MyNumbers()
myit = iter(mn)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
    
'''
StopIteration :- 
---------------------
The example above would continue forever if you had enough next() statements, or if 
it was used in a for loop.

To prevent the iteration to go on forever, we can use the StopIteration statement.

In the __next__() method, we can add a terminating condition to raise an error if the 
iteration is done a specified number of times.
'''
Ex :-  Stop after 10 iterations.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a = self.a + 1
      return x
    else:
      raise StopIteration

mn = MyNumbers()
myit = iter(mn)

for x in myit:
  print(x)
  
------------- Result -----------
1
2
3
4
5
6
7
8
9
10

