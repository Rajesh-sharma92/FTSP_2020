# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 14:54:14 2020

@author: Rajesh
"""
# Here we using the KMeans Algorithms in the Unsupervised Machine Learning.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\Knowledge Shelf\KS_Machine_Learning_2020\ML_CSV\income.csv')
dataset.head()
*******************
      Name  Age  Income($)
0      Rob   27      70000
1  Michael   29      90000
2    Mohan   29      61000
3   Ismail   28      60000
4     Kory   42     150000


dataset.isnull().any(axis=0) # There is NO Missing values into dataset.

features = dataset.iloc[:,[1,2]].values

# Now we will plot the data first & check the details. 
plt.scatter(features[:,0],features[:,1])
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.title('Age & Income($) Graph')
plt.show()

from sklearn.preprocessing import MinMaxScaler
mms =  MinMaxScaler()
features  = mms.fit_transform(features)


# Fitting K-Means to the dataset using 3 clusters.
from sklearn.cluster import KMeans
# Since we have seen the visual, we have told the algo to make 3 clusters.
kmeans = KMeans(n_clusters=3)
pred_cluster = kmeans.fit_predict(features)
print(pred_cluster)
# [2 2 1 1 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 2 2 1]

dataset['Cluster'] = pred_cluster # Here we have just added to understand better.
dataset.head()
*****************
      Name  Age  Income($)  Cluster
0      Rob   27      70000        2
1  Michael   29      90000        2
2    Mohan   29      61000        1
3   Ismail   28      60000        1
4     Kory   42     150000        0



# Centroid of the clusters.
print(kmeans.cluster_centers_)

print(kmeans.cluster_centers_[:, 0]) # x 
print(kmeans.cluster_centers_[:, 1]) # y 

# How to find which points from features falls with cluster id 0 , 1 & 2.
print(pred_cluster==0)
print(len(features[pred_cluster==0])) # 7
print(len(features[pred_cluster==1])) # 11
print(len(features[pred_cluster==2])) # 4

# Now we will plot the graph & visulalize the data.
plt.scatter(features[pred_cluster == 0,0] , features[pred_cluster==0,1] , c='red' ,label='Cluster-1')
plt.scatter(features[pred_cluster == 1,0] , features[pred_cluster==1,1] , c='green' ,label='Cluster-2')
plt.scatter(features[pred_cluster == 2,0] , features[pred_cluster==2,1] , c='blue' ,label='Cluster-3')
plt.scatter(kmeans.cluster_centers_[:, 0] , kmeans.cluster_centers_[:, 1] , c='Black' ,label='Centroids' , marker='*')

# Now how to check the exactly how many clusters we need to have it here.
# Using the elbow method to find the optimal number of clusters
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
print(wcss)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Here we can see in the graph we have correct 3 clusters to divide the dataset.


    
    





