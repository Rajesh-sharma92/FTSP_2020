# We are using the Apriori Algorithm 

import pandas as pd

from apyori import apriori

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Market_Basket_Optimisation.csv',header=None)

transactions = [] # Empty List

for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    

# Training Apriori on Dataset.
rules = apriori(transactions , min_support = 0.003 , min_confidence = 0.25 , min_lift = 4)

print(type(rules)) # <class 'generator'>

# Visualising the results.
results = list(rules)
print(len(results))   # 30

# How to find out the Association now.

results[0] 

results[25]    

# What are Generators in Python ?
# To get the square of those all elements from list.

list1 = [1,2,3,4,5]

[i*i for i in list1] # List Comprehension
 # [1, 4, 9, 16, 25]

# How to use Generators 
 
q =  (i*i for i in list1)

print(type(q)) # <class 'generator'>

print(q) # <generator object <genexpr> at 0x000000000D0DE4C8>

next(q) # 1 

next(q) # 4
 
next(q) # 9

next(q) # 16

next(q) # 25

next(q) # It will throw an Exception coz just 5 elements into list.




