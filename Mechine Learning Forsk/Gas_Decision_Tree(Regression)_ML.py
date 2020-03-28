# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:22:06 2020

@author: Rajesh
"""
"""
# DecissionTree for Regression

Problem Definition
The problem here is to predict the gas consumption (in millions of gallons) 
in 48 of the US states based on petrol tax (in cents), per capita income 
(dollars), paved highways (in miles) and the proportion of population with 
the driving license.
Govt to predict how much petrol to import

"""
import pandas as pd

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\petrol_consumption.csv')
# print(dataset)

dataset.head()
dataset.shape # (48, 5)

# Checking for Categorical Data.
pd.set_option('display.max_columns', None)
dataset.sample(10)

# Finding missing data.
dataset.isnull().any(axis=0)
********************************
Petrol_tax                      False
Average_income                  False
Paved_Highways                  False
Population_Driver_licence(%)    False
Petrol_Consumption              False
dtype: bool

features = dataset.drop('Petrol_Consumption',axis=1)
print(features)
print(features.shape) # (48, 4)

labels = dataset['Petrol_Consumption']
print(labels)
print(labels.shape) # (48,)

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.20,random_state=0)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(features_train,labels_train)

labels_pred = regressor.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)
*************************
 Actual  Predicated
29     534       541.0
4      410       414.0
26     577       554.0
30     571       554.0
32     577       554.0
37     704       574.0
34     487       628.0
40     587       649.0
7      467       414.0
10     580       498.0

regressor.predict([[48,4500,6200,0.65]]) # array([649.])



#Evaluating the algorithm
from sklearn import metrics

print('Mean Absolute Error:', metrics.mean_absolute_error(labels_test, labels_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(labels_test, labels_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(labels_test, labels_pred)))  
print (np.mean(labels))




























