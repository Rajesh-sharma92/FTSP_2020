# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 23:25:19 2020

@author: Rajesh
"""
Series Object in Pandas :- 
-----------------------
import pandas as pd

kulfi = ['choclate','better scotch','orange','pista-kesar','mango']
series = pd.Series(kulfi)
print(series)
#####################
0         choclate
1    better scotch
2           orange
3      pista-kesar
4            mango
dtype: object


series[1] # better scotch

series[4] # mango

series[:3]
#################
0         choclate
1    better scotch
2           orange

series[:]
################
0         choclate
1    better scotch
2           orange
3      pista-kesar
4            mango

series[:-2]
0         choclate
1    better scotch
2           orange

-----------------------------------------------------------------------------------------

import pandas as pd

lottery = [4,8,10,25,30,45,60]

ltr = pd.Series(lottery)
print(ltr)

######################
0     4
1     8
2    10
3    25
4    30
5    45
6    60
dtype: int64
-------------------------------------------------------------------------------------

reg = [True,False,False,True,False,True]
pd.Series(reg)
################
0     True
1    False
2    False
3     True
4    False
5     True
dtype: bool

##############
print(reg)

[True, False, False, True, False, True]

----------------------------------------------------------------------------------
Attributes in Pandas :- 
---------------------

import pandas as pd

men = ['Smart','Hansome','Charming','Brillent','Humable']
s = pd.Series(men)
print(s)
################
0       Smart
1     Hansome
2    Charming
3    Brillent
4     Humable
dtype: object

s.values
################
array(['Smart', 'Hansome', 'Charming', 'Brillent', 'Humable'],
      dtype=object)

s.dtypes # dtype('O')

s.index
RangeIndex(start=0, stop=5, step=1)

s.ndim # 1

s.size # 5

















