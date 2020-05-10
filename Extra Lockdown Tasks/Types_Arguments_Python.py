# Types of Arguments in Python :- 
Ex :- 

def add(x,y): # Formal Args
    z = x+y
    print('The Add :',z)

add(10,20) # Actual Args

# Actual Args.
1) Position
2) Keyword
3) Default
4) Variable Length

Ex :- Position

def emp(ename,eage):
    print(ename)
    print(eage+5)
    
emp('Surya',25)

emp(25,'Surya')
    
Ex :- Keyword

def emp(ename,eage):
    print(ename)
    print(eage+5)
    

emp(eage=25,ename='Surya')

# Default

def emp(ename,eage=18): # Default
    print(ename)
    print(eage)
    

emp('Surya')
emp('Surya',45)

# Variable Length :- 

def add(x,*y):
    z = x+y
    print(z)
    
    
    













    

    





    














    
    
    
    
    
    
    




















