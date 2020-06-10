# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 17:04:23 2020

@author: Rajesh
"""

import pandas as pd

from apyori import apriori

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\BreadBasket_DMS.csv')

a = dict(dataset['Item'].value_counts())

import matplotlib.pyplot as plt

# 1) Top 15 Items are into the List

plt.pie(list(a.values())[0:15] , labels = list(a.keys())[0:15] , autopct='%1.2f%%')



# 2) To find the association of the  items where minimum support show min_confidance=0.2 , min_lift=3. 

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\BreadBasket_DMS.csv')

transactions = []
value = 1
new = []


for j,i in enumerate(dataset.iloc[:,2]):
    if i == value:
        new.append(str(dataset.values[j,3]))
        value = i
    else:
        transactions.append(new)
        new = []
        new.append(str(dataset.values[j,3]))
        value = i
        

rules = apriori(transactions,min_support=0.0025,min_confidance=0.2,min_lift=3)
print(type(rules))

results = list(rules)
print(len(results))

results[0]

results[0].items # frozenset({'Coke', 'Sandwich'})

results[3].items # frozenset({'Mineral water', 'Sandwich'})

results[0].support # 0.005141657922350472

results[0][2][0]

results[0][2][0][2] # 0.2663043478260869

results[0][2][0][3] # 3.7321771099744243



'''
# 3) Out of the Given results set , Show only names of the associated items 
# from given results row wise.

for item in results:
    pair = item[0]
    items = [x for x in pair]
    print('Rule :' + item[0] + '->' + items[1])
    
    print('support :' + str(item[1]))
    
'''

    




        












