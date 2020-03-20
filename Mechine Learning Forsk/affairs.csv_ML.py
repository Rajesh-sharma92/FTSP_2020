# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:41:14 2020

@author: Rajesh
"""
"""
Code Challenges
Q1. (Create a program that fulfills the following specification.)
affairs.csv

Import the affairs.csv file.

It was derived from a survey of women in 1974 by Redbook magazine, in which married women were asked about their participation in extramarital affairs.

Description of Variables

The dataset contains 6366 observations of 10 variables:(modified and cleaned)

rate_marriage: woman's rating of her marriage (1 = very poor, 5 = very good)

age: women's age
yrs_married: number of years married

children: number of children

religious: women's rating of how religious she is (1 = not religious, 4 = strongly religious)

educ: level of education (9 = grade school, 12 = high school, 14 = some college,
 16 = college graduate, 17 = some graduate school, 20 = advanced degree)

occupation: women's occupation (1 = student, 2 = farming/semi-skilled/unskilled, 
3 = "white collar", 4 = teacher/nurse/writer/technician/skilled, 5 = managerial/business, 6 = professional with advanced degree)

occupation_husb: husband's occupation (same coding as above)

affair: outcome 0/1, where 1 means a woman had at least 1 affair.

Now, perform Classification using logistic regression and check your model accuracy using confusion matrix and also through .score() function.

NOTE: Perform OneHotEncoding for occupation and occupation_husb, since they should be treated as categorical variables. Careful from dummy variable trap for both!!
What percentage of total women actually had an affair?

(note that Increases in marriage rating and religiousness correspond to a decrease in the likelihood of having an affair.)

Predict the probability of an affair for a random woman not present in the dataset. She's a 25-year-old teacher who graduated college, has been married for 3 years, has 1 child, rates herself as strongly religious, rates her marriage as fair, and her husband is a farmer.
Optional
Build an optimum model, observe all the coefficients.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'E:\ML Code Challenges\ML CSV Files\affairs.csv')
print(dataset)

dataset.columns

dataset.shape # (6366,9)
dataset.ndim # 2

# There is no Categorical Data
dataset.head()
dataset.sample(5)


# There is no Missing Data
# Check Column wise is any data is missing or NaN
dataset.isnull().any(axis=0) # All coulmns are False.

# Lets seperate the features and labels from the data 
features = dataset.iloc[:,0:-1].values

labels = dataset.iloc[:,[-1]].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)

# He has already calculated the mean and sd, so we only need to transform
features_test = sc.transform(features_test)

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train, labels_train)


# Predicting the class labels ( 0 or 1 )
labels_pred = classifier.predict(features_test)

# Comparing the predicted and actual values
my_frame= pd.DataFrame(labels_pred, labels_test)
print(my_frame)

# Now we can draw 4 combination 
# I predicted 1 , Acutal was also 1  ( RIGHT PREDICTION ) True positives (TP)
# I predicted 2,  Actual was also 2  ( RIGHT PREDICTION ) True negatives (TN)

# I predicted 1 , Acutal was also 2  ( WRONG PREDICTION ) False positives (FP)
# I predicted 2,  Actual was also 1  ( WRONG PREDICTION ) False negatives (FN)

# We represent this type of information in form of Matrix


# Making the Confusion Matrix or Error Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)
"""
[[989 111]
 [314 178]]


989 + 178  ( RIGHT PREDICTION )
314 + 111 ( WRONG PREDICTION )
"""
# Model Score = 75.86 times out of 100 model prediction was RIGHT

print( (989.0 + 178.0) / 1592.0) # 0.7330402010050251

-------------------------------------------------------------------------------------------------------------------------------
"""2) To Check the Score Function :- """
---------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'E:\ML Code Challenges\ML CSV Files\affairs.csv')
print(dataset)

#Lets seperate the features and labels from the data 
features = dataset.iloc[:,0:-1].values

labels = dataset.iloc[:,[-1]].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,labels_train)

labels_pred = regressor.predict(features_test)

df = pd.DataFrame({'Actual':labels_test,'Predicated':labels_pred})
print(df)

score1 = regressor.score(features_train,labels_train)
print(score1) # 0.16022026866729655

score2 = regressor.score(features_test,labels_test)
print(score2) # 0.16059470161905953

-----------------------------------------------------------------------------------------------------------------------------
"""
Predict the probability of an affair for a random woman not present in the dataset. 
She's a 25-year-old teacher who graduated college, has been married for 3 years, 
has 1 child, rates herself as strongly religious, rates her marriage as fair, 
and her husband is a farmer Optional.
"""


labels_pred = classifier.predict([[4,25,3,1,4,16,4,2]])
labels_pred[0]

# 0 means There is No affair.


# Define p Value ?
# p value is a  Probability that says your column by chance 
# has come in the decission making process
    


# add code to automate the p value removing
import statsmodels.api as sm
import numpy as np

features_obj = features[:, [0,1,2,3,4,5,6,7]]
features_obj = sm.add_constant(features_obj)
while (True):
    regressor_OLS = sm.OLS(endog = labels,exog =features_obj).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.0001 :
        features_obj = np.delete(features_obj, p_values.argmax(),1)
    else:
        break
















 




















