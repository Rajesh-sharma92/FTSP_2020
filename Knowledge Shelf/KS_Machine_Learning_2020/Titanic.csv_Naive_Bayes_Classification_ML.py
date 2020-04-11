# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:29:22 2020

@author: Rajesh
"""
"""
Naive Bayes flavour ( variants )
    1. Gaussian     ( for continuous data like numerical )
    2. Bernolli     ( for discrete values like 0 or 1 )
    3. Multinomial  ( for text data like NLP )
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv(r'E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\titanic.csv')

dataset.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns',inplace=True)
dataset.head()
***************
   Survived  Pclass     Sex   Age     Fare
0         0       3    male  22.0   7.2500
1         1       1  female  38.0  71.2833
2         1       3  female  26.0   7.9250
3         1       1  female  35.0  53.1000
4         0       3    male  35.0   8.0500


dataset.isnull().any(axis=0)

age_mean = dataset['Age'].mean()

dataset.fillna(age_mean ,inplace=True)

dataset.isnull().any(axis=0)

features = dataset.drop('Survived', axis = 1).values
labels = dataset['Survived'].values

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
features[:, 1] = le.fit_transform(features[:, 1])

# we need to onehotencoding for all these above columns.
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [1])
features = onehotencoder.fit_transform(features).toarray()

# Dummy Trap. 
features = features[:, 1:]

# Train and test split
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size=0.20,random_state=0)  

# Now we will be using the Naive Bayes Algorithms & We have GussainNB.
from sklearn.naive_bayes import GaussianNB
gb = GaussianNB()
gb.fit(features_train,labels_train)

labels_pred = gb.predict(features_test)

# Comparing the predicted and actual values
df= pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})
df.head()
*************
  Actual  Predicted
0       0          0
1       0          0
2       0          0
3       1          1
4       1          1

score = gb.score(features_test,labels_test)
print(score) # 0.7877094972067039

from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(labels_test,labels_pred)
print(cm)
***********
[[87 23]
 [16 53]]

print((87+53)/(87+23+16+53)) # 0.7877094972067039

# Now we will be doing some of the predictions.

gb.predict([[1,3,45,250]]) # 1

gb.predict([[1,1,20,500]]) # 1

gb.predict([[1,2,99,150]]) # 1

gb.predict([[0,1,15,450]]) # 1 

--------------------------------------------------------------------------------------------
# Now we will be using the Naive Bayes Algorithms & We have GussainNB.
from sklearn.naive_bayes import  BernoulliNB, MultinomialNB
br = BernoulliNB()
br.fit(features_train,labels_train)

labels_pred = br.predict(features_test)

# Comparing the predicted and actual values
df= pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})
df.head()


score = br.score(features_test,labels_test)
print(score) # 0.7877094972067039

from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(labels_test,labels_pred)
print(cm)
**********
[[92 18]
 [20 49]]

print((92+49)/(92+18+20+49)) # 0.7877094972067039


