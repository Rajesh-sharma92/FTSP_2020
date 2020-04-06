# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 23:02:03 2020

@author: Rajesh
"""
# Focus is on Supervised Machine Learning
# But on Classification and not Regression
# We need to predict a category and not a value in classification 
# Logistic Regression 
# K Nearest Neighbour  kNN

# Open the Heart_Disease.csv from UCI Repository 
# We are predicting his hearth Disease with 1 or 0 as the Class in last column
# There are v1 to v9 total 9 features 
# ML Algo works on the column data and it does not known what that means

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\Social_Network_Ads.csv')
dataset.head()
*******************
 Age  EstimatedSalary  Purchased
0   19            19000          0
1   35            20000          0
2   26            43000          0
3   27            57000          0
4   19            76000          0

features = dataset.iloc[:,:2].values
labels = dataset.iloc[:,2].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Fitting Logistic Regression to the Training set.
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features_train,labels_train)

# Calculate Class Probabilities
Probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix.

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)

************
[[63  3]
 [16 18]]



























