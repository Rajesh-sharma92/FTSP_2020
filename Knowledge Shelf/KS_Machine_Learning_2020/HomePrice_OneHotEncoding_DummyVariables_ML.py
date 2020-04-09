# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:26:19 2020

@author: Rajesh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\homeprices2.csv')
dataset.head()
**********
              town  area   price
0  monroe township  2600  550000
1  monroe township  3000  565000
2  monroe township  3200  610000
3  monroe township  3600  680000
4  monroe township  4000  725000

dataset.isnull().any(axis=0) # False

# dummies = pd.get_dummies(dataset['town'])

features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,[-1]].values

# Now here we have categorial values into dataset. So we need to remove all those categorials data.
from sklearn.preprocessing import LabelEncoder
le  = LabelEncoder()
features[:,0]= le.fit_transform(features[:,0])
print(features[:,0]) # [0 0 0 0 0 2 2 2 2 1 1 1 1]

# Now we will apply the One Hot Encoding technique. 
from sklearn.preprocessing import OneHotEncoder
oneHE = OneHotEncoder(categorical_features=[0])
features = oneHE.fit_transform(features).toarray()


# Now we will apply the Dummy Variables technique.
features = features[:,1:]

# Now we train/fitting of the model.
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labels)

regressor.predict([[3400,0,1]]) # 87543702.47258629


regressor.predict([[2800,1,0]]) # 72171742.63599205



