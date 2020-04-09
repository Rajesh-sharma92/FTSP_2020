# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:27:37 2020

@author: Rajesh
"""

Training and Testing Data :-
--------------------------
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

# Now we will using Train & Test Data set Model.
from sklearn.model_selection import train_test_split
featutres_train,featutres_test,labels_train,labels_test = train_test_split(featutres,labels,test_size=0.20,random_state=0)

# We are train/fitting od the model here.
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(featutres_train,labels_train)

labels_pred = regressor.predict(featutres_test)

# We will do the comparison between Actual & Predicated values.
df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)

   Actual    Predicated
0   32000  26215.973457
1   21000  19215.578783
2   31500  29547.629787

regressor.predict([[0,1,50000,5]]) # 28913.69215424

regressor.predict([[1,0,30000,2]]) # 41599.2410114

# Now we will check the Acurracy of the Model.
score1 = regressor.score(featutres_train,labels_train)
print(score1) # 0.9516232418974803

score2 = regressor.score(featutres_test,labels_test)
print(score2) # 0.4757986404705386






