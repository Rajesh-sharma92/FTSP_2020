# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:28:27 2020

@author: Rajesh
"""

" pg : (25) WAP to print this below pattern." 

                    1
                   22
                  333
                 4444

n = int(input('Enter n value :'))
for i in range(n):
    print(' '*(n-i-1) , str(i+1)*(i+1))


" pg : (26) WAP to print this below pattern." 

               1
              12
             123
            1234

n = int(input('Enter n value :'))
for i in range(n):
    print(' '*(n-i-1) , end='')
    for j in range(i+1):
        print(j+1 , end='')
    print()
    
" pg : (27) WAP to print this below pattern." 

                A
               BB
              CCC
             DDDD

n = int(input('Enter n value :'))
for i in range(n):
    print(' '*(n-i-1) , chr(65+i)*(i+1))

" pg : (28) WAP to print this below pattern." 

                   A
                  AB
                 ABC
                ABCD
n = int(input('Enter n value :'))
for i in range(n):
    print(' '*(n-i-1) , end='')
    for j in range(i+1):
        print(chr(65+j) , end='')
    print()
    
    
" pg : (29) WAP to print this below pattern."   

            ****
              ***
               **
                *

n = int(input('Enter n value :'))
for i in range(n):
    print(' '*(i) , '*'*(n-i))
    
" pg : (30) WAP to print this below pattern."   

             4444
              333
               22
                1
                
n = int(input('Enter n value :'))
for i in range(n):
    print(' '*(i) , str(n-i)*(n-i))
    


    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    












        

