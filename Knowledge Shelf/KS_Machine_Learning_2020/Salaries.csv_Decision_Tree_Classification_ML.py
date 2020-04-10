# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:09:07 2020

@author: Rajesh
"""
# Decision Tree Classification :- 
---------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\salaries.csv')
dataset.head()
*******************
 company                  job     degree  salary_more_then_100k
0  google      sales executive  bachelors                      0
1  google      sales executive    masters                      0
2  google     business manager  bachelors                      1
3  google     business manager    masters                      1
4  google  computer programmer  bachelors                      0


features = dataset.drop('salary_more_then_100k' , axis=1).values
labels = dataset['salary_more_then_100k'].values

# We have the Categorial values into dataset so we need to apply the Labelencoding & Onehot.
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

features[:, 0] = le.fit_transform(features[:, 0])

features[:, 1] = le.fit_transform(features[:, 1])

features[:, 2] = le.fit_transform(features[:, 2])

# we need to onehotencoding for all these above columns.
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [2])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]

# Train and test split
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size=0.20,random_state=0)  

# Training and making predictions 
# We need to be careful in using DecissionTreeClassifier or DecissionTreeRegressor
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)


labels_pred = classifier.predict(features_test) 

# Comparing the predicted and actual values
df= pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})
df.head()
*************
   Actual  Predicted
0       0          1
1       0          0
2       0          0
3       1          0

score = classifier.score(features_test,labels_test)
print(score) # 0.50

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)
**************
[[2 1]
 [1 0]]

print((2+0)/(2+1+1+0)) # 0.5

