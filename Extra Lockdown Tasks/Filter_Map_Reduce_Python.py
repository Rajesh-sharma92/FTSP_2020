# Filter Map Reduce in Python :- 
Ex :- To find the even nos from this l1.

def is_even(n):
    return n%2==0

l1 = [5,11,12,16,21,31,41,50]

res = list(filter(is_even , l1))
print('The Result :', res)

Ex :- 

l1 = [11,12,13,14,21,22]

res = list(filter(lambda x : x%2==0 , l1))
print('The Result :', res)

Ex :- To get the Odd nos.

l1 = [11,12,13,14,21,22,31,55]

res = list(filter(lambda x : x%2!=0 , l1))
print('The Result :', res)

Ex :- Diviable by 5

l3 = [10,12,31,30,20,55,41]

div5 = list(filter(lambda x : x%5==0 ,l3))
print('The Divisble :', div5)



