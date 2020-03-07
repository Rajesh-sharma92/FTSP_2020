# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 21:52:26 2020

@author: Rajesh
"""

# Now explain the random state by pring features_test with and without random state set.
import numpy as np

X,y = np.arange(10).reshape(5,2),list(range(5))

print(type(X)) # <class 'numpy.ndarray'>

print(type(y)) # <class 'list'>

print(X)

[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]

print(y)

[0, 1, 2, 3, 4]

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_label = train_test_split(X,y,test_size=0.33)

from sklearn.linear_model import LinearRegression

regg = LinearRegression()
regg.fit(X_train,y_train)

labels_pred = regg.predict(X_test)

import pandas as pd

df = pd.DataFrame({'Actual':y_label,'Predicaated':labels_pred})
print(df)

********* Result ***********

Actual  Predicaated
0       3          3.0
1       2          2.0

-----------------------------------------------------------------------------------------------------------
# If you use random_state=some_number, 
# then you can guarantee that your split will be always the same. 
# This is useful if you want reproducible results, 
# I would say, set the random_state to some fixed number while you test stuff, 
# but then remove it in production if you need a random (and not a fixed) split.



from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

print (X_train)

[[4 5]
 [0 1]
 [6 7]]

print (X_test)

[[2 3]
 [8 9]]

print (y_train)
[2, 0, 3]

print (y_test)
[1, 4]


from sklearn.linear_model import LinearRegression

regg = LinearRegression()
regg.fit(X_train,y_train)

labels_pred = regg.predict(X_test)

import pandas as pd

df = pd.DataFrame({'Actual':y_label,'Predicaated':labels_pred})
print(df)

********* Result ***********
Actual  Predicaated
0       3          1.0
1       2          4.0
--------------------------------------------------------------------------------------------------------------
# This result would be different from last one, but if you run it again and again it will be same

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=100)

print (X_train)
print (X_test)

print (y_train)
print (y_test)

from sklearn.linear_model import LinearRegression

regg = LinearRegression()
regg.fit(X_train,y_train)

labels_pred = regg.predict(X_test)

import pandas as pd

df = pd.DataFrame({'Actual':y_label,'Predicaated':labels_pred})
print(df)

********* Result ***********
  Actual  Predicaated
0       3          1.0
1       2          2.0
-------------------------------------------------------------------------------------

# Model accuracy
print (regg.score(X_test, y_test)) # 1.0
print (regg.score(X_train, y_train)) # 1.0



# Now lets talk about two terms - overfitting and underfitting the data


# Do we have case of underfitting?
# Do we have case of overfitting?




































