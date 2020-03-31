# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 15:04:55 2020

@author: Rajesh
"""

# https://medium.com/@jayeshbahire/lasso-ridge-and-elastic-net-regularization-4807897cb722

"""
L1 Regularization aka Lasso Regularization– This add regularization terms in the model which are function of absolute value of the coefficients of parameters. The coefficient of the paratmeters can be driven to zero as well during the regularization process. Hence this technique can be used for feature selection and generating more parsimonious model
L2 Regularization aka Ridge Regularization — This add regularization terms in the model which are function of square of coefficients of parameters. Coefficient of parameters can approach to zero but never become zero and hence
Combination of the above two such as Elastic Nets– This add regularization terms in the model which are combination of both L1 and L2 regularization.
"""

import pandas as pd
import numpy as np

# Import dataset and create a dataframe.

from sklearn import datasets

boston = datasets.load_boston()
print(boston)
print(type(boston)) # <class 'sklearn.utils.Bunch' Means Dictionary Types.

# Find out more about this dataset
print(boston.DESCR)

# Boston dataset features
boston.keys() 
***************
dict_keys(['data', 'target', 'feature_names', 'DESCR', 'filename'])

boston.data  # ( features )

boston.data.shape # (506, 13)

boston.feature_names
***********************
['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD',
       'TAX', 'PTRATIO', 'B', 'LSTAT']

boston.target  # label

boston.target.shape # (506,)

# Create a dataframe.

boston_df = pd.DataFrame(boston.data , columns = boston.feature_names)
boston_df.head()

NOTE :- Here we can see that, we have only the 0-12 means 13 features only and Lables we need to 
Add into boston_df dataset now. 

boston_df['House_Price'] = boston.target

boston_df.head()

boston_df.describe()

'''
features = boston_df.drop('House_Price',axis = 1)
labels = boston_df['House_Price']
features.head()
labels.head()
'''
features = boston_df.iloc[:,:-1].values
labels = boston_df.iloc[:,-1].values

# Create train and test data with 70o/o and 30°/o split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train,labels_test = train_test_split(features, labels, test_size=0.3, random_state=1)

features_train.shape # (354, 13)
features_test.shape # (152, 13)
labels_train.shape # (354,)
labels_test.shape # (152,)

# Let's import the Lasso, Ridge, Elasticnet regression object and define model.
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

lm = LinearRegression ()
lm_lasso = Lasso() 
lm_ridge =  Ridge() 
lm_elastic = ElasticNet() 

# Fit a model on the train data.
lm.fit(features_train,labels_train)
lm_lasso.fit(features_train,labels_train)
lm_ridge.fit(features_train,labels_train)
lm_elastic.fit(features_train,labels_train)

# Evaluate the model
import matplotlib.pyplot as plt

plt.figure (figsize= (15,10))
ft_importances_lm = pd.Series(lm.coef_, index= features.columns)
ft_importances_lm .plot(kind = 'barh')
plt.show()

# R2 Value
 
print("RSquare Value for Simple Regresssion TEST data is-")
print(np.round(lm.score(features_test,labels_test)*100,2)) # 78.36

print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lm_lasso.score(features_test,labels_test)*100,2)) # 66.95

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(features_test,labels_test)*100,2)) # 78.91

print ("RSquare Value for Elastic Net Regresssion TEST data is-")
print (np.round (lm_elastic.score(features_test,labels_test)*100,2)) # 69.98


# Predict on test and training data.

predict_test_lm = lm.predict(features_test)
predict_test_lasso = lm_lasso.predict (features_test) 
predict_test_ridge = lm_ridge.predict (features_test)
predict_test_elastic = lm_elastic.predict(features_test)

#  Print the Loss Funtion - MSE & MAE

import numpy as np
from sklearn import metrics

print ("Simple Regression Mean Square Error (MSE) for TEST data is") 
print(np.round(metrics.mean_squared_error(labels_test,predict_test_lm),2)) # 19.83

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print(np.round(metrics.mean_squared_error(labels_test,predict_test_lasso),2)) # 30.29

print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, predict_test_ridge),2)) # 19.33

print ("ElasticNet Mean Square Error (MSE) for TEST data is")
print (np.round (metrics .mean_squared_error(labels_test, predict_test_elastic),2)) # 27.51

"""
The benchmark of random guessing should get you an RMSE = standard_deviation. 
So lower than this, your model is demonstrating some ability to learn; 
above that number, you haven't even learned to guess the mean correctly.
"""



















 





