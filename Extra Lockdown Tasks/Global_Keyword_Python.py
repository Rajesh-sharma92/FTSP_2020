'''
Global Variables in Python :- 
----------------------------
'''
x = 100 # Global Variable

def f1(): # Function Defining
    
    global y
    y = 200
    print('The Local Variable :', y)
    print('The Global Variable :', x)

f1() # Function Calling

print('The Global Variable :', x)
print('The Local Variable :', y) # Outside

















