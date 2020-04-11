# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:48:10 2020

@author: Rajesh
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

iris_df['target'] = iris.target

iris_df.head() # It will take the new columns details also.

iris['target_names'] # 'setosa', 'versicolor', 'virginica'

iris_df[iris_df['target']==0].shape # (50, 5)

iris_df[iris_df['target']==0].head() # from 0 to 49 values for 'setosa'

iris_df[iris_df['target']==1].shape # (50, 5)

iris_df[iris_df['target']==2].shape # (50, 5)

# Now we want to generate new column.
iris_df['flower_name'] = iris_df['target'].apply(lambda x : iris.target_names[x])
iris_df.head()

iris_df_0 = iris_df[iris_df['target']==0]
iris_df_1 = iris_df[iris_df['target']==1]
iris_df_2 = iris_df[iris_df['target']==2]

plt.scatter(iris_df_0['sepal length (cm)'] , iris_df_0['sepal width (cm)'],color='green',marker='+')
plt.scatter(iris_df_1['sepal length (cm)'] , iris_df_1['sepal width (cm)'],color='blue',marker='+')
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.show()

plt.scatter(iris_df_0['petal length (cm)'] , iris_df_0['petal width (cm)'],color='green',marker='+')
plt.scatter(iris_df_1['petal length (cm)'] , iris_df_1['petal width (cm)'],color='blue',marker='+')
plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')
plt.show()

# Now we will be separating the features & labels.
features = iris_df.iloc[:,:4].values
labels = iris_df.iloc[:,4].values

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train,labels_test = train_test_split(features,labels,test_size=0.20,random_state=0)

# Now we will use the SVM Algorithm.
from sklearn.svm import SVC
classifier = SVC() # Default kernal = 'rbf'
classifier.fit(features_train,labels_train)

# How to check the Accuracy/ Score of the model.
score = classifier.score(features_test,labels_test)
print(score) # 1.0

labels_pred = classifier.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)
df.head()
***********
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
*************
[[11  0  0]
 [ 0 13  0]
 [ 0  0  6]]

print((11+13+6)/(11+13+6)) # 1.0

import seaborn as sn
plt.figure(figsize=(10,3))
sn.heatmap(cm,annot=True)
plt.xlabel('Predicated')
plt.ylabel('Truth')

-------------------------------------------------------------------------------------------
# If we have kernal = ploy. # ploy , rbf , linear and etc.

from sklearn.svm import SVC
classifier = SVC(kernel='poly') # Default kernal = 'rbf'
classifier.fit(features_train,labels_train)

# How to check the Accuracy/ Score of the model.
score = classifier.score(features_test,labels_test)
print(score) # 1.0

labels_pred = classifier.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)
df.head()







