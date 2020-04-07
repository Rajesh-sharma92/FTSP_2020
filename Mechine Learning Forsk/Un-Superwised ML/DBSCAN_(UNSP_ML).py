# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:07:51 2020

@author: Rajesh
"""
"""
DbSCAN ( Density Based and not centroid based )
"""
"""
Open the Webpage
https://www.naftaliharris.com/blog/visualizing-k-means-clustering/
How to pick the initial centroids?  == Randomly
What kind of data would you like?   == Smiley Face
Take clusters as 3 
Follow all the steps to update the centroid

Data in not uniformly distributed, there should be 4 clusters, 
but kMeans will give different clusters

kMeans is good when the data is uniformly distributed

DBSCAN is good for non uniformly distributed data. 
It does not uses centroid concept, but uses density based concept

https://www.naftaliharris.com/blog/visualizing-dbscan-clustering/
Explain the animation for minimum_samples and epsilon, 
There should be minimum samples in the circle drawn with epsilon radius
Apply recursion for the points within the circle and the proces goes on...
Noise are those points which are not part of any cluster, it gives -1


Now the actual explanation of the algorithm !!
https://www.naftaliharris.com/blog/visualizing-dbscan-clustering/
Uniform points

DbSCAN is a recursive type of algorithm
[ within radius = 1(epsilion) and has minpoints = 4 ]
It has shown a lot of rings, but only those rings are RED when is satisfying
the condition of radius = 1 and minpoints = 4

It start randomly from any point
Then it decides at what minimum points should i decide its a cluster now
Lets assume we have set the minimum points as 4
Within certain area if there are 4 points, then there will be a cluster

For the distance we use another parameter epsilion radius
Within the radius of 1 otherwise it will not be cluster
It is showing in RED only those rings which are stasifying our both conditoins

For each point in the RED ... 
it tries to calcuate the next cluster within our 2 conditions 

This recursion goes on
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]  # 3 ---> 0 1 2 

# make_blobs generates random points from any point from a list
# by default it gives 2 features, 

features , labels = make_blobs(n_samples=750,centers=centers,cluster_std=0.4,random_state=0)
print(features)
print(labels)

plt.scatter(features[:,0],features[:,1])
plt.show()

features = StandardScaler().fit_transform(features)
# Scatter all these data points on the matplotlib
plt.scatter(features[:,0],features[:,1])
plt.show()


# Compute DBSCAN

db = DBSCAN(eps=0.5,min_samples=10).fit(features)

labels_pred = db.labels_ # belongs to which cluster id
print(labels_pred)

# Now plot the graph.
plt.scatter(features[labels_pred == 0,0], features[labels_pred == 0,1],c='r', marker='+' )
plt.scatter(features[labels_pred == 1,0], features[labels_pred == 1,1],c='g', marker='o' )
plt.scatter(features[labels_pred == 2,0], features[labels_pred == 2,1],c='b', marker='s' )
plt.scatter(features[labels_pred == -1,0],features[labels_pred == -1,1],c='y', marker='*' )

--------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler

features , labels = make_blobs(n_samples=1350,cluster_std=0.10)
print(features)
print(labels)

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()



features = StandardScaler().fit_transform(features)

#Scatter all these data points on the matplotlib
plt.scatter(features[:,0], features[:,1])
plt.show()


# Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(features)
#core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
#core_samples_mask[db.core_sample_indices_] = True

labels_pred = db.labels_ # belongs to which cluster id

print(labels_pred)

# Plot result
import matplotlib.pyplot as plt


plt.scatter(features[labels_pred == 0,0], features[labels_pred == 0,1],c='r', marker='+' )
plt.scatter(features[labels_pred == 1,0], features[labels_pred == 1,1],c='g', marker='o' )
plt.scatter(features[labels_pred == 2,0], features[labels_pred == 2,1],c='b', marker='s' )
plt.scatter(features[labels_pred == -1,0],features[labels_pred == -1,1],c='y', marker='*' )



















