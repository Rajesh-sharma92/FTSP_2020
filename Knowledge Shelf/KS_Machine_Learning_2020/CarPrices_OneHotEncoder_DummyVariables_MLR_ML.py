# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:37:32 2020

@author: Rajesh
"""
"""
1) Predict price of a mercedez benz that is 4 yr old with mileage 45000
2) Predict price of a BMW X5 that is 7 yr old with mileage 86000
3) Tell me the score (accuracy) of your model. (Hint: use LinearRegression().score())
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\carprices.csv')
dataset.head()
********
  Car Model  Mileage  Sell Price($)  Age(yrs)
0    BMW X5    69000          18000         6
1    BMW X5    35000          34000         3
2    BMW X5    57000          26100         5
3    BMW X5    22500          40000         2
4    BMW X5    46000          31500         4

featutres = dataset.drop('Sell Price($)' , axis = 'columns').values

labels = dataset['Sell Price($)'].values

# Now we will be checking like Categorial data or not.
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
featutres[:,0] = le.fit_transform(featutres[:,0])
print(featutres[:,0]) # [1 1 1 1 1 0 0 0 0 2 2 2 2]

# One Hot Encoding.
from sklearn.preprocessing import OneHotEncoder
oneHE = OneHotEncoder(categorical_features = [0])
featutres = oneHE.fit_transform(featutres).toarray()
print(featutres)

# Dummy Trap Variables. 
featutres = featutres[:,1:]
print(featutres)

# Everything is fine and we can train / fitting of our model.
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(featutres,labels)

BMW X5 = 0
Audi A5 = 1
Merceds Benz = 2

BMW X5   Audi A5    Merceds Benz
1           0           0
0           1           0
0           0           1


# Price of mercedez benz that is 4 yr old with mileage 45000
regressor.predict([[0,1,45000,4]]) # 36991.31721062

# Price of BMW X5 that is 7 yr old with mileage 86000
regressor.predict([[1,0,86000,7]]) # 11080.74313219

# Price of Audi A5 that is 8 yr old with mileage 75000
regressor.predict([[1,0,75000,8]]) # 13819.63254285

# Now we check the Accuracy or score of the model.
score = regressor.score(featutres,labels)
print('The Accuracy :', score)

# The Accuracy : 0.9417050937281083


