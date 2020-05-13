# map() & reduce() in Python :- 

Ex :- 

def square(x):
    return x*x # return x**2

l1 = [1,2,3,4,5]

res = list(map(square,l1))
print('The Result :', res)

res = list(map(lambda x : x*x ,l1))
print('The Result :', res)

Ex :- Different filter() & map()

l1 = [10,20,31,33,24] # filter
res = list(filter(lambda x : x%2==0 ,l1))
print('The Result :', res)


l1 = [10,20,31,33,24] # map
res = list(map(lambda x : x%2==0 ,l1))
print('The Result :', res)

# reduce method :- 

from functools import reduce
'''
def add(x,y):
    return (x+y)
'''
l1 = [1,2,3,4,5] # 15

l2 = [10,20,22,31,45] # 128

res = reduce(lambda x,y :x+y ,l2)
print('The Result :', res)




