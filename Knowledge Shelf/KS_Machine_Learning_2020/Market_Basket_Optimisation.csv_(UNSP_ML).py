# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:08:44 2020

@author: Rajesh
"""

# Association Algorithm with Unsupervised Machine Learning.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\Market_Basket_Optimisation.csv', header =  None)

transactions = []

for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
# Now Traning on the Aporiori dataset.
from apyori import apriori
rules = apriori(transactions,min_support=0.003,min_confidence=0.25,min_lift=4)

# Visuling the results.
results = list(rules)

results[0]
****************
RelationRecord(items=frozenset({'chicken', 'light cream'}), support=0.004532728969470737, 
               ordered_statistics=[OrderedStatistic(items_base=frozenset({'light cream'}), 
              items_add=frozenset({'chicken'}), confidence=0.29059829059829057, 
              lift=4.84395061728395)])

    
    
    