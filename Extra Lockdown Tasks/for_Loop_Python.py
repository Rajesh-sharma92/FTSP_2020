# for loop in Python 

# We know we have the 

sequence data like
lists , tuples,sets
dicts, strigs ..etc..

l1 = [10,20,'Python']

l1[0]
l1[2]

for x in l1:
    print(x)
    
str1 = 'Python Coding'

for x in str1:
    print(x)

for item in str1:
    print(item , end='#')
    
Ex :- 

for x in [10,'Python',20.5]:
    print(x)
   
for x in range(10):
    print(x)

for x in range(20,25):
    print(x)
for x in range(20,30,2):
    print(x)
    
EX :- 
# Even & odd nos.0 to 10.

for x in range(10):
    if (x%2==0):
        print(x)

for x in range(10):
    if (x%2!=0):
        print(x)
        
        
        