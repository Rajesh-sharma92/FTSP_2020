# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:03:29 2020

@author: Rajesh
"""
import pandas as pd

from sklearn.datasets import load_wine
wine = load_wine()

wine.data[0:2]

wine.feature_names # It shows the all features names.

df = pd.DataFrame(wine.data , columns = wine.feature_names)

df['target']= wine.target # # It will take the new columns details also.

wine['target_names'] # ['class_0', 'class_1', 'class_2']

df['Wine_Type'] = df['target'].apply(lambda x : wine.target_names[x])

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
train_test_split(wine.data, wine.target, test_size=0.3, random_state=0)

from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
mnb.fit(features_train,labels_train)

labels_pred = mnb.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)
df.head()
************
   Actual  Predicated
0       0           0
1       2           2
2       1           1
3       0           0
4       1           1

score = mnb.score(features_test,labels_test)
print(score) # 0.8703703703703703

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)
*************
[[17  1  1]
 [ 1 19  2]
 [ 1  1 11]]

print((17+19+11)/(17+1+1+1+19+2+1+1+11)) # 0.8703703703703703

----------------------------------------------------------------------------------------------

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(features_train,labels_train)

labels_pred = gnb.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)
df.head()
************
   Actual  Predicated
0       0           0
1       2           2
2       1           1
3       0           0
4       1           1

score = gnb.score(features_test,labels_test)
print(score) # 0.9444444444444444

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)
*************
[[19  0  0]
 [ 2 19  1]
 [ 0  0 13]]

print((19+19+13)/(19+0+0+2+19+1+0+0+13)) # 0.9444444444444444

