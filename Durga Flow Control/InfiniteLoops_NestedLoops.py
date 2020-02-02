# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 21:58:06 2020

@author: Rajesh
"""

########### Infinite loops ################

i = 1

# while True:

while(True):
    
    print('Forsk coding school',i)
    
    i = i + 1
    
    print('Rajesh sharma')
    
    break # It's used to stop the execution of next lines.
    
    print('Jaipur Rajasthan , India ') # This line will be never executed coz its already loop has been breaked.
    
    
    ##################  Nested Loops ############# 
    
    # NOTE :- Range always start from 0 to n-1 form.
    
    # Nested Loops :- Loops inside the loops are called Nested loops.
    
    for i in range(3): # 0 , 1 , 2 => Outer loop
        
        for j in range(2): # 0 , 1 => Inner Loop
            
            print('Hello')
            
            ### output ###
           """
            Hello
            Hello
            Hello
            Hello
            Hello
            Hello
            """
            
     
   ##################  Nested Loops #############     
   
    for i in range(3): # 0 , 1 , 2 => Outer loop
       
       for j in range(2): # 0 , 1 => Inner Loop
            
           print('i = {} , j = {}'.format(i,j))
         
            ### output ###
            
            i = 0 , j = 0
            i = 0 , j = 1
            i = 1 , j = 0
            i = 1 , j = 1
            i = 2 , j = 0
            i = 2 , j = 1
                        
            
            
            