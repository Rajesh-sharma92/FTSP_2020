# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:13:50 2020

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
from sklearn.linear_model import LogisticRegression
le = LogisticRegression()
le.fit(features_train,labels_train)

# Once the model is trained then we will be checking the score or accuracy of the model.
score = le.score(features_test,labels_test)
print(score) # 0.95

# Now we will check the predicitions.
plt.matshow(digits['images'][67]) # It shows the some image value.

digits['target'][67] # 6

le.predict([digits['data'][67]]) # 6

le.predict(digits.data[0:5]) # [0, 1, 2, 3, 4]

labels_pred = le.predict(features_test)

# Now we will check the much percentage our model is the best.
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)
**************
[[27  0  0  0  0  0  0  0  0  0]
 [ 0 31  0  0  0  0  1  0  3  0]
 [ 0  0 34  2  0  0  0  0  0  0]
 [ 0  0  0 29  0  0  0  0  0  0]
 [ 0  0  0  0 30  0  0  0  0  0]
 [ 0  0  0  0  0 39  0  0  0  1]
 [ 0  1  0  0  0  0 43  0  0  0]
 [ 0  1  0  0  1  0  0 37  0  0]
 [ 0  2  1  0  0  0  0  0 35  1]
 [ 0  0  0  1  0  1  0  0  2 37]]



# NOTE :- Here we are getting confused with the matrix.So we will plot the graph.
import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm,annot=True)
plt.xlabel('Predicated')
plt.ylabel('Truth')













