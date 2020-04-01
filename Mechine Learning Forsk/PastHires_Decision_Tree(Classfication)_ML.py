# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:56:51 2020

@author: Rajesh
"""
"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv

Here, we are building a decision tree to check if a person is hired or not 
based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.
"""

import pandas as pd

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\PastHires.csv')
print(dataset)

dataset.shape # (13, 7)

dataset.ndim # 2

dataset.head()
*********************
   Years Experience Employed?  ...  Interned Hired
0                10         Y  ...         N     Y
1                 0         N  ...         Y     Y
2                 7         N  ...         N     N
3                 2         Y  ...         N     Y
4                20         N  ...         N     N

[5 rows x 7 columns]

pd.set_option('display.max_columns', None)
dataset.sample(10)

"""
features = dataset.iloc[:,:-1]
labels = dataset.iloc[:,-1].values
"""

# Checking for Categorical Data
# Best part is that DT and RF works on the categorical data also
# We do not need to perform the Label encoding for it, Algo does it internally 
dataset.head()
pd.set_option('display.max_columns', None)
dataset.sample(10)


# Finding missing data
dataset.isnull().any(axis=0)
**********************************
Years Experience      False
Employed?             False
Previous employers    False
Level of Education    False
Top-tier school       False
Interned              False
Hired                 False



# Preparing the dataset
# This technique of dropping can be used when the label is in between features
features = dataset.drop('Hired', axis=1)
features = features.values

# Label Encoding for Features

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

#For Column --->  Employed?
features[:, 1] = labelencoder.fit_transform(features[:, 1])

#For Column --->  Level of Education
features[:, 3] = labelencoder.fit_transform(features[:, 3])

#For Column --->  Top-tier school
features[:, 4] = labelencoder.fit_transform(features[:, 4])

#For Column --->  Interned.
features[:, 5] = labelencoder.fit_transform(features[:, 5])


# we need to onehotencoding for all these above columns.
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [3])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]


# Label Encoding for Features
labels = dataset['Hired']  
labels = labels.values

#For Column --->  Hired
labels = labelencoder.fit_transform(labels)



# Train and test split
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size=0.20)  

# Training and making predictions 
# We need to be careful in using DecissionTreeClassifier or DecissionTreeRegressor
from sklearn.tree import DecisionTreeClassifier  
classifier = DecisionTreeClassifier()  
classifier.fit(features_train, labels_train)


labels_pred = classifier.predict(features_test) 

# Comparing the predicted and actual values
my_frame= pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})
print(my_frame)
**********************
  Actual  Predicted
0       1          1
1       1          0
2       0          0


# Evaluating score
# For classification tasks some commonly used metrics are confusion matrix, 
# precision, recall, and F1 score.
from sklearn.metrics import confusion_matrix  
cm = confusion_matrix(labels_test, labels_pred)
print(cm)   # 0.6666666666666666

*******************
[[1 0]
 [1 1]]

# Model Score = 100% times out of 100 model prediction was RIGHT
print((cm[0][0] + cm[1][1]) / (cm[0][0] + cm[1][1] + cm[0][1] + cm[1][0]))


# Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(labels_test,labels_pred))  
***********
[[1 0]
 [1 1]]

print(classification_report(labels_test,labels_pred))  
***********
  precision    recall  f1-score   support

           0       0.50      1.00      0.67         1
           1       1.00      0.50      0.67         2

    accuracy                           0.67         3
   macro avg       0.75      0.75      0.67         3
weighted avg       0.83      0.67      0.67         3

print(accuracy_score(labels_test, labels_pred)) # 0.6666666666666666


# So we have here for decision Tree

----------------------------------------------------------------------------------------------------------------

# Now we will take Random Forest and solve it
"""
Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to 
    top-tire school, having Bachelor's Degree without Internship.
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\PastHires.csv')

#data analysis
dataset.shape

# Checking for Categorical Data
# Best part is that DT and RF works on the categorical data also
# We do not need to perform the Label encoding for it, Algo does it internally 

dataset.head()
pd.set_option('display.max_columns', None)
dataset.sample(10)


# Finding missing data
dataset.isnull().any(axis=0)


# Preparing the dataset
# This technique of dropping can be used when the label is in between features
features = dataset.drop('Hired', axis=1)
features = features.values


# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

#For Column --->  Employed?
features[:, 1] = labelencoder.fit_transform(features[:, 1])

#For Column --->  Level of Education
features[:, 3] = labelencoder.fit_transform(features[:, 3])

#For Column --->  Top-tier school
features[:, 4] = labelencoder.fit_transform(features[:, 4])

#For Column --->  Internet
features[:, 5] = labelencoder.fit_transform(features[:, 5])


#we need to onehotencoding for this column
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [3])
features = onehotencoder.fit_transform(features).toarray()
features = features[:, 1:]


# Label Encoding for Features
labels = dataset['Hired']  
labels = labels.values

#For Column --->  Hired
labels = labelencoder.fit_transform(labels)


# Train and test split
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size=0.20)


# Train the model
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators=10, random_state=0)  
classifier.fit(features_train, labels_train)  


# Now we will predict with some data that this employe will Hired or not?
# so our features = [0,0,10,1,4,1,0]
 
labels_pred = classifier.predict([[0,0,10,1,4,1,0]]) 

# we predict that Employee will be hired -->array([1])


"""

Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any 
top-tire school, having Master's Degree with Internship. 

[1,0,10,0,4,0,1]

"""
labels_pred = classifier.predict([[1,0,10,0,4,0,1]])   

# we predict that Employee will be hired -->array([1])


























