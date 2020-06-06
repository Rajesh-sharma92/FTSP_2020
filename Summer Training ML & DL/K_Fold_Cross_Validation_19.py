# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 08:59:51 2020

@author: Rajesh
"""

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Social_Network_Ads_2.csv')

dataset.head()
********************
    User ID  Gender  Age  EstimatedSalary  Purchased
0  15624510    Male   19            19000          0
1  15810944    Male   35            20000          0
2  15668575  Female   26            43000          0
3  15603246  Female   27            57000          0
4  15804002    Male   19            76000          0


features = dataset.iloc[:,[2,3]].values

labels = dataset.iloc[:,4].values

from sklearn.model_selection import train_test_split

features_train , features_test , labels_train , labels_test =\
train_test_split(features,labels,test_size=0.25,random_state=0)
 
# Now we will be performing feature scalling coz there is more differnce between data.
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features_train = sc.fit_transform(features_train)
features_test = sc.transform(features_test)

# Now Applying KNN to this dataset.
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()

classifier.fit(features_train,labels_train)

labels_pred = classifier.predict(features_test)

# Now we will be applying the Confusion Matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(labels_test , labels_pred)

print(cm)
***********
[[64  4]
 [ 3 29]]

print((64+29)/(64+4+3+29)) # 0.93

print(classifier.score(features_train,labels_train)) # 0.91

print(classifier.score(features_test,labels_test)) # 0.93


classifier.predict([[25,10000]]) # 1
classifier.predict([[36,3000]]) # 1

# Now we will be Visualizing the Dataset.
# STEP : 1

x_min = features_train[:,0].min() - 1
x_max = features_train[:,0].max() + 1
print(x_min) # -2.99
print(x_max) # 3.166

y_min = features_train[:,1].min() - 1
y_max = features_train[:,1].max() + 1
print(y_min) # -2.58
print(y_max) # 3.33

# STEP : 2

xx , yy = np.meshgrid(np.arange(x_min,x_max,0.1) , np.arange(y_min,y_max,0.1))

print(xx.shape) # (60, 62)
print(yy.shape) # (60, 62)

# Now we have to faltten the dataset from 2D to 1D dataset.
xt = xx.ravel()
print(xt.shape) # (3720,) # 60x62 = 3720
print(xt)


# Now we have to faltten the dataset from 2D to 1D dataset.
yt = yy.ravel()
print(yt.shape) # (3720,) # 60x62 = 3720
print(yt)

# Now to make them as points, Similar to zip.
pt = np.c_[xt,yt]
print(pt.shape) # (3720, 2)
print(pt)

# To get the prediction for the new points.
z = classifier.predict(pt)
print(z.shape) # (3720,)
print(z) # [0 0 0 ... 1 1 1]

# Now we have to reshape z as xx & yy.
z = z.reshape(xx.shape)
print(z.shape) # (60, 62)


# Now we will ploting the Decision Boundary.
plt.contourf(xx,yy,z)

# Now we have to plot the new Points.
plt.plot(features_test[labels_test == 0 , 0] , features_test[labels_test == 0 , 1] ,'ro', label='class1')

plt.plot(features_test[labels_test == 1 , 0] , features_test[labels_test == 1 , 1] ,'bo', label='class2')

plt.legend()

plt.show()

print(cm)




