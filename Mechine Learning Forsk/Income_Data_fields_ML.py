# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 18:02:02 2020

@author: Rajesh
"""
"""
Explain the Income Data fields
Divide into features and labels with explanation 
HR Tool to offer a salary to new candidate of 15 yrs
Explain the plotting of two list with range data
Explain best fit line concept, Calculate slope and constant  
y = mx + c 
Gradient Descent concept to find best fit line
to minimise the loss or cost function
For Linear Regression the cost function = Mean Square error
its diffetent for different algorithms.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Income_Data.csv')
print(dataset)

# We know that , y = mx+c
# We need to use first we need to find the feartures(Experience) & Labels(Income).
features = dataset.iloc[:,: 1].values
labels = dataset.iloc[:,-1].values

from sklearn.linear_model import LinearRegression
regg = LinearRegression() # Object creation / Model Creation.
regg.fit(features,labels) # Trainig the model / Fitting the model.

# regg.predict(features)

regg.predict() # If we will pass the directly 12 it will through some error coz 
# it need data into numpy array form.

# regg.predict([[12]]) 139191.74805613

x = [12]
x = np.array(x)
x = x.reshape(1,1)
a = regg.predict(x)
a[0] # 139191.7480561296

x = [20]
x = np.array(x)
x = x.reshape(1,1)
a = regg.predict(x)
a[0] # 214791.4466277702

x = [4.5]
x = np.array(x)
x = x.reshape(1,1)
a = regg.predict(x)
a[0] # 68317.03064521654

plt.scatter(features,labels,color='green')
plt.plot(features,regg.predict(features),color='red')
plt.xlabel('No. of Experience')
plt.ylabel('Salaries Details')
plt.title('Experience & Salaries Graph')
plt.savefig('E:\Mechine Learning Forsk\Exp_sal.jpg')
plt.show()

























