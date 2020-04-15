# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 16:09:48 2020

@author: Rajesh
"""

K Fold Cross Validation :- 
------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
digits = load_digits()

# We will do the Train & Test and Spliting the dataset.

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = \
train_test_split(digits.data , digits.target,test_size=0.30)

# Logistic Regression 
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(features_train,labels_train)


first time = lr.score(features_test,labels_test) # 0.9648148148148148
second time = lr.score(features_test,labels_test) # 0.987037037037037

# Support Vector Machine(SVM)
from sklearn.svm import SVC
svc = SVC()
svc.fit(features_train,labels_train)

first time = svc.score(features_test,labels_test) # 0.49444444444444446
second time =  svc.score(features_test,labels_test) # 0.825925925925926


# Random Forest 
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(features_train,labels_train)

first time = rf.score(features_test,labels_test) # 0.9425925925925925
second time =  rf.score(features_test,labels_test) # 0.9777777777777777

# NOTE :- We can see that in the above all the results are changing every time for the 
# every iteration like running again & again.

# Now we will be uisng the KFold Algorithm.
from sklearn.model_selection import KFold
kf = KFold(n_splits=3)
print(kf) # KFold(n_splits=3, random_state=None, shuffle=False)

for features_index,labels_index in kf.split([1,2,3,4,5,6,7,8,9]):
    print(features_index,labels_index)

-------------
[3 4 5 6 7 8] [0 1 2]
[0 1 2 6 7 8] [3 4 5]
[0 1 2 3 4 5] [6 7 8]    
    














