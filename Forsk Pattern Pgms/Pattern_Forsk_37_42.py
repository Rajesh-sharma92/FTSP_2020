# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 21:37:15 2020

@author: Rajesh
"""

" pg : (37) WAP to print this below pattern."
                A
               BBB
              CCCCC
             DDDDDDD

n = int(input('Enter n value :'))
for i in range(n):
    print(' '*(n-i-1) , chr(65+i)*(2*i+1))
    
    
" pg : (38) WAP to print this below pattern."  

                    A
                   CCC
                  EEEEE
                 GGGGGGG
                 
n = int(input('Enter n value :'))
for i in range(n):
    print(' '*(n-i-1) , chr(65+2*i)*(2*i+1))
    
    
" pg : (39) WAP to print this below pattern."    

                   1
                  123
                 12345
                1234567

n = int(input('Enter n value :'))
for i in range(n):
    print(' '*(n-i-1) , end='')
    for j in range(2*i+1):
        print(j+1 , end='')
    print()
    
    
" pg : (40) WAP to print this below pattern."  

                   A
                  ABC
                 ABCDE
                ABCDEFG      
    
n = int(input('Enter n value :'))
for i in range(n):
    print(' '*(n-i-1) , end='')
    for j in range(2*i+1):
        print(chr(65+j) , end='')
    print()

    
" pg : (41) WAP to print this below pattern."      
    
                   1
                  321
                 54321
                7654321
                    
n = int(input('Enter n value :'))
for i in range(n):
    print(' '*(n-i-1) , end='')
    for j in range(2*i+1):
        print((2*i+1)-j , end='')
    print()
    
" pg : (42) WAP to print this below pattern."  

                   A
                  CBA
                 EDCBA
                GFEDCBA
    
n = int(input('Enter n value :'))
for i in range(n):
    print(' '*(n-i-1) , end='')
    for j in range(2*i+1):
        print(chr(65 +(2*i)-j) , end='')
    print()        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
