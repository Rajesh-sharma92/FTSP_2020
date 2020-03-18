# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:50:42 2020

@author: Rajesh
"""
"""
Q2. (Create a program that fulfills the following specification.)
Female_Stats.Csv
Female Stat Students

 Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

1) Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
2) When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
3) When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.

"""
"""
1) Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not.
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Female_Stats.csv')
print(dataset)

dataset.dtypes

Height       float64
momheight    float64
dadheight    float64


dataset.isnull().any(axis=0)
Height       False
momheight    False
dadheight    False

1) Build A Predictive Model And Conclude If Both Predictors(Independent Variables) 
Are Significant For A Students’ Height Or Not.

features = dataset.iloc[:,1:].values
labels = dataset.iloc[:,0].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

# Fitting Multiple Linear Regression to the Training set
# Whether we have Univariate or Multivariate, class is LinearRegression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)


labels_pred = regressor.predict(features_test)

# df = pd.DataFrame(zip(labels_pred,labels_test))
df = pd.DataFrame({'Actual':labels_test,'Predicated':labels_pred})
print(df)

print(regressor.predict([[75,75]]))  # [70.59058003]

print(regressor.predict([[65,95]]))  # [75.57843766]

------------------------------------------------------------------------------------------------------------------------------------
"""
2) When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
"""

import pandas as pd
import numpy as np

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Female_Stats.csv')
print(dataset)

dataset.dtypes
dataset.isnull().any(axis=0)

features = dataset.iloc[:,[1]].values
labels = dataset.iloc[:,[0]].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

# Fitting Multiple Linear Regression to the Training set
# Whether we have Univariate or Multivariate, class is LinearRegression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(features_train,labels_train)


labels_pred = regressor.predict(features_test)

print(pd.DataFrame(zip(labels_pred,labels_test)))

# df = pd.DataFrame(zip(labels_pred,labels_test))
#df1 = pd.DataFrame({'Actual':labels_test,'Predicated':labels_pred})
#print(df1)

----------------------------------------------------------------------------------------------------------------------------
"""
3) When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.
"""
import pandas as pd
import numpy as np

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Female_Stats.csv')
print(dataset)

dataset.dtypes
dataset.isnull().any(axis=0)

features = dataset.iloc[:,[2]].values
labels = dataset.iloc[:,[0]].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state=0)

# Fitting Multiple Linear Regression to the Training set
# Whether we have Univariate or Multivariate, class is LinearRegression

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(features_train,labels_train)


labels_pred = regressor.predict(features_test)

print(pd.DataFrame(zip(labels_pred,labels_test)))






