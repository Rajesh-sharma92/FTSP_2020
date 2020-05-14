# Swap 2 Variables in Python :- 

Ex :- 

x = 10
y = 20 

temp = x
x = y
y = temp

print('X value :', x) # 20
print('Y value :', y) # 10

# Without using 3rd variable swap.

x = 100
y = 200

x = x+y # 100+200 = 300
y = x-y # 300-200 = 100
x = x-y # 300-100 = 200

print('X value :', x) # 200
print('Y value :', y) # 100

Ex :- 

x = 10
y = 20

x,y = y,x

print('X value :', x) # 20
print('Y value :', y) # 10




