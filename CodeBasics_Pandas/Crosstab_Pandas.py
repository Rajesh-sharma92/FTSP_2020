# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:36:25 2020

@author: Rajesh
"""

import pandas as pd

df = pd.read_excel('E:\CodeBasics_Pandas\Pandas_CSV_CB\survey.xls')

df.head()
-------------
     Name Nationality     Sex  Age Handedness
0   Kathy         USA  Female   23      Right
1   Linda         USA  Female   18      Right
2   Peter         USA    Male   19      Right
3    John         USA    Male   22       Left
4  Fatima   Bangadesh  Female   31       Left


# We will use the cross tab here.
pd.crosstab(df.Nationality , df.Handedness) # It is also correct line.

pd.crosstab(df['Nationality'],df['Handedness']) # It is also correct line.
------------------
Handedness   Left  Right
Nationality             
Bangadesh       2      0
China           2      1
India           2      1
USA             1      3

# If we want to know that how many males & females are which Handed.
pd.crosstab(df['Sex'],df['Handedness']) 
------------
Handedness  Left  Right
Sex                    
Female         2      3
Male           5      2

# Here we can get the total count of the male & females into dataset.
pd.crosstab(df['Sex'],df['Handedness'] , margins=True) 
-----------
Handedness  Left  Right  All
Sex                         
Female         2      3    5
Male           5      2    7
All            7      5   12

# If we want to get the details as per the Countries wise Handed.
pd.crosstab(df.Sex , [df.Handedness , df.Nationality],margins=True) # It is also correct line.
--------------
Handedness       Left                 Right           All
Nationality Bangadesh China India USA China India USA    
Sex                                                      
Female              1     1     0   0     1     0   2   5
Male                1     1     2   1     0     1   1   7
All                 2     2     2   1     1     1   3  12


pd.crosstab([df.Nationality ,df.Sex] , df.Handedness ,margins=True) # It is also correct line.
--------------
Handedness          Left  Right  All
Nationality Sex                     
Bangadesh   Female     1      0    1
            Male       1      0    1
China       Female     1      1    2
            Male       1      0    1
India       Male       2      1    3
USA         Female     0      2    2
            Male       1      1    2
All                    7      5   12

# Now we will come to our Original Dataframes.
pd.crosstab(df.Sex , df.Handedness , margins=True)

Handedness  Left  Right  All
Sex                         
Female         2      3    5
Male           5      2    7
All            7      5   12


# If we want to get the percentage.
pd.crosstab(df.Sex , df.Handedness , normalize=True)
----------
Handedness      Left     Right
Sex                           
Female      0.166667  0.250000
Male        0.416667  0.166667

pd.crosstab(df.Sex , df.Handedness , normalize='index')
-----------
Handedness      Left     Right
Sex                           
Female      0.400000  0.600000
Male        0.714286  0.285714

# If we want to get the Average age of the Male & Female & How Female are Left & how
# Males are Right Handed?

import numpy as np
pd.crosstab(df.Sex,df.Handedness,values=df.Age,aggfunc=np.average)
-------------
Handedness  Left  Right
Sex                    
Female      44.5   31.0
Male        31.2   28.0

pd.crosstab(df['Sex'],df['Handedness'],values=df['Age'],aggfunc=np.average) # It is also correct.
--------
Handedness  Left  Right
Sex                    
Female      44.5   31.0
Male        31.2   28.0

