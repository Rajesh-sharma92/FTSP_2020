# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:31:55 2020

@author: Rajesh
"""

" pg : (13) WAP to print this below pattern."

            A   
            BB  
            CCC 
            DDDD
            
n = int(input('Enter n value :'))
for i in range(n):
    print(chr(65+i)*(i+1) , (' '*(n-i-1)))
#print()
    
" pg : (14) WAP to print this below pattern."

            A 
            A B 
            A B C 
            A B C D 
            
n = int(input('Enter n value :'))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j) , (''*(n-i-1)) , end='')
    print()
    
" pg : (15) WAP to print this below pattern."

            * * * *  
            * * *  
            * *  
            *  

n = int(input('Enter n value :'))
for i in range(n):
    print('* ' *(n-i) , (''*(i)))
    
    
" pg : (16) WAP to print this below pattern."

                1111 
                222 
                33 
                4 
                
n = int(input('Enter n value :'))
for i in range(n):
    print(str(i+1)*(n-i) , (''*(i)))
    
    
" pg : (17) WAP to print this below pattern."

            1 2 3 4 
            1 2 3 
            1 2 
            1 

n = int(input('Enter n Value :'))
for i in range(n):
    for j in range(n-i):
        print(j+1 , (''*(i)) , end='')
    print()
    
 " pg : (18) WAP to print this below pattern."

n = int(input('Enter n value :'))
for i in range(n):
    print(chr(65+i)*(n-i) , (''*(i)))

     
     
     
     
    
 
    
    
    
    
    
    
    
    
    
    
    