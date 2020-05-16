# Tuples Comprehension in Python :-

t1 = (10,20,'Yuvi',20.5,-2020)
print(t1)
print(type(t1)) 

for i in t1:
    print(i)
    
t1 = tuple(i for i in t1)

print(t1)
print(type(t1))

# we have some values and we want to get Square of those.

t1 = (1,2,3,4,5,3)

for i in t1:
    print(i*i)
    
t1 = tuple(i*i for i in t1)    
print(t1)    
    
t1 = tuple(i**2 for i in t1)    
print(t1)    
    
# Even Nos. from tuples.

t1 = (10,11,12,20,21,30)

for i in t1:
    if i%2==0:
        print(i)
        

t1 = tuple( i for i in t1 if i%2==0 )
print(t1)
print(type(t1))





