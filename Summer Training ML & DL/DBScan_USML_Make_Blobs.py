import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets.samples_generator import make_blobs

# To Generate the Sample Data.
centers = [[1,1],[-1,-1],[1,-1]]
features , labels = make_blobs(n_samples=750 , centers = centers , cluster_std=0.4 , random_state=0)

print(features)
print(labels)

plt.scatter(features[:,0] , features[:,1])
plt.show()

# Now we will be applyingf the Standard Scaling.
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

features = sc.fit_transform(features)

# Now we will be applying the db Scan Algorithm.
from sklearn.cluster import DBSCAN

db = DBSCAN(eps=0.3 , min_samples=10)
db.fit(features)


labels_pred = db.labels_

print(labels_pred)

# Now we will plot the Graph.
plt.scatter(features[labels_pred == 0,0] , features[labels_pred == 0,1] , c='r' ,marker='+', label = 'Cluster1')
plt.scatter(features[labels_pred == 1,0] , features[labels_pred == 1,1], c='g' ,marker='o' ,label = 'Cluster2')
plt.scatter(features[labels_pred == 2,0] , features[labels_pred == 2,1], c='b' ,marker='s', label = 'Cluster3')
plt.scatter(features[labels_pred == -1,0] , features[labels_pred == -1,1], c='y' ,marker='*', label = 'Noise')
plt.legend()                   
                       
plt.title('Clusters of DataPoints')                      
plt.xlabel('X Coordinates')
plt.ylabel('Y Coordinates')
plt.show()


# NOTE :- Actually, we don't any kind of Centroids here in the DBSCAN but in any case if need to 
# u can take like this.

features[labels_pred == 0]

print(len(features[labels_pred == 0])) # 243

np.mean(features[labels_pred == 0 , 0]) # 0.61

np.mean(features[labels_pred == 0 , 1]) # 1.32




