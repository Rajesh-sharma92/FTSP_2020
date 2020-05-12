# Recursion in Python :- 
# The function calls itself.

Ex :- 

def rec(): # Function Creation
    print('Hello Guys!!')
    rec()
    
rec()   # Function Calling

import sys

print(sys.getrecursionlimit())
print(sys.setrecursionlimit(60))
print(sys.getrecursionlimit())

Ex :- 

import time
i = 0 # Global variable
def rec(): # Function Creation
    global i
    i = i + 1
    print('Hello Guys!!' , i)
    time.sleep(1)
    rec() # Recursion 
    
rec()   # Function Calling




