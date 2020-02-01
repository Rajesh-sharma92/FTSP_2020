# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 10:02:42 2020

@author: Rajesh
"""

" pg : (19) WAP to print this below pattern."

            A B C D 
            A B C 
            A B 
            A 

n = int(input('Enter n value :'))
for i in range(n):
    for j in range(n-i):
        print(chr(65+j) , (''*(i)) , end='')
    print()
    

" pg : (20) WAP to print this below pattern."

                4444 
                333 
                22 
                1 

n = int(input('Enter n value :'))
for i in range(n):
    print(str(n-i)*(n-i) , (''*(i)))

" pg : (21) WAP to print this below pattern." 

                4 3 2 1 
                4 3 2 
                4 3 
                4 
                
n = int(input('Enter n value :'))
for i in range(n):
    for j in range(n-i):
        print((n-j) , (''*(i)) , end='')
    print()
    
" pg : (22) WAP to print this below pattern." 

                    DDDD 
                    CCC 
                    BB 
                    A 

n = int(input('Enter n value :'))
for i in range(n):
    print(chr(65+n-i-1)*(n-i) , (''*(i)) , end='')
    print()

" pg : (23) WAP to print this below pattern." 

            D C B A 
            D C B 
            D C 
            D 

n = int(input('Enter n value :'))
for i in range(n):
    for j in range(n-i):
        print(chr(65+n-j-1) , (''*(i)) , end='')
    print()

" pg : (24) WAP to print this below pattern." 
            
            *
          * *
        * * *
      * * * *

n = int(input('Enter n value :'))
for i in range(a):
    print((''*(n-i-1)) , '* ' *(i+1))


    
 


















