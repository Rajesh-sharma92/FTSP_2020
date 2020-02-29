# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:55:32 2020

@author: Rajesh
"""

Method Resolution Order (MRO) Algorithm :-
----------------------------------------
Hybrid Inheritance :- It contains all type of single , multilevel , multiple and hirechical Inheritance.

class P:
    pass
class C(P):
    def m1(self):
        print('Child class m1() method')
        
c = C()
c.m1()  # Child class m1() method
-------------------------------------------------------------------------------------------------------
class P:
    def m1(self):
        print('Parent class m1() method')
class C(P):
    pass

c = C()
c.m1() # Parent class m1() method
------------------------------------------------------------------------------------------------
class P:
    def m1(self):
        print('Parent class m1() method')
        
class C(P):
    def m1(self):
        print('Child class m1() method')
        
c = C()
c.m1() # Child class m1() method

p = P()
p.m1() # Parent class m1() method
-----------------------------------------------------------------------------------------------------------
MRO examples are below :-
-----------------------
class p:
    def m1(self):
        print('Parent class m1() method')
class C(P):
    pass
print(C.mro())
     
************* Result *****************   
[<class '__main__.C'>, <class '__main__.P'>, <class 'object'>]
---------------------------------------------------------------------------------------------------
class p:
    def m1(self):
        print('Parent class m1() method')
class C(P):
    pass
print(P.mro())
     
************* Result *****************   
[<class '__main__.P'>, <class 'object'>]
--------------------------------------------------------------------------------------------------------------
class p:
    def m1(self):
        print('Parent class m1() method')
class C(P):
    pass

p = P()
p.m1()

print(P.mro())

************* Result *****************   
[<class '__main__.P'>, <class 'object'>]
-----------------------------------------------------------------------------------------------------
NOTE :- Actually, It will be searching always from child class to parent class and finally it will be 
going to the Python Object class or Supermost class in Python.

NOTE :- If there are multiple parents then general approach is from left to right searching.
-------------------------------------------------------------------------------------------------
class P:
    pass
class C(P):
    pass

print(C.mro) # It just prints the address of Object mro() Method.
print(P.mro) # It just prints the address of Object mro() Method.
--------------------------------------------------------------------------------------------------
Ex :- MRO for this particular diagram.

            Object class
                A
            /       \
            /       \
            /       \
            B       c
              \ D / 

class A:
    pass

print(A.mro()) -->> [<class '__main__.A'>, <class 'object'>]
-----------------------------------------------------------------------------------------------------
class A:
    pass
class B(A):
    pass
print(B.mro()) --> [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
-----------------------------------------------------------------------------------------------    
class A:
    pass
class C(A):
    pass
print(C.mro()) --> [<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
------------------------------------------------------------------------------------------------
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass

print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

------------------------------------------------------------------------------------------------------------------------------
Ex :- The above example you can write in this way also.

class A: pass
class B(A): pass
class C(A): pass
class D(B,C): pass
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())

********* Result **************
[<class '__main__.A'>, <class 'object'>]
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
[<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
-----------------------------------------------------------------------------------------------------
Ex :- pls go through this below example.

class A:
    def m1(self):
        print('A class m1 () method')
    
class B(A): 
    def m1(self):
        print('B class m1 () method')
    
class C(A): 
    def m1(self):
        print('C class m1 () method')
    
class D(B,C):
    def m1(self):
        print('D class m1 () method')
    
d = D()

d.m1() # D class m1 () method
print(D.mro())

************** Result ************

[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
-------------------------------------------------------------------------------------------------------
EX :-
class A: pass
class B(A): pass
class C(A): pass
class D(B,C): pass

d = D()

d.m1() # AttributeError: 'D' object has no attribute 'm1'
------------------------------------------------------------------------------------------------------
Ex :-

                        Object Class
                    /       |       \
                   /        |       \
                   A        B        C \
                   \        / \      /  \
                   \        /   \   /    \   
                       X          Y       \
                        \         /        \
                        \         /         \
                          \      /          / 
                              P-------------|


mro(o) --> Object class
mro(A) --> A --> object  class 
mro(B) --> B --> object class
mro(C) ---> C ---> Object class

mro(x) ---> x --> A--> B --> Object class
mro(y) ---> y --> B--> C---> Object class
mro(p) ---> p --> x--> y ---> C--> A--->B--->Object class. NOTE :- It may be wrong also if there is multiple level are there.

Ex :- 
class A: pass
class B:pass
class C:pass

class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass

print(A.mro())
print(B.mro())
print(C.mro())

[<class '__main__.A'>, <class 'object'>]
[<class '__main__.B'>, <class 'object'>]
[<class '__main__.C'>, <class 'object'>]

print(X.mro())
[<class '__main__.X'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

print(Y.mro())

[<class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

print(P.mro())

[<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
----------------------------------------------------------------------------------------------------------------------------------------------
NOTE :- If we are having multiple level of classes then we are not knowing the better solution then
we should for an Algorithm and it is called as C3 Algorithm.

mro(P) = P + Merge(mro(X), mro(Y) , mro(C), XYC)

where XYC means Parent list.

mro(P) = P + Merge(XABO,YBCO,CO,XYC)

NOTE :- For example if we have like ABCDEF.

Head Element = A ---> Always only the first one.
Tail part = BCDEF ---> Apart from first element everything remains the tail part only.

NOTE :- If head element of first list not present in the tail part of any other list then
consider that element in the result and remove that element from all the lists.

mro(P) = P + Merge(mro(X),mro(Y),mro(C),XYC)
mro(P) = P + Merge(XABO,YBCO,CO, XYC)
         P + X + Merge(ABO,YBCO,CO, YC)
         P + X + A + Merge(BO,YBCO,CO,YC)
         P + X + A + Y + Merge(BO,BCO,CO,C)
         P + X + A + Y + B + Merge(O,CO,CO,C)
         P + X + A + Y + B + C + Merge(O,O,O)
         P + X + A + Y + B + C + O                  

Result ==>> P + X + A + Y + B + C + O

[<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

----------------------------------------------------------------------------------------------------------------
Ex :- 
                            Object class(O)
                          /     |      \
                          /     |       \
                         D      E       F
                          \    /      / Here C is child of Parents like D & F not able to draw the diagram properly.
                            B       C 
                            \       /
                                A    

mro(O) --> Object class
mro(D) --> D ---> Object class
mro(E) --> E --> Object class
mro(F) --> F --> Object class
mro(B) --> B --> D ---> E ---> Object class
mro(C) --> C --> D ---> F ---> Object class
mro(A) ----> Here we need to follow the C3 Algorithm and we will be tracing each & every steps.


class D: pass
class E : pass
class F : pass
class B(D,E): pass
class C(D,F): pass
class A(B,C): pass

print(D.mro())
print(E.mro())
print(F.mro())
print(B.mro())
print(C.mro())
print(A.mro())

************* Result ************

[<class '__main__.D'>, <class 'object'>]
[<class '__main__.E'>, <class 'object'>]
[<class '__main__.F'>, <class 'object'>]
[<class '__main__.B'>, <class '__main__.D'>, <class '__main__.E'>, <class 'object'>]
[<class '__main__.C'>, <class '__main__.D'>, <class '__main__.F'>, <class 'object'>]
[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]

------------------------------------------------------------------------------------------------------------
NOTE :- If head element of first list not present in the tail part of any other list then
consider that element in the result and remove that element from all the lists.

mro(A) = A + Merge(mro(B),mro(C), BC)
mro(A) = A + merge(BDEO,CDFO, BC)
       = A + B + Merge(DEO,CDFO, C) 
       = A + B + C + Merge(DEO,DFO)
       = A + B + C + D + Merge(EO,FO)
       = A + B + C + D + E + Merge(O,FO)
       = A + B + C + D + E + F + Merge(O,O)
       = A + B + C + D + E + F + O
       
Result ==>>  A + B + C + D + E + F + O

[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]

------------------------------------------------------------------------------------------------------------------------------------------------------------
Ex :- See that practically also.

class D: 
    def m1(self):
        print('D class m1() method')

class E :
    def m1(self):
        print('E class m1() method')

class F : 
    def m1(self):
        print('F class m1() method')

class B(D,E): 
    def m1(self):
        print('B class m1() method')

class C(D,F): 
    def m1(self):
        print('C class m1() method')

class A(B,C): 
    def m1(self):
        print('A class m1() method')

a = A()
a.m1() # A class m1() method
--------------------------------------------------------------------------------------------------
class D: 
    def m1(self):
        print('D class m1() method')

class E :
    def m1(self):
        print('E class m1() method')

class F : 
    def m1(self):
        print('F class m1() method')

class B(D,E): 
    def m1(self):
        print('B class m1() method')

class C(D,F): 
    def m1(self):
        print('C class m1() method')

class A(B,C): pass
    
a = A()
a.m1() # B class m1() method
------------------------------------------------------------------------------------------------------
class D: 
    def m1(self):
        print('D class m1() method')

class E :
    def m1(self):
        print('E class m1() method')

class F : 
    def m1(self):
        print('F class m1() method')

class B(D,E): pass
    
class C(D,F): 
    def m1(self):
        print('C class m1() method')

    
class A(B,C): pass
    
a = A()
a.m1() # C class m1() method
---------------------------------------------------------------------------------------------------
class D: 
    def m1(self):
        print('D class m1() method')

class E :
    def m1(self):
        print('E class m1() method')

class F : 
    def m1(self):
        print('F class m1() method')

class B(D,E): pass
    
class C(D,F): pass
    
class A(B,C): pass
    
a = A()
a.m1() # D class m1() method
------------------------------------------------------------------------------------------
class D: pass
    
class E :
    def m1(self):
        print('E class m1() method')

class F : 
    def m1(self):
        print('F class m1() method')

class B(D,E): pass
    
class C(D,F): pass
    
class A(B,C): pass
    
a = A()
a.m1() # E class m1() method
------------------------------------------------------------------------------------------------------------
class D: pass
    
class E :pass
    
class F : 
    def m1(self):
        print('F class m1() method')

class B(D,E): pass
    
class C(D,F): pass
    
class A(B,C): pass
    
a = A()
a.m1() # F class m1() method
---------------------------------------------------------------------------------------------
class D: pass
    
class E :pass
    
class F : pass
    
class B(D,E): pass
    
class C(D,F): pass
    
class A(B,C): pass
    
a = A()
a.m1() # AttributeError: 'A' object has no attribute 'm1'
------------------------------------------------------------------------------------------

    





















       
       
       
       























































































































    












































    
        
        
        
        
        
        
        
