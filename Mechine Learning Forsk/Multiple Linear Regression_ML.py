# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:14:09 2020

@author: Rajesh
"""

"""
# Open Salary_Classification.csv
# Teach how to read the dataset 
# Sandeep is working in the Development Department, 
# have worked for 1000 hours
# Has 1 Certificate and have 2 years experience
# Now predict the salary for Sandeep ??
# Which are the features and labels ??
# So there are 4 features and 1 Label ( Multivariate Data)

# Multiple Linear Regression

"""

Multiple Linear Regression :- 
--------------------------

import pandas as pd
import numpy as np

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Salary_Classification.csv')
print(dataset)

# To Check the columns Name.
dataset.columns
==> 
Index(['Department', 'WorkedHours', 'Certification', 'YearsExperience',
       'Salary'],
      dtype='object').
           

# To Check the data Types.
print(dataset.dtypes)
==> 
Department          object
WorkedHours          int64
Certification        int64
YearsExperience    float64
Salary               int64
dtype: object

NOTE :- Here we can se that all the columns have integer values apart from 
Department column.

# NDArray 
# Introduce the concept of Categorical and Numerical Data Types
temp = dataset.values
print(temp)

type(dataset) # pandas.core.frame.DataFrame

type(temp) # numpy.ndarray

# Seperate Features and Labels.
features = dataset.iloc[ : , : -1].values
labels = dataset.iloc[ : , -1].values

# Check Column wise is any data is missing or NaN.
dataset.isnull().any(axis=0)

Department         False
WorkedHours        False
Certification      False
YearsExperience    False
Salary             False
dtype: bool

NOTE :- In the above line we can understand if axis=0 means that we are checking 
any columns value is Nan.

# For applying Regression Algorithm, it is mandatory that there should not be
# any Categorial Data in the dataset
# Decission Tree and Random Forest Algo can take Categorical Data

# Converting your categorical data to Numerical Data is known as Label Encoding

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder

# Create objct of LabelENcoder
labelencoder = LabelEncoder()

# Fit and Use the operation Transform
features[:,0] = labelencoder.fit_transform(features[:,0])
print(features)

# Development = 0
# Testing = 1
# UX = 2
# There is a problem in Label Encoding, our algo would understand 
# that UX has more preference/priority than Testing and Development
# or reverse 0 is high priority
# So there is a ORDER Generation after Label Encoding 
# So there should be a solution to fix it

# Show One_hot_encoding_colors.png
# Calculate the unique values in Column
# Create new columns for each unique value
# Is your value is equal to Column Name, make it 1 .. others 0
 
# Show One_hot_encoding_week_days.png

# This way of representation of data is known as One Hot Encoding

from sklearn.preprocessing import OneHotEncoder

# Creation of Object
onehotencoder = OneHotEncoder(categorical_features=[0])

# Convert to NDArray format
onehotencoder.fit_transform(features).toarray()
# OneHotEncoder always puts the encoded values as the first columns
# irrespective of the column you are encoding

print(features)

# Development = 1 0 0
# Testing = 0 1 0
# UX = 0 0 1

# Now sklearn has new way of using Transformer
# Pandas has pd.get_dummies(dataset) will directly OneHotEncode your data
# Pandas always adds the encoded columns as the last columns

# If there is a new column of Qualification which has B.Tech, M.Tech, Ph.D values
# Then we DO NOT need to OneHotEncode the column, only Label Encoding is required
# Since we do not require to remove the ORDERING issue

# If we know the values of first two columns, then can we know the value in third col
# That means one column out of three is redundant
# And its value is dependent on the other columns
# Predictions will be poor if there are redundant columns in dataset
# This problem is known as Dummy Variable Trap
# We can drop any one column to solve this problem 
# We should have singularity in the dataset and not have redundancy

 

# Avoiding the Dummy Variable Trap
# dropping first column
features = features[ : , 1:]
# Now our data is ready for Modelling .

# Splitting the dataset into the Training set and Test set.
from sklearn.model_selection import train_test_split
features_train , features_test , labels_train , labels_test = train_test_split(features, labels , test_size=0.2 , random_state=0)

# Fitting Multiple Linear Regression to the Training set
# Whether we have Univariate or Multivariate, class is LinearRegression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)

# Check the value of intercept and slope
# y = ax + by + cz + d
# Here a, b and c are the coefficients and d is the intercept
print(regressor.intercept_)   
print (regressor.coef_)   # we will have 5 values since we have 5 columns (5dimension)
# We cannot show a line on a graph as we did for 2D data, since we have 5D data

# Predicting the Test set results.
labels_pred = regressor.predict(features_test)

df = pd.DataFrame({'Actual':labels_test,'Predicted':labels_pred})
print(df)

# Prediction for a new values for a person in 'Development', hours worked 1150,
# 3 certificates , 4yrs of experience. What would be his salary ??

regressor.predict(['Development',1150,3,4])

x = ['Development',1150,3,4]

print(type(x))
x = np.array(x)
print(type(x))

print(x.shape)
x = x.reshape(1,4) # x.reshape(1,-1)
print(x.shape)


regressor.predict(x)

x = [1,0,0,1150,3,4]
x = np.array(x)
x = x.reshape(1,4)
regressor.predict(x)
# Again we will get error


# This again throws error, cannot cast array data from float to x32
# Since it requires 5 columns but you are passing only 4 columns

 
# make this according to the data csv format
# We need to OneHotEncode the data
# Development is replaced by 1,0,0 to 0,0 to remove dummy trap

x = [0,0,1150,3,4]
x = np.array(x)
x = x.reshape(1,5)
x = regressor.predict(x)
x[0] # 62362.14371687774

# General Way of solving the above problem
le = labelencoder.transform(['Development'])
print(le)
# le = labelencoder.transform(['Testing'])
# print(le)
# le = labelencoder.transform(['UX'])
# print(le)
# le = labelencoder.transform(['CSE'])
# print(le)

ohe = onehotencoder.transform(le.reshape(1,1)).toarray()
print(ohe)
x = [ohe[0][1],ohe[0][2],1150,3,4]

x = np.array(x)
x = x.reshape(1, -1)
x = regressor.predict(x)
x[0] # 62362.14371687774

"""
x = np.array(columnTransformer.transform(x), dtype = np.float32)
x = x[:,1:]
regressor.predict(x)
"""


# Getting Score for the Multi Linear Reg model
Score = regressor.score(features_train, labels_train)
Score = regressor.score(features_test, labels_test)


"""
If the training score is POOR and test score is POOR then its underfitting
If the training score is GOOD and test score is POOR then its overfitting
"""























           
           

