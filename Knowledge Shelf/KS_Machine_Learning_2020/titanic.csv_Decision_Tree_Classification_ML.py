# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 17:32:10 2020

@author: Rajesh
"""
"""
Build decision tree model to predict survival based on certain parameters

In this file using following columns build a model to predict if person would survive or not,
1) Pclass
2) Sex
3) Age
4) Fare
Calculate score of your model
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
0       0          0
1       0          0
2       0          0
3       1          1
4       1          0

score = classifier.score(features_test,labels_test)
print(score) # 0.7877094972067039

from sklearn.metrics import confusion_matrix 
cm = confusion_matrix(labels_test,labels_pred)
print(cm)
***********
[[96 14]
 [24 45]]

Right Prediction = 96+45 : 141
Wrong prediction = 14+24 : 38    

Total values = 141+38 = 179

print((141/179)) # 0.7877094972067039

# Now we will be doing some of the predictions.

classifier.predict([[1,3,45,250]]) # 0 

classifier.predict([[1,1,20,500]]) # 1

classifier.predict([[1,2,99,150]]) # 0 

classifier.predict([[0,1,15,450]]) # 1 


