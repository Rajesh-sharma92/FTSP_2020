# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 10:41:02 2020

@author: Rajesh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Lanuages_growth_Year.csv')
print(dataset)

features = dataset.iloc[:, :1].values # It ontains rows & Columns in syntax.
labels = dataset.iloc[:,-1].values

"""
Now use a LinearRegression algorithm to 
train the model now 
"""

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(features,labels)

print(regressor.intercept_) # -15463.54545454546

print(regressor.coef_) # [7.69090909]

# what would be prediction of score if someone studies 2026 Year.
# y = (m)x + (c)   where m is the slope and c is the inetrcept.

print(regressor.coef_*(2026) + regressor.intercept_) # [118.23636364]

# This can also be predicted using a function 
print(regressor.predict([[2026]])) # [118.23636364]

# Visualising the  results
plt.scatter(features, labels, color = 'Blue')
plt.plot(features, regressor.predict(features), color = 'Green')
plt.title('Lanuages growth Year')
plt.xlabel('Years')
plt.ylabel('Percentage')
plt.show()






















