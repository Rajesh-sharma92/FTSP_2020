# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:24:54 2020

@author: Rajesh
"""
"""
Train SVM classifier using sklearn digits dataset (i.e. from sklearn.datasets import load_digits) and then,

1) Measure accuracy of your model using different kernels such as rbf and linear.
2) Tune your model further using regularization and gamma parameters and try to come up 
    with highest accurancy score.
3) Use 80 % of samples as training data size.
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

# Now we will be separating the features & labels.
#features = digits.iloc[:,:4].values 
#labels = digits.iloc[:,4].values 

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train,labels_test = train_test_split(digits.data,digits.target,test_size=0.20,random_state=0)

# Now we will use the SVM Algorithm.
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear') # Default kernal = 'rbf'
classifier.fit(features_train,labels_train)

# How to check the Accuracy/ Score of the model.
score = classifier.score(features_test,labels_test)
print(score) # 0.9777

labels_pred = classifier.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})
print(df)
df.head()
***************
Actual  Predicated
0       2           2
1       8           8
2       2           2
3       6           6
4       6           6

# Now we will check the much percentage our model is the best.
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,labels_pred)
print(cm)
*************
[[27  0  0  0  0  0  0  0  0  0]
 [ 0 34  0  0  0  0  0  0  1  0]
 [ 0  0 36  0  0  0  0  0  0  0]
 [ 0  0  0 29  0  0  0  0  0  0]
 [ 0  0  0  0 30  0  0  0  0  0]
 [ 0  0  0  0  0 39  0  0  0  1]
 [ 0  1  0  0  0  0 43  0  0  0]
 [ 0  0  0  0  1  0  0 38  0  0]
 [ 0  1  1  0  0  0  0  0 37  0]
 [ 0  0  0  1  0  1  0  0  0 39]]

print((352)/(360)) # 0.9777

import seaborn as sn
plt.figure(figsize=(10,3))
sn.heatmap(cm,annot=True)
plt.xlabel('Predicated')
plt.ylabel('Truth')

















