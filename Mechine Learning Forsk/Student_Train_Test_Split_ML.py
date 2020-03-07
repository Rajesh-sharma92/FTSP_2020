# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 12:29:26 2020

@author: Rajesh
"""
# A faculty in your college teaches you Data Structure
# How does the faculty EVALUATES that how much have you understood that 
# he has explained or TRAINED you
# How well your Brain is trained WELL or BAD is EVALUATED
# TEST or EXAM is the way to EVALUATE it

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\student_scores.csv')
print(dataset)

features = dataset.iloc[: , : -1].values
labels = dataset.iloc[: , 1]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features , labels, test_size = 0.2 , random_state = 41)

from sklearn.linear_model import LinearRegression
reggressor = LinearRegression()

reggressor.fit(features_train,labels_train)

labels_pred = reggressor.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicted':labels_pred})
print(df)

*************** Result *********
  Actual  Predicted
5       20  15.964757
19      69  74.613283
14      17  11.988585
10      85  77.595411
7       60  55.726469

---------------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\student_scores.csv')
print(dataset)

features = dataset.iloc[: , : -1].values
labels = dataset.iloc[: , 1]

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features , labels, test_size = 0.4 , random_state = 41)

from sklearn.linear_model import LinearRegression
reggressor = LinearRegression()

reggressor.fit(features_train,labels_train)

labels_pred = reggressor.predict(features_test)

df = pd.DataFrame({'Actual':labels_test , 'Predicted':labels_pred})
print(df)

*************** Result *********
  Actual  Predicted
5       20  15.996489
19      69  73.865675
14      17  12.073154
10      85  76.808176
7       60  55.229835
8       81  82.693178
17      24  19.919823
11      62  59.153170
15      95  88.578180
9       25  27.766493



















