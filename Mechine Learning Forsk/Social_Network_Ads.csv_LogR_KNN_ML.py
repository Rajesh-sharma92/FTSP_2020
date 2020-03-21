# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:20:15 2020

@author: Rajesh
"""
"""
Classification problem is always like drawing a decission boundary
LR is a linear Classifer, 
that means the decission boundary will always be straight line

kNN is a non linear Classifier,
that means the decission boundary will always be nonlinear in nature.

# Logistic Regression Visualisation ( Classification)
# Explain the viualisation code later
# If Sandeep age is 20 and he is earning 50000 salary, wuill he click on the ad or not ?
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Social_Network_Ads.csv')
print(dataset)

dataset.columns

dataset.dtypes

dataset.ndim # 2

dataset.isnull().any(axis=0)

# To define features & labels into dataset.
features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,[-1]].values

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

[[63  3]
 [16 18]]

63 + 18 = 81 = Right Prediction
16 + 3 = Wrong Prediction

print((63+18)/ 100) # 0.81

Ads_click = classifier.predict([[32,150000]])
Ads_click[0] # 1

Ads_click = classifier.predict([[39,59000]])
Ads_click[0] # 1

----------------------------------------------------------------------------------------------------------------------

# K-Nearest Neighbors (kNN) Visualisation 
# Explain the viualisation code later
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Social_Network_Ads.csv')
features = dataset.iloc[:, :-1].values
labels = dataset.iloc[:, [-1]].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.25, random_state = 40)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Fitting K-NN to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)

[[62  4]
 [ 4 30]]

62 + 30 =  92 = Right prediction
4 + 4 =  8 Wrong prediction 

print((62+30)/100) # 0.92

Ads_click = classifier.predict([[32,150000]])
Ads_click[0] # 1

Ads_click = classifier.predict([[39,59000]])
Ads_click[0] # 1


NOTE :- We can see that for the above problem statement , KNN is the best Regression Algorithm 
coz it is showing better results comapring to Logistics regression.

------------------------------------------------------------------------------------------------------------------------------------------
















