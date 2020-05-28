# Import the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To Import csv file
dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\caesarian.csv') 

dataset.head()
-------------------
   Age  DeliveryNumber  DeliveryTime  BloodPressure  HeartProblem  Caesarian
0   22               1             0              2             0          0
1   26               2             0              1             0          1
2   26               2             1              1             0          0
3   28               1             0              2             0          0
4   22               2             0              1             0          1


dataset.isnull().any(axis=0) # There is No Nan Valeus into dataset.

features = dataset.iloc[:,:-1].values

labels = dataset.iloc[:,-1].values


from sklearn.model_selection import train_test_split

features_train , features_test , labels_train , labels_test =\
train_test_split(features,labels,test_size=0.2,random_state=41)

# Now we do the Feature Scaling here with features_train.
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

features_train = sc.fit_transform(features_train)

# Now we have already calculated the mean & SD then just do the transform only.
features_test = sc.transform(features_test)

# Fitting Logistics Regression to the Train set data.
from sklearn.neighbors import KNeighborsClassifier

# We are not mentioning k & p values then by default it will be taking the k = 5 , p = 2
# p = 2 means Equaliden distance , p = 1 menas Manhattan distance.
classifier = KNeighborsClassifier(n_neighbors = 5 , p = 2)

classifier.fit(features_train,labels_train)


# Calculating the Probability.
probability = classifier.predict_proba(features_test)
print(probability)

# Predicting the class labesl like (0 or 1)
labels_pred = classifier.predict(features_test)

# Making Dataframe & doing the Comparison.
df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})

df.head()

# To make the Confusion Matrix.
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(labels_test , labels_pred)

print(cm)
----------------
[[7 2]
 [2 5]]


print(12/16) # 0.75






