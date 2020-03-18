# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:33:36 2020

@author: Rajesh
"""
"""
Q1. (Create a program that fulfills the following specification.)
iq_size.csv

Are a person's brain size and body size (Height and weight) predictive of his or her intelligence?

 Import the iq_size.csv file

It Contains the details of 38 students, where

Column 1: The intelligence (PIQ) of students

Column 2:  The brain size (MRI) of students (given as count/10,000).

Column 3: The height (Height) of students (inches)

Column 4: The weight (Weight) of student (pounds)

What is the IQ of an individual with a given brain size of 90, height of 70 inches, and weight 150 pounds ? 
Build an optimal model and conclude which is more useful in predicting intelligence Height, Weight or brain size.
"""

import pandas as pd
import numpy as np


dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\iq_size.csv')
print(dataset)

print(dataset.dtypes)

PIQ         int64
Brain     float64
Height    float64
Weight      int64

dataset.isnull().any(axis=0)

PIQ       False
Brain     False
Height    False
Weight    False

features = dataset.iloc[:,1:].values
labels = dataset.iloc[:,0].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
# Whether we have Univariate or Multivariate, class is LinearRegression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

# Check the value of intercept and slope
# y = ax + by + cz + d
# Here a, b and c are the coefficients and d is the intercept
print(regressor.intercept_)   
print (regressor.coef_)   
# We cannot show a line on a graph as we did for 2D data, since we have 5D data

# Predicting the Test set results
labels_pred = regressor.predict(features_test)
print(labels_pred)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)

regressor.predict([90,70,150])

x = [90,70,150]
x = np.array(x)
type(x) # numpy.ndarray
x.ndim # 1

print(x.shape) # (3,)
x = x.reshape(1,3)
print(x.shape) # (1,3)

x = regressor.predict(x)

x[0] # 105.76890364348625

NOTE :- What is the IQ of an individual with a given brain size of 125, height of 90 inches, and weight 250 pounds ? 

regressor.predict([125,90,250])

x = [125,90,250]
x = np.array(x)
type(x) # numpy.ndarray
x.ndim # 1

print(x.shape) # (3,)
x = x.reshape(1,3)
print(x.shape) # (1,3)

x = regressor.predict(x)

x[0] # 125.24323130715055
























