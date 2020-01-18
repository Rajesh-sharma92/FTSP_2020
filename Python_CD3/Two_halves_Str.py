# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 07:46:46 2020

@author: Rajesh
"""

"""
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.

"""

s=str(input('Enter any string :'))

print('The Total Length of String :', len(s))

if len(s)%2==0:
    even_str1=s[: (len(s)//2) ]
    even_str2=s[(len(s)//2) :]
    
    print('The First Half of Even String:',even_str1)
    print('The Second Half of Even String:',even_str2)
    
else:
    
    if len(s)%2!=0:
            
        odd_str1=s[: (len(s)//2) +1 ]
        odd_str2=s[(len(s)//2) +1  :]
        
        print('The First Half of Odd String:',odd_str1)
        print('The Second Half of Odd String:',odd_str2)
    



 