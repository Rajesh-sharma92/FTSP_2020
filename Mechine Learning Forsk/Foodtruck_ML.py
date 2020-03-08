# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:24:46 2020

@author: Rajesh
"""

"""
Code Challenge
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Foodtruck.csv')
print(dataset)

dataset.columns
Index(['Population', 'Profit'], dtype='object')

features = dataset.iloc[:,:1].values
labels = dataset.iloc[:,1].values

from sklearn.linear_model import LinearRegression
regg = LinearRegression() # Model creation / Object creation.

regg.fit(features,labels) # Traing of the model / fitting of the model.

# regg.predict([[3.073]]) # array([-0.22958849])

x = [3.073]
x = np.array(x)
x = x.reshape(1,1)
a = regg.predict(x)
a[0] # -0.22958849

---------------------------------------------------------------------
If the jaipur city population is more then ?
x = [13.073]
x = np.array(x)
x = x.reshape(1,1)
a = regg.predict(x)
a[0] # 11.700747952178707

-----------------------------------------------------------------------------------------------------------------------
NOTE :- We will be training half module & testing also and then what will be the result ?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('E:\ML Code Challenges\ML CSV Files\Foodtruck.csv')
print(dataset)

dataset.columns
Index(['Population', 'Profit'], dtype='object')

features = dataset.iloc[:,:1].values
labels = dataset.iloc[:,1].values

from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.3,random_state=41)

from sklearn.linear_model import LinearRegression
regg = LinearRegression() # Model creation / Object creation.

regg.fit(features_train,labels_train)

labels_pred = regg.predict(features_test)

df = pd.DataFrame({'Actual':labels_test,'Predicated':labels_pred})
print(df)

************ Result **************
  Actual  Predicated
0    0.55657    2.271225
1    6.79810    6.737876
2    7.20290    2.820249
3    4.34830    4.720999
4    5.70140    1.832764
5    2.05760    1.917047
6    1.84510    2.627298
7   17.59200    3.103639
8    3.08250    2.458258
9    7.54350    7.434514
10   5.74420    5.690137
11   7.04670    8.841166
12  12.13400    6.818371
13  13.66200    5.954706
14   3.88450    4.794629
15   1.01730    2.380722
16  22.63800   18.296975
17   1.84950    2.845226
18   1.98690    2.151074
19   4.60420    2.546803
20   0.92695    2.975676
21   8.00430    9.720693
22   1.27840    2.980648
23   5.16940    6.317881
24   3.65180    3.481848
25   1.42330    3.367261
26   6.75260    8.032663
27   0.15200    2.405581
28  12.00000    6.025139
29   3.39280    2.507265

----------------------------------------------------------------------------------
# We will plot the graph of these values.

plt.scatter(features_test,labels_test,color='pink')
#plt.plot(features_test,regg.predict(features_test),color='orange')
plt.plot(features_train,regg.predict(features_train),color='skyblue')
plt.xlabel('Total Population')
plt.ylabel('Total Profit')
plt.title('Population & Profit Graph')
plt.savefig('E:\Mechine Learning Forsk\Food_Truck.jpg')
plt.show()


















































































