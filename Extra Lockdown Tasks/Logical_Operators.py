# Logical Operators in Python :- 
# Identity 
# Membership 

Truth table
and , or , not 

x y o/p
0 0 0 
0 1 0
1 0 0
1 1 1

ex:- 

x = 100
y = 200

print(x<y and y>x)

print(x<y and y<x)

OR Truth Table 

x y o/p
0 0 0 
0 1 1
1 0 1
1 1 1

Ex :- 

x = 1001
y = 200

print(x<y or x>y)

x = True
print(not(x))

EX :- 

x = 100
y = 200

print(x<y)

print(not(x<y))

# Identity Operator :-

is , is not 

x = 100
#y = 200
y = 100
print(x is y)
print(x is y)

print(id(x))
print(id(y))

x = 100
y = 200

print(x is not y)

print(id(x))
print(id(y))

# Membership Operators :-

in , not in

l1 = [10,20,30,'Python','Surya']

print('Python' in l1)

print(1001 not in l1)

print('Apple' in l1)


