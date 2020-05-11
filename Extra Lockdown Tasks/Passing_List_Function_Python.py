# Can we Pass List & Tuple to Function :- 
Ex :- 

def Test(l1):
    print('Yes!!, We can pass.')
    print(type(l1))
    print(l1)
    
Test([1,2,3,4,5])    

Ex :- 

def square(l1):
    for i in l1:
        print(i**2)
        
square([1,2,3,4,5])
        
# Tuple :- 

def Test(t):
    print('Yes!!, We can pass for Tuple.')
    print(type(t))
    print(t)
    
Test((1,2,3,4,5))    

Ex :- 

def add(t):
    s = 0
    for i in t:
        s = s + i
        print(s)
        
add((1,2,3,4,5))        
 

       
        
        