# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 12:01:12 2020

@author: Rajesh
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Claims_paid.csv')

dataset.head()
********************
   Year   Cost
0  1971  45.13
1  1972  51.71
2  1973  60.17
3  1974  64.83
4  1975  65.24

dataset.shape # (10, 2)

dataset.ndim # 2

dataset.dtypes # No categorial data into dataset.

# Check for missing values.
dataset.isnull().any(axis=0) # There is No Nan Values into dataset

# Now we will sepate the features & Labels.
features = dataset.iloc[:,0:1].values

labels = dataset.iloc[:,1].values

# Now Dataset is very samll so we just plot it & check it the distribution.
plt.scatter(features,labels)

# Now we will be applying the Linear Regression to dataset.
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features,labels)

# Now we will be prediction the Result.
x = regressor.predict([[1981]])
x[0] # 106.0393


# Visulazing the Linear Regression Results.
plt.scatter(features,labels,color = 'Red')
plt.plot(features,regressor.predict(features) , color = 'Black')
plt.title('Linear Regression Graph' , color = 'Purple')
plt.xlabel('Year' , color = 'Blue')
plt.ylabel('Claims paid', color = 'Green')
plt.show()
---------------------------------------------------------------------------------------


# Now we will applying the Polynomial Regression to dataset.
# We convert feature(x) into degrees like degree = 5
from sklearn.preprocessing import PolynomialFeatures
poly_object = PolynomialFeatures(degree = 5)
print(features.shape) # (10, 1)

features_poly = poly_object.fit_transform(features)
print(features_poly)
print(features_poly.shape) # (10, 6)

# Now we will be using the Linear Regression for Polynomial Regression.
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()

lin_reg.fit(features_poly,labels)

lin_reg.predict([1981])

# Now we will be Transform the features first.
x = lin_reg.predict((poly_object.transform([[1981]])))

x[0] # 148.44

# Visulazing the Linear Regression Results for the Polynomial Curve.
plt.scatter(features,labels,color = 'Red')
plt.plot(features,lin_reg.predict(poly_object.fit_transform(features)), color = 'Black')
plt.title('Polynomial Linear Regression Graph' , color = 'Purple')
plt.xlabel('Year' , color = 'Blue')
plt.ylabel('Claims paid', color = 'Green')
plt.show()


# NOTE :- Here degree values are not fix or there is No any method to calculated it.
# We just need to hit & trail kind of things we need to perform it.



