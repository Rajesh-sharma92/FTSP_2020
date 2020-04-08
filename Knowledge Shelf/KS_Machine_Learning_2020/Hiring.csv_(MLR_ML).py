# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:49:23 2020

@author: Rajesh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\hiring.csv')
dataset.head()
*****
  experience  test_score(out of 10)  interview_score(out of 10)  salary($)
0        NaN                    8.0                           9      50000
1        NaN                    8.0                           6      45000
2       five                    6.0                           7      60000
3        two                   10.0                          10      65000
4      seven                    9.0                           6      70000

dataset.isnull().any(axis=0)
***********
experience                     True
test_score(out of 10)          True
interview_score(out of 10)    False
salary($)                     False

ts_median = dataset['test_score(out of 10)'].median() # 8.0

dataset['test_score(out of 10)'].fillna(ts_median ,inplace = True)
dataset.head()

from word2number import w2n
"""
print(w2n.word_to_num("two million three thousand nine hundred and eighty four")) # 2003984

print(w2n.word_to_num('two point three'))  # 2.3
"""
dataset['experience'].fillna('zero' , inplace=True)
dataset.head()
********
  experience  test_score(out of 10)  interview_score(out of 10)  salary($)
0       zero                    8.0                           9      50000
1       zero                    8.0                           6      45000
2       five                    6.0                           7      60000
3        two                   10.0                          10      65000
4      seven                    9.0                           6      70000

dataset['experience'] = dataset['experience'].apply(w2n.word_to_num)
dataset.head()
*******************
 experience  test_score(out of 10)  interview_score(out of 10)  salary($)
0           0                    8.0                           9      50000
1           0                    8.0                           6      45000
2           5                    6.0                           7      60000
3           2                   10.0                          10      65000
4           7                    9.0                           6      70000


# Now we will sepated the features & labels.
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,[-1]].values

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labels)

# Now we will predicate the some of questions.
x = regressor.predict([[2,9,6]])
print(x[0]) # 53205.96797671


x = regressor.predict([[12,10,10]])
print(x[0]) # 92002.18340611


