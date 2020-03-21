# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:46:43 2020

@author: Rajesh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\caesarian.csv ')
print(dataset)

dataset.columns

['Age', 'DeliveryNumber', 'DeliveryTime', 'BloodPressure',
       'HeartProblem', 'Caesarian'],

dataset.dtypes

Age               int64
DeliveryNumber    int64
DeliveryTime      int64
BloodPressure     int64
HeartProblem      int64
Caesarian         int64

dataset.isnull().any(axis=0)

Age               False
DeliveryNumber    False
DeliveryTime      False
BloodPressure     False
HeartProblem      False
Caesarian         False


# Last column marks whether it was caesarian or not ( 1 or 0 ).
dataset.head()

  Age  DeliveryNumber  DeliveryTime  BloodPressure  HeartProblem  Caesarian
0   22               1             0              2             0          0
1   26               2             0              1             0          1
2   26               2             1              1             0          0
3   28               1             0              2             0          0
4   22               2             0              1             0          1

# Now, we need to fine out features and lables.
features = dataset.iloc[:, :-1].values

labels = dataset.iloc[:,[-1]].values

# Splitting the dataset into the Training set and Test set.
from sklearn.model_selection import train_test_split
featutes_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.25,random_state=41)

# Feature Scaling.
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
featutes_train = sc.fit_transform(featutes_train)
features_test = sc.transform(features_test)

# Fitting Logistic Regression to the Training set.
from sklearn.neighbors import KNeighborsClassifier
# When p = 1, this is equivalent to using manhattan_distance (l1), 
# and euclidean_distance (l2) for p = 2
classifier = KNeighborsClassifier(n_neighbors=5 , p=2)

classifier.fit(featutes_train,labels_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix.
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)

[[7 4]
 [2 7]]

7+7 = 14 == Right prediction
2+4 = 6 == Wrong prediction

# Model Score = 0.7  times out of 100 model prediction was RIGHT.

print((7+7)/20) # 0.7

Delivery_pred = classifier.predict([[40,4,1,2,1]])
Delivery_pred[0] # 1 --> Caesarion will be there.

# You cannot create confusion Matrix in case of Regression
# Since u cannot compare 2 continuous value







































