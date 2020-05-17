# What are Patterns in Python :- 

print('*')
print('Andy')

Pattern :- * * * * *

# print('*****')
# print(2*3)
print(5 * ' *')
print(5 * ' Python')

Pattern :- Python Python Python 

Pattern :- # # # # #
print(10 * ' #')
      
      
Pattern :- A A A A A
print(5 * ' A')

for i in range(5):
    print(5 * 'A')


Pattern :- * * * 
           * * * 
           * * *

for i in range(5):
    print(3 * ' *')

          
Pattern :- *
           *
           *
           *
 
for i in range(5): # 0,1,2,3,4
    print('*')
    
for i in range(5):# 0,1,2,3,4
    print('#' , end=' ')
    
 
for i in range(5): # 0,1,2,3,4
    if i==3:
        break
    print('$')
         
          
Pattern :- 2 2 2
           2 2 2
           2 2 2
             
n = int(input('Enter n Value :'))

for i in range(n):
    print(n * ' 2')
    
    
    
           

