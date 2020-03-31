# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:09:59 2020

@author: Rajesh
"""
"""
Code Challenges
Code Challenge 01: (Prostate Dataset) Prostate_Cancer.csv
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delimiter =' ')

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""


import pandas as pd
import numpy as np

dataset = pd.read_csv('http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat', delimiter = ' ')
dataset.head()
****************
     lcavol   lweight  age      lbph  svi       lcp  gleason  pgg45      lpsa
1 -0.579818  2.769459   50 -1.386294    0 -1.386294        6      0 -0.430783
2 -0.994252  3.319626   58 -1.386294    0 -1.386294        6      0 -0.162519
3 -0.510826  2.691243   74 -1.386294    0 -1.386294        7     20 -0.162519
4 -1.203973  3.282789   58 -1.386294    0 -1.386294        6      0 -0.162519
5  0.751416  3.432373   62 -1.386294    0 -1.386294        6      0  0.371564

dataset.shape # (97, 9)
dataset.ndim # 2


features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.25,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)


labels_pred = regressor.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)

df.shape # (25, 2)

df.head()
************
     Actual  Predicated
0  1.800058    1.856926
1  3.587677    2.606893
2 -0.162519    0.455392
3  2.718001    2.911489
4  2.962692    1.307735

(a) Can we predict lpsa from the other variables ?

x = regressor.predict([[4.5,4.0,70,0.50,1,3.0,5,40]])
x[0] # 4.381407995240034

# Evaluate the Algorithm.
from sklearn import metrics

print('Mean Squared Error :', metrics.mean_squared_error(labels_test,labels_pred))
# Mean Squared Error : 0.44437009898432345

# Model accuracy ( you can swap features and labels passing).
print(regressor.score(features_test,labels_test)) # 0.6300727970070961

print(regressor.score(features_train,labels_train)) # 0.6591300587436444

# (2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge  # RidgeClassier is also there

lm = LinearRegression ()
lm_lasso = Lasso() 
lm_ridge =  Ridge() 

# Fit a model on the train data
lm.fit(features_train, labels_train)
lm_lasso.fit(features_train, labels_train)
lm_ridge.fit(features_train, labels_train)

predict_test_lm =	lm.predict(features_test ) 
predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)


import numpy as np
from sklearn import metrics

print ("Simple Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lm),2) ) # 0.44

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_lasso),2)) # 1.04

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2)) # 0.44










