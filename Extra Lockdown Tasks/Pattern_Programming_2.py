# How to print this below Pattern in Python :- 
# Pattern :- 

1 1 1 1 
2 2 2 2 
3 3 3 3 
4 4 4 4 

n = int(input('Enter n value :'))

for i in range(n): # 0,1,2,3,4
    print((str(i+1)+' ') * n)
    
s1 = 'Andy'
s2 = ' Candy'
print(s1+s2)


# Pattern :- 

A A A A 
B B B B 
C C C C 
D D D D 

n = int(input('Enter n value :'))

for i in range(n): # 0,1,2,3,4
    print((chr(65+i)+' ') * n)
    

    
print(chr(65)) # A
print(chr(66))
print(chr(67))
print(chr(68))

print(ord('A'))
print(ord('B'))
print(ord('z'))




