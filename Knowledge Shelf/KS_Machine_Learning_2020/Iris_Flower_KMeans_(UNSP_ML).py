# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:27:21 2020

@author: Rajesh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.datasets import load_iris

iris = load_iris()
iris_df = iris.data

iris_df = pd.DataFrame(iris.data , columns = iris.feature_names)
iris_df.head()


features = iris_df.iloc[:,[2,3]].values

# Now we will plot the data first & check the details. 
plt.scatter(features[:,0],features[:,1])
plt.xlabel('petal length(cm)')
plt.ylabel('petal width(cm)')
plt.title('Iris Flower Dataset')
plt.show()

"""
from sklearn.preprocessing import MinMaxScaler
mms =  MinMaxScaler()
features  = mms.fit_transform(features)
"""


from sklearn.cluster import KMeans
# Since we have seen the visual, we have told the algo to make 3 clusters.
kmeans = KMeans(n_clusters=2)
pred_cluster = kmeans.fit_predict(features)
print(pred_cluster)

iris_df['Cluster'] = pred_cluster # Here we have just added to understand better.
iris_df.head()

print(kmeans.cluster_centers_)

# How to find which points from features falls with cluster id 0 , 1 & 2.
print(pred_cluster==0)
print(len(features[pred_cluster==0])) # 6
print(len(features[pred_cluster==1])) # 7


# Now we will plot the graph & visulalize the data.
plt.scatter(features[pred_cluster == 0,0] , features[pred_cluster==0,1] , c='red' ,label='Cluster-1')
plt.scatter(features[pred_cluster == 1,0] , features[pred_cluster==1,1] , c='green' ,label='Cluster-2')
plt.scatter(kmeans.cluster_centers_[:, 0] , kmeans.cluster_centers_[:, 1] , c='Black' ,label='Centroids' , marker='*')
plt.legend()



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





