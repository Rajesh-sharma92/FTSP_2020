# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:27:43 2020

@author: Rajesh
"""
# Now if I want to get 100 Scores.(features=which is given in the question)
# How much hours do i need to study.(Labels=which we need to find out ?)

# Reverse the features and labels and try the model and prediction again
# You might need to reshape the features by features = featurtes.reshape(25,1)
# Now regressor.predict(100)

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\student_scores.csv')

labels = dataset.iloc[:,-2].values
features = dataset.iloc[:,1].values
features=features.reshape(25,1)
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(features,labels)

print(regressor.coef_)
print(regressor.intercept_)

print (regressor.coef_*(100) + regressor.intercept_) 

print(regressor.predict([[100]]))

# Visualising the  results
plt.scatter(features, labels, color = 'red')
plt.plot(features, regressor.predict(features), color = 'blue')
plt.title('Study Hours and Exam Score')
plt.xlabel('Exam Score: Marks')
plt.ylabel('Study Hours')
plt.savefig('E:\Mechine Learning Forsk\Student4.jpg')
plt.show()





