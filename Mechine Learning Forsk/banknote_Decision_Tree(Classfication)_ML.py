# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:14:41 2020

@author: Rajesh
"""
"""
# open bill_authentication.csv 

Data Set Information:

    Data were extracted from images that were taken from 
genuine and forged banknote-like specimens. 
For digitization, an industrial camera usually used for 
print inspection was used. 
The final images have 400x400 pixels. 
Due to the object lens and distance to the 
investigated object gray-scale pictures with a 
resolution of about 660 dpi were gained. 
Wavelet Transform tool were used to extract 
features from images.
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# This is a Classification problem

dataset = pd.read_csv(r"E:\ML Code Challenges\ML CSV Files\bill_authentication.csv")  
#print(dataset)

dataset.shape # (1372, 5)
dataset.ndim # 2

# Checking for Categorical Data
# Best part is that DT and RF works on the categorical data also
# We do not need to perform the Label encoding for it, Algo does it internally 

dataset.head()
***********************
  Variance  Skewness  Curtosis  Entropy  Class
0   3.62160    8.6661   -2.8073 -0.44699      0
1   4.54590    8.1674   -2.4586 -1.46210      0
2   3.86600   -2.6383    1.9242  0.10645      0
3   3.45660    9.5228   -4.0112 -3.59440      0
4   0.32924   -4.4552    4.5718 -0.98880      0

pd.set_option('display.max_columns', None)
dataset.sample(5)
*************************
     Variance  Skewness   Curtosis  Entropy  Class
876   -3.59160  -6.22850  10.238900 -1.15430      1
244    2.42870   9.38210  -3.247700 -1.45430      0
688    2.62130   5.79190   0.065686 -1.57590      0
1018  -0.40804   0.54214  -0.527250  0.65860      1
338    0.96414   5.61600   2.213800 -0.12501      0

# Finding missing data
dataset.isnull().any(axis=0)
**************************************
Variance    False
Skewness    False
Curtosis    False
Entropy     False
Class       False

# Preparing the dataset
# This technique of dropping can be used when the label is in between features.
features = dataset.drop('Class',axis=1)
print(features)
print(features.shape) # (1372, 4)

labels = dataset['Class']
print(labels)
print(labels.shape) # (1372, 1)

# Train and test split.
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.20)

# Training and making predictions 
# We need to be careful in using DecissionTreeClassifier or DecissionTreeRegressor

from sklearn.tree import DecisionTreeClassifier

Classifier = DecisionTreeClassifier() # Object creation of the model.

Classifier.fit(features_train,labels_train) # Fitting of the model.

labels_pred = Classifier.predict(features_test)

# Comparing the predicted and actual values.
df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)

# Evaluating score
# For classification tasks some commonly used metrics are confusion matrix, 
# precision, recall, and F1 score.

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)
*******************
[[151   5]
 [  3 116]]

print((151+116)/(275)) # 0.9709090909090909

# Model Score = 98.90 times out of 100 model prediction was RIGHT
print( (cm[0][0] + cm[1][1]) / (cm[0][0] + cm[1][1] + cm[0][1] + cm[1][0])) # 0.9709090909090909

#Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(labels_test,labels_pred))  
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred))












































