# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 17:56:25 2020

@author: Rajesh
"""
"""
Q1. dataset: 
    pima-indians-diabetes.csv

Perform both Multinomial and Gaussian Naive Bayes classification 
after taking care of NA values (maybe replaced with zero in dataset)

Calculate accuracy for both Naive Bayes classification model.
"""
--------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

# Importing dataset
data = pd.read_csv("E:\ML Code Challenges\ML CSV Files\pima-indians-diabetes.csv")

print(data.shape) # (767, 9)

data.isnull().any(axis=0)


# Split dataset in training and test datasets
from sklearn.model_selection import train_test_split

# We have not seperated the feature and label, we have given the whole data
# thats why we only have features test and train 
# we have taken care where we are training the model in fit method
features_train, features_test =\
train_test_split(data, test_size=0.5, random_state=0)


gnb = GaussianNB()

used_features =[
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7"
]    # "8" is the column for labeleling 



# Train classifier
gnb.fit(
    features_train[used_features].values,  # features are passed
    features_train["8"].values      # labels is passed
)

labels_pred = gnb.predict(features_test[used_features])


# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_gnb = confusion_matrix(features_test["8"], labels_pred)
print(cm_gnb)
*******
[[217  36]
 [ 62  69]]


print( (cm_gnb[0][0] + cm_gnb[1][1]) / (cm_gnb[0][0] + cm_gnb[1][1] + cm_gnb[0][1] + cm_gnb[1][0]))

#Output   ---->    0.7447916666666666

-------------------------------------------------------------------------------------------------

mnb = MultinomialNB()
used_features =[
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7"
]    # "8" is the column for labeleling 
mnb.fit(
    features_train[used_features].values,
    features_train["8"].values
)
labels_pred = mnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_mnb = confusion_matrix(features_test["8"], labels_pred)
print(cm_mnb)
*********
[[182  71]
 [ 76  55]]

print( (cm_mnb[0][0] + cm_mnb[1][1]) / (cm_mnb[0][0] + cm_mnb[1][1] + cm_mnb[0][1] + cm_mnb[1][0]))

#Output   ----> 0.6171875










