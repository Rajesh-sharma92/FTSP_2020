# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:10:19 2020

@author: Rajesh
"""
# This problem is solved by KMeans Algorithm in the Unsupervised machine Learnning.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Mall_Customers.csv')

dataset.isnull().any(axis=0) # There is No empty columns.

features = dataset.iloc[:,[3,4]].values

# Now we will plot the graph for the dataset.
plt.scatter(features[:,0],features[:,1])
plt.show()

# Now we will be fitting the Model.
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5)

pred_cluster = kmeans.fit_predict(features)

plt.scatter(features[pred_cluster == 0,0], features[pred_cluster == 0,1],c='r', label='Cluster-1' )
plt.scatter(features[pred_cluster == 1,0], features[pred_cluster == 1,1],c='g', label='Cluster-2' )
plt.scatter(features[pred_cluster == 2,0], features[pred_cluster == 2,1],c='b', label='Cluster-3' )
plt.scatter(features[pred_cluster == 3,0], features[pred_cluster == 3,1],c='orange', label='Cluster-4' )
plt.scatter(features[pred_cluster == 4,0], features[pred_cluster == 4,1],c='pink', label='Cluster-5' )

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'yellow', label = 'Centroids')
plt.title('Clusters of Customers')
plt.xlabel('Annual Income(K$)')
plt.ylabel('Spending Score(1-100)')
plt.legend()
plt.show()

"""

# How to get the optimal no. of Clusters.
# wcss = With in cluster sum of square.

wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11) , wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show() 

# Here we will be having the number of clusters are 5.   

"""

