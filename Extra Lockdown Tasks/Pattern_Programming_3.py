# To Print these below patterns in Python :- 

# Pattern :- 

   j =  0 1 2 3 
   
i = 0  1 2 3 4 
i = 1  1 2 3 4 
i = 2  1 2 3 4 
i = 3  1 2 3 4 

n = int(input('Enter n value :'))

for i in range(n): # 0,1,2,3 # Outer loop
    
    for j in range(n): # 0,1,2,3 # Inner Loop
        
        print(j + 1 , end=' ')
        
    print()   
        
        
# Pattern :-
 
A B C D 
A B C D 
A B C D 
A B C D 

n = int(input('Enter n value :'))

for i in range(n): # 0,1,2,3
    
    for j in range(n): # 0,1,2,3
        
        print(chr(65+j) , end=' ')
        
    print()    
        
        
# print(ord('A'))



