# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:28:10 2020

@author: Rajesh
"""
# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Wine.csv')

# Explain the features
# label is the customer categorories ( 1,2,3) who will like the wine
features = dataset.iloc[:,:13].values
labels = dataset.iloc[:,13].values

# If new wine is launched, which category of customer would like it
# We can visualise only 2D dataset, but we have 13D dataset.
# which would be difficult to visualize and draw the decission boundary
# Solution to it is convertion from 13D to 2D data

# df_features = pd.DataFrame(features)
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

"""
13D Data to 2D dataset 
Convoluton of 13D data, if has not removed any features, 
but have created two new features PC1 and PC2 which has 
some weightage of all the 13 features
"""

# Applying PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)

features_train = pca.fit_transform(features_train)
features_test = pca.transform(features_test)

# How much is the loss and how much we are able to retain the information.
explained_variance = pca.explained_variance_ratio_
print(explained_variance) # [0.36884109 0.19318394]

# first paramater (PC1) is holding 36% of the 13D data
# second parameter (PC2) is holding 19% of the 13D data

# Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
print(cm)
------------
[[14  0  0]
 [ 1 15  0]
 [ 0  0  6]]

# 3 Segmentation of the Customers 
# With 56% reduced data, we are still able to get good score of prediction 

# After reduction of data, still there is good prediction 
# We should have compared this with 13D data
print( (cm[0][0] + cm[1][1]) / (cm[0][0] + cm[1][1] + cm[0][1] + cm[1][0]))
# 0.9666666666666667

# Visualising the Test set results
x_min, x_max = features_train[:, 0].min() - 1, features_train[:, 0].max() + 1
y_min, y_max = features_train[:, 1].min() - 1, features_train[:, 1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))
# Obtain labels for each point in mesh using the model.
# ravel() is equivalent to flatten method.
# data dimension must match training data dimension, hence using ravel
Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

# Plot the points, we have three labels (1,2,3)
plt.plot(features_test[labels_test == 1, 0], features_test[labels_test == 1, 1], 'ro', label='Class 1')
plt.plot(features_test[labels_test == 2, 0], features_test[labels_test == 2, 1], 'go', label='Class 2')
plt.plot(features_test[labels_test == 3, 0], features_test[labels_test == 3, 1], 'bo', label='Class 3')

#plot the decision boundary
plt.contourf(xx, yy, Z, alpha=.5)

plt.show()
print(cm)

# How will i come to know, that in PC1 and PC2, which features from 13D
# has its percentage 

# Dump components relations with features:
df_features = pd.DataFrame(features)
df_pca =  pd.DataFrame(pca.components_,columns=df_features.columns,index = ['PC-1','PC-2'])
print(df_pca)
# 

PC-1  0.129600 -0.244641 -0.010189  ...  0.307105  0.376362  0.281109
PC-2 -0.498073 -0.231685 -0.314969  ...  0.271617  0.160712 -0.365473

