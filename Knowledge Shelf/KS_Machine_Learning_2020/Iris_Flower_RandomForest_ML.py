# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:28:13 2020

@author: Rajesh
"""
"""
Use famous iris flower dataset from sklearn.datasets to predict flower species using random forest classifier.

Measure prediction score using default n_estimators (10)
Now fine tune your model by changing number of trees in your classifer and tell me what 
best score you can get using how many trees.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Now we will load the dataset from sklearn.
from sklearn.datasets import load_iris

iris = load_iris()

dir(iris) # ['DESCR', 'data', 'feature_names', 'filename', 'target', 'target_names']

iris.keys()

iris.data

iris.data.shape # (150, 4)

iris.feature_names
******
['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)']

iris.target # It shows the target values like o , 1 & 2 into the all 150 rows.

iris.target.shape # (150,)

# Create a dataframe.
iris_df = pd.DataFrame(iris.data , columns = iris.feature_names)
iris_df.head()
*******************
  sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2


NOTE :- Here we can see that, we have only the 0-3 means 4 features only and Lables we need to 
Add into iris_df dataset now. 

iris_df['Plant Types'] = iris.target

iris_df.head() # It will take the new columns details also.

iris_df.describe()

features = iris_df.iloc[:,:-1].values
labels = iris_df.iloc[:,-1].values

# Create train and test data with 70o/o and 30°/o split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train,labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)

# Now we will use the Classification model.
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=20)
rf.fit(features_train,labels_train)

# Once the model is trained then we will be checking the score or accuracy of the model.
score = rf.score(features_test,labels_test)
print(score) # 1.0

labels_pred = rf.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)
df.head()
************
Actual  Predicated
0       2           2
1       1           1
2       0           0
3       2           2
4       0           0


# Now we will check the much percentage our model is the best.
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)
**************
[[11  0  0]
 [ 0 13  0]
 [ 0  0  6]]

print((11+13+6)/(11+0+0+0+13+0+0+0+6)) # 1.0


# NOTE :- Here we are getting confused with the matrix.So we will plot the graph.
import seaborn as sn
plt.figure(figsize=(5,3))
sn.heatmap(cm,annot=True)
plt.xlabel('Predicated')
plt.ylabel('Truth')

