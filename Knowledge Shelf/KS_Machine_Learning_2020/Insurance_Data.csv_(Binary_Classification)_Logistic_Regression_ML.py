# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 19:34:30 2020

@author: Rajesh
"""
# Here we need to check what ages type of people are buying the Life Insurance.
# Yes = 1 & No = 0

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\insurance_data.csv')
dataset.head()
*****************
  age  bought_insurance
0   22                 0
1   25                 0
2   47                 1
3   52                 0
4   46                 1


featutres = dataset.iloc[:,:1].values

labels = dataset.iloc[:,1].values


# Now we will using Train & Test Data set Model.
from sklearn.model_selection import train_test_split
featutres_train,featutres_test,labels_train,labels_test = train_test_split(featutres,labels,test_size=0.25,random_state=0)

# We are train/fitting od the model here.It is classfication problem.
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(featutres_train,labels_train)

#Calculate Class Probabilities
# Open in variable explorer and show ( FAIL and PASS probability)
# There are two probabilities since we have 2 class
probability = classifier.predict_proba(featutres_test)
print(probability)


# Predicting the class labels ( 0 or 1 )
labels_pred = classifier.predict(featutres_test)

# Comparing the predicted and actual values
df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)
****************
  Actual  Predicated
0       1           1
1       1           1
2       1           1
3       1           1
4       1           1
5       0           0
6       1           1


# Making the Confusion Matrix or Error Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)
********
[[1 0]
 [0 6]]

print((1+6)/(1+6+0+0)) # 1.0

Right Prediction = 1 + 6 = 7
Wrong Prediction = 0 + 0 = 0

print('The Right Accuray of Model :', (7/7))
# The Right Accuray of Model : 1.0

score1 = classifier.score(featutres_train,labels_train)
print(score1) # 0.85

score2 = classifier.score(featutres_test,labels_test)
print(score2) # 1.0

# Now we will be predicting the some new values.

x = classifier.predict([[20]])
print(x[0]) # 0


x = classifier.predict([[40]])
print(x[0]) # 1


x = classifier.predict([[60]])
print(x[0]) # 1


x = classifier.predict([[99]])
print(x[0]) # 1

