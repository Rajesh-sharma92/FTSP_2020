# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:46:52 2020

@author: Rajesh
"""

import pandas as pd
dataset = pd.read_csv('E:/Knowledge Shelf/csv Files/Salary_Classification.csv' , squeeze = True)
print(dataset)

dataset.head()
*********************
   Department  WorkedHours  Certification  YearsExperience  Salary
0  Development         2300              0              1.1   39343
1      Testing         2100              1              1.3   46205
2  Development         2104              2              1.5   37731
3           UX         1200              1              2.0   43525
4      Testing         1254              2              2.2   39891

dataset.count()
***********************
Department         30
WorkedHours        30
Certification      30
YearsExperience    30
Salary             30
dtype: int64

len(dataset) # 30 ; NOTE :- It is almost same like count() function but it shows over all length of every row.

dataset.sum()
************************
Department         DevelopmentTestingDevelopmentUXTestingUXDevelo...
WorkedHours                                                    51425
Certification                                                     62
YearsExperience                                                159.4
Salary                                                       2280090

dataset.mean()
*************
WorkedHours         1714.166667
Certification          2.066667
YearsExperience        5.313333
Salary             76003.000000
dtype: float64

(dataset.sum())/( dataset.count())
******************************************
WorkedHours         1714.166667
Certification          2.066667
YearsExperience        5.313333
Salary             76003.000000

dataset.std()
******************************************
WorkedHours          480.554068
Certification          1.112107
YearsExperience        2.837888
Salary             27414.429785

dataset.min()
******************************************
Department         Development
WorkedHours               1000
Certification                0
YearsExperience            1.1
Salary                   37731

dataset.max()
******************************************
Department             UX
WorkedHours          3000
Certification           4
YearsExperience      10.5
Salary             122391


dataset['Salary'].min() # 37731

dataset['Salary'].max() # 122391

dataset.median()
*********************
WorkedHours         1520.0
Certification          2.0
YearsExperience        4.7
Salary             65237.0

----------------------------------------------------------------------------------------------

"""
.idxmax(), .idxmin() Methods in Pandas  :- 
--------------------------------------
"""
import pandas as pd
dataset = pd.read_csv('E:/Knowledge Shelf/csv Files/Salary_Classification.csv')
# print(dataset)

dataset.head()
*********************
   Department  WorkedHours  Certification  YearsExperience  Salary
0  Development         2300              0              1.1   39343
1      Testing         2100              1              1.3   46205
2  Development         2104              2              1.5   37731
3           UX         1200              1              2.0   43525
4      Testing         1254              2              2.2   39891

NOTE :- If we are using squeeze = True , or not but there will be the same result as earlier.

dataset.max()
*********************
Department             UX
WorkedHours          3000
Certification           4
YearsExperience      10.5
Salary             122391

dataset.min()
************************
Department         Development
WorkedHours               1000
Certification                0
YearsExperience            1.1
Salary                   37731


dataset['Salary'].idxmax() # 28

dataset['Salary'].idxmin() # 2

dataset['Salary'][28] # 122391

dataset['Salary'][2] # 37731

dataset['Certification'].idxmax() # 22

dataset['Certification'].idxmin() # 0

dataset['Certification'][22] # 4

dataset['Certification'][0] # 0

NOTE :- Here we can use these above codes like this also.

dataset['Certification'][dataset['Certification'].idxmax()] # 4

dataset['Salary'][dataset['Salary'].idxmax()] # 122391




































