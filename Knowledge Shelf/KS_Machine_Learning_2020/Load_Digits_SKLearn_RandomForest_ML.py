# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:10:43 2020

@author: Rajesh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Now we will load the dataset from sklearn.
from sklearn.datasets import load_digits

digits = load_digits()

dir(digits)
***************
['DESCR', 'data', 'images', 'target', 'target_names']

digits['data'][0] # here data column has Actual numrical values.

plt.gray()
plt.matshow(digits['images'][0]) # Images column has Actual images.

# For example if we want to print just 5 values.
plt.gray()
for i in range(5):
    plt.matshow(digits['images'][i])
    
digits['target'][0:5] # array([0, 1, 2, 3, 4])



from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(digits.data , digits.target , test_size=0.20,random_state=0)

# Now we will use the Classification model.
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(features_train,labels_train)

# Once the model is trained then we will be checking the score or accuracy of the model.
score = rf.score(features_test,labels_test)
print(score) # 0.95

# Now we will check the predicitions.
plt.matshow(digits['images'][67]) # It shows the some image value.

digits['target'][67] # 6

rf.predict([digits['data'][67]]) # 6

rf.predict(digits.data[0:5]) # [0, 1, 2, 3, 4]

labels_pred = rf.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)
df.head(10)
**************
 Actual  Predicated
0       2           2
1       8           8
2       2           2
3       6           6
4       6           6
5       7           7
6       1           1
7       9           9
8       8           8
9       5           5


# Now we will check the much percentage our model is the best.
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)
************
[[27  0  0  0  0  0  0  0  0  0]
 [ 0 34  0  0  0  1  0  0  0  0]
 [ 1  0 33  0  0  0  0  0  1  1]
 [ 0  0  0 29  0  0  0  0  0  0]
 [ 0  0  0  0 29  0  0  1  0  0]
 [ 0  0  0  1  0 38  0  0  0  1]
 [ 0  0  0  0  0  0 44  0  0  0]
 [ 0  0  0  0  0  0  0 39  0  0]
 [ 0  1  0  2  0  0  0  1 34  1]
 [ 0  0  0  2  0  1  0  1  0 37]]

print((344/360)) # 0.95

# Visualize the Confusion Matrix.
import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')










