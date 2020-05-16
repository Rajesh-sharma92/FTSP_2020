# Prime Number in Python :- 

# The no. which is divisible 1 & itself.

# 1 , 7 , 13 , 19 .........n

num = 5

for x in range(2,num):
    if num % x == 0:
        print('Not Prime Number')
        break
    
else:
        
    print('Prime Number')
        




