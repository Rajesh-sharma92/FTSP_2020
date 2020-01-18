# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:54:21 2020

@author: Rajesh
"""

# string = "Rajasthan"
# Print characters at the even index number 

str=input('Enter any string to print the  chracter at Even index number :')

i=0 # Even Index

while i<len(str):
    print(str[i])
    i=i+2



str=input('Enter any string to print the  chracter Odd Index number:')

i=1 # Odd Index

while i<len(str):
    print(str[i])
    i=i+2
    
# string = "Forsk"
# Print the given string in reverse 

str=input('Enter any string to Reverse :')
revstr=str[: : -1]
print('The Reversed string :', revstr)
 
# O/P : ksrof

# string = "Forsk Technologies"
#Print Forsk using slicing ( forward indexing Left to Right  )  

str=input('Enter any string to print from left to right index :')
print('The String :', str[0:5])
print('The String :', str[:5])

x = input('Enter any string to print from left to right index :')
y = x.split()
print(y[0])

# string = "Forsk Technologies"
# Print Technologies using slicing ( forward indexing Left to Right ).

str=input('Enter any string to print from Right to Left index :')
print('The String :', str[6:])
print('The String :', str[6: :])

x = input('Enter any string to print from Right to Left index :')
y = x.split()
print(y[1])
print(y[-1])

# string = "Forsk Technologies"
# Print Forsk using slicing ( Reverse indexing Right to Left  ) 
 
s=input('Enter any string :')
rev_str=s.split()
print('The Reversed string :', rev_str[-2])

# string = "Forsk Technologies"
# Print Technologies using slicing ( Reverse indexing Right to Left )

s=input('Enter any string :')
rev_str=s.split()
print('The Reversed string :', rev_str[-1])

# string = "Forsk Technologies"
# Print ksroF using slicing ( forward indexing and Reverse  Indexing)  

s=input('Enter any string :')

print(s[s.index(" ")::-1])

# string = "Forsk Technologies"
# Print siesgolonhceT using slicing ( forward indexing Left to Right )  

s=input('Enter any string :')
print(s[: s.index(" "):-1])

s=input('Enter any string :')
b=s.split()
c=str[: : -1]

# string = "Forsk Technologies"
# Print Technologies Forsk using slicing ( forward indexing Left to Right  )

s=input('Enter any string :')
x=s.split()
x.reverse()
output=" ".join(x)
print(output)


# string = "Forsk Technologies"
# Print Technologies Forsk using slicing ( Reverse indexing Right to Left ) 

s=input('Enter any string :')



s1=input('Enter string A :')
s2=input('Enter string B :')






