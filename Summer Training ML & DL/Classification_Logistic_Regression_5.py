# Import the Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# To Import csv file
dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Heart_Disease.csv') 

dataset.head(2)
------------------
    V1     V2    V3     V4  V5  V6     V7     V8  V9  Class
0  160  12.00  5.73  23.11   1  49  25.30  97.20  52      2
1  144   0.01  4.41  28.61   2  55  28.87   2.06  63      2


dataset.isnull().any(axis=0) # We don't have any Null values into dataset.

# To seggrating the features & lables from dataset.
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


# Now we apply the Logistic Regression to train set.
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()

classifier.fit(features_train,labels_train)

# Calculating the Probability.
probability = classifier.predict_proba(features_test)
print(probability)

# Predicting the class labesl like (0 or 1)
labels_pred = classifier.predict(features_test)

# Making Dataframe & doing the Comparison.
df = pd.DataFrame({'Actual':labels_test , 'Predicated':labels_pred})

df.head()
-------------
   Actual  Predicated
0       1           1
1       2           1
2       1           1
3       2           1
4       1           2

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(labels_test , labels_pred)

print(type(cm)) # <class 'numpy.ndarray'>

print(cm)
-------------
            1   2 Predicated
            
Actual     1  [[48 14]

           2  [15 16]]

print('Right Predication :',(48+16)) # 64

print('Wrong Predication :',(15+14)) # 29


print(64/93) # 0.68




