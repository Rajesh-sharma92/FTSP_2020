# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:34:29 2020

@author: Rajesh
"""
# Simple Linear Regression ( Straight Line )
# y = mx + c 

# Multiple Linear Regression ( Straight Line )
# y = ax + by + cz + d

# Polynomial Regression ( Polynomial Curve )
# y = ax² + bx + c ( Quadratic Equation )
# Feature is one only, but we have converted into different degrees, 
# multiplied by different coefficients

# Open Claims_Paid.csv
# Explain the Insurance Domain and How claims are paid
# Expalin the columns
# How much they are going to Pay in 1981 
# It seems it is a ML Problem (LR) and as the years are inc cost is inc
 
# Importing the libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Claims_Paid.csv')
print(dataset)

dataset.shape # (10,2)
dataset.ndim # 2

# Check for categorical data
dataset.dtypes

Year      int64
Cost    float64

# Check for missing data
dataset.isnull().any(axis=0)

Year    False
Cost    False

# Seperate features and labels.
features = dataset.iloc[:,[0]].values
print(features)

labels = dataset.iloc[:,[1]].values
print(labels)

#let's first analyze the data
# Visualising the Linear Regression results
# There seems to be a positive corelation between feature and labels

plt.scatter(features,labels , color='Red')

# Fitting Linear Regression to the dataset
# We can avoid splitting since the dataset is too small

# It will give an Error.
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features, labels) 

print ("Predicting result with Linear Regression")
print (regressor.predict([[1981]])) # if error we can pass as a list # 106.039

# Visualising the Linear Regression results
plt.scatter(features, labels, color = 'red')
plt.plot(features, lin_reg_1.predict(features), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Year')
plt.ylabel('Claims Paid')
plt.show()

# After seeing the visual, its sems that the predictions will be poor
# Once the years increases
# Actual line should be a polynomial line
# What should be the degree of the polynomial function 
# Its a hit and trail method and visualize it to see the curve

# We need to convert the feature(x) into 5 degree format
# Fitting Polynomial Regression to the dataset.

from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
print(features.shape)

features_poly = poly_object.fit_transform(features)
print(features_poly)
print(features_poly.shape) # (10,6) ==> # x0 x1 x2 x3 x4 x5  

from sklearn.linear_model import LinearRegression
regressor1 = LinearRegression()
regressor1.fit(features_poly,labels)

# This will give error dim1 != dim 6
# We need to convert the data into polynomial format
print(regressor1.predict(1981))

print ("Predicting result with Polynomial Regression")
print (regressor1.predict(poly_object.transform([[1981]]))) # 148.4460
# This value has huge difference from the Linear Regression 
# But if we visualize it, we will come to know that Poly is better predictions

# Visualising the Polynomial Regression results.
plt.scatter(features, labels, color = 'red')
plt.plot(features,regressor1.predict(features_poly),color='Red')
plt.title('Polynomial Regression')
plt.xlabel('Year')
plt.ylabel('Claims Paid')
plt.savefig('E:\Mechine Learning Forsk\Insurence_Cost_Polynomial_reg_Univarates')
plt.show()

# Try with different degrees = 2 and then visualize it

# Try with different degrees = 8 and then visualize it
---------------------------------------------------------------------------------------------------------------------


# What if the data is Multivariate, 
# we can then also apply Polynomial Regression
# Since in the above example we have taken Univariate dataset


# Open Salary_Classification.csv
# We used this for Multiple Linear Regression










































