# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:50:41 2020

@author: Rajesh
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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\Salary_Classification.csv')
dataset.head()
****************
   Department  WorkedHours  Certification  YearsExperience  Salary
0  Development         2300              0              1.1   39343
1      Testing         2100              1              1.3   46205
2  Development         2104              2              1.5   37731
3           UX         1200              1              2.0   43525
4      Testing         1254              2              2.2   39891


features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1]

dataset.isnull().any(axis=0)
*************************
Department         False
WorkedHours        False
Certification      False
YearsExperience    False
Salary             False

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder

# Create objct of LabelENcoder
labelencoder = LabelEncoder()

# Fit and Use the operation Transform
features[:, 0] = labelencoder.fit_transform(features[:, 0])

print(features)

# Development = 0
# Testing = 1
# UX = 2


from sklearn.preprocessing import OneHotEncoder

# Creation of Object
onehotencoder = OneHotEncoder(categorical_features = [0])

# Convert to NDArray format
features = onehotencoder.fit_transform(features).toarray()
# OneHotEncoder always puts the encoded values as the first columns
# irrespective of the column you are encoding

print(features)

# Development = 1 0 0
# Testing = 0 1 0
# UX = 0 0 1

# Avoiding the Dummy Variable Trap
# dropping first column
features = features[:, 1:]
# Now our data is ready for Modelling 



# Now sklearn has new way of using Transformer
# Pandas has pd.get_dummies(dataset) will directly OneHotEncode your data
# Pandas always adds the encoded columns as the last columns

# If there is a new column of Qualification which has B.Tech, M.Tech, Ph.D values
# Then we DO NOT need to OneHotEncode the column, only Label Encoding is required
# Since we do not require to remove the ORDERING issue


# Splitting the dataset into the Training set and Test set.
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.20,random_state=0)

# Fitting Multiple Linear Regression to the Training set
# Whether we have Univariate or Multivariate, class is LinearRegression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)

labels_pred = regressor.predict(features_test)

df = pd.DataFrame({'Actual':labels_test,'Predicated':labels_pred})
df.head()
**************
    Actual     Predicated
2    37731   43891.269027
28  122391  126961.498814
13   57081   62010.545521
10   63218   61270.231965
26  116969  112780.993053

# Getting Score for the Multi Linear Reg model
Score1 = regressor.score(features_train, labels_train)
print(Score1) # 0.9479557005187084

Score2 = regressor.score(features_test, labels_test)
print(Score2) # 0.9823026784845371
 
"""
If the training score is POOR and test score is POOR then its underfitting
If the training score is GOOD and test score is POOR then its overfitting
"""
# Prediction for a new values for a person in 'Development', hours worked 1150,
# 3 certificates , 4yrs of experience. What would be his salary ??

# Predicting the Test set results
Pred = regressor.predict(features_test)

import pandas as pd
import numpy as np
print (pd.DataFrame(zip(Pred, labels_test)))


# Prediction for a new values for a person in 'Development', hours worked 1150,
# 3 certificates , 4yrs of experience. What would be his salary ??


regressor.predict(['Development',1150,3,4])
# This will throw error of Expected 2D Array but got 1D Array 



x = ['Development',1150,3,4]

print(type(x))
x = np.array(x)
print(type(x))

print(x.shape)
x = x.reshape(1,4) # x.reshape(1,-1)
print(x.shape)


regressor.predict(x)
# This again throws error, cannot cast array data from float to x32
# Since it requires 5 columns but you are passing only 4 columns

 
# make this according to the data csv format
# We need to OneHotEncode the data
# Development is replaced by 1,0,0 to 0,0 to remove dummy trap

x = [1,0,0,1150,3,4]
x = np.array(x)
x = x.reshape(1,4)
regressor.predict(x)
# Again we will get error



# We need to remove the dummy trap also
# Development 1,0,0 to be replaced by 0,0 to remove dummy trap

x = [0,0,1150,3,4]
x = np.array(x)
x = x.reshape(1,5)
regressor.predict(x) # 62362.1437168












