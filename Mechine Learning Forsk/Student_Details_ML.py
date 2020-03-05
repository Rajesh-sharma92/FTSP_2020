# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:37:46 2020

@author: Rajesh
"""
"""
# Open student_scores.csv 
# Identify which is x ( feature or independent ) and y ( label or dependent )
# This is a labelled dataset

# If Sandeep studied for 10 hours then what would be his score

# Solution 

# Since we have the x and y values, we can draw a straight line on the graph

# Then we can find the intercept and slope of the line

# after that we can apply  that on the equation y = mx + c and find the value
# of y for a specific value of x
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\student_scores.csv')

print(dataset)

dataset.count()

****** Result ****
Hours     25
Scores    25
dtype: int64

print(dataset.shape) # (25, 2)

print(dataset.ndim) # 2

print(dataset.size) # 50

print(dataset.dtypes)
**** Result *******
Hours     float64
Scores      int64
dtype: object

print(dataset.head())
**** Result *******
 Hours  Scores
0    2.5      21
1    5.1      47
2    3.2      27
3    8.5      75
4    3.5      30

print(dataset.tail())
**** Result *******
  Hours  Scores
20    2.7      30
21    4.8      54
22    3.8      35
23    6.9      76
24    7.8      86

print(dataset.describe())
**** Result *******
          Hours     Scores
count  25.000000  25.000000
mean    5.012000  51.480000
std     2.525094  25.286887
min     1.100000  17.000000
25%     2.700000  30.000000
50%     4.800000  47.000000
75%     7.400000  75.000000
max     9.200000  95.000000

# dataset.isnull().any(axis=1) # It shows all values which are null.

dataset.isnull().any(axis=0)
**** Result *******
Hours     False
Scores    False
dtype: bool

# Check for outlier values
# Also helps in finding the data distribution.
plt.boxplot(dataset.values)

# In the last example.
x  = [1,2,3,4,5]
y = [1,2,3,4,5]
plt.axis([0,6,0,6])
plt.scatter(x,y)
plt.plot(x,y)


# let's plot our data points on 2-D graph to eyeball our dataset 
# and see if we can manually find any relationship between the data. 

dataset.plot(x='Hours' , y='Scores', style='o')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.title('Hours vs Percentage')
plt.show()

# Since we have a labelled dataset
# We need to segregate the features and labels

# prepare the data to train the model.

features = dataset.iloc[ : , : -1]
print(type(features)) # <class 'pandas.core.frame.DataFrame'>
print(type(features.values)) # <class 'numpy.ndarray'>

features = dataset.iloc[ : , : -1].values
labels = dataset.iloc[ : , 1].values # To covert from DataFram to Array coz we can perform task on array only.

# Open in the Variable Explorer
type(features)
features
features.shape
features.ndim

"""
Now use a LinearRegression algorithm to 
train the model now 
"""
# import the scikit learn library to import the algorithm.
from sklearn.linear_model import LinearRegression

# Create the object of the class, which is known as MODEL
regressor = LinearRegression()

# Now we need to train the MODEL to make him learn the features and labels.
regressor.fit(features,labels)

# To see the value of the intercept and slop calculated by the linear regression 
# algorithm for our dataset, execute the following code.
print(regressor.intercept_) # 2.483673405373196
print(regressor.coef_) # [9.77580339]

# what would be prediction of score if someone studies 10 hours
# y = (m)x + (c)   where m is the slope and c is the inetrcept.

print(regressor.coef_*(10)+regressor.intercept_) # [100.24170731]

# This can also be predicted using a function.
print(regressor.predict([[10]])) # [100.24170731]

# Visualize the best fit line.
# Visualising the  results.

plt.scatter(features,labels,color='Red')
plt.plot(features,regressor.predict(features), color = 'Blue')

plt.title('Study Hours and Exam Score')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score: Marks')
plt.savefig('E:\Mechine Learning Forsk\Marks_Scores.jpg')
plt.show()

---------------------------------------------------------------------------------
NOTE :- How to Add the new values which we predicted in the dataset.

a = regressor.predict([[10]])[0]

dataset.loc[dataset.shape[0]]=[10,a]

a = regressor.predict([[11]])[0]

dataset.loc[dataset.shape[0]]=[11,a]

a = regressor.predict([[12]])[0]

dataset.loc[dataset.shape[0]] = [12,a]



plt.scatter(features,labels,color='Green')
plt.plot(features,regressor.predict(features), color = 'Red')
plt.title('Study Hours and Exam Score')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score: Marks')
plt.savefig('E:\Mechine Learning Forsk\Marks_Scores1.jpg')
plt.show()




#""""""""""" NOTES """"""""""""""

# How to save the updated CSV file into another CSV file.
dataset.to_csv('E:\Mechine Learning Forsk\Test.csv') 

dataset = dataset.drop('Hours',axis=True) # How To drop a column

dataset = dataset.drop('Scores',axis=True) # How To drop a column
















































































































