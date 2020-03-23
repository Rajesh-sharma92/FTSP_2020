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

------------------------------------------------------------------------------------------------
"""
Methods,Parameters & Arguments in Pandas :-
-----------------------------------------
"""
import pandas as pd

Rate = [10.5,20.4,40.10,65.5,89.0,99.5]
r = pd.Series(Rate)
print(r)

###################
0    10.5
1    20.4
2    40.1
3    65.5
4    89.0
5    99.5
dtype: float64

r.sum() # 325.0

r.product() # 4982166377.055

r.mean() # 54.166666666666664
---------------------------------------------------------------------------------------------
import pandas as pd

fruits = ['Apple','Mango','Watermelon','Pinnaple','Grapes']
weekdays = ['Mon','Tue','Wed','Thu','Fri']

pd.Series(fruits,weekdays) # Here Mon,Tue and etc. will works as Index nos.
#################################
Mon         Apple
Tue         Mango
Wed    Watermelon
Thu      Pinnaple
Fri        Grapes
dtype: object

pd.Series(data=fruits,index=weekdays) # It will also gives the same output.
####################################
Mon         Apple
Tue         Mango
Wed    Watermelon
Thu      Pinnaple
Fri        Grapes
dtype: object

pd.Series(fruits,index=weekdays) # It will also gives the same output.
##################################
Mon         Apple
Tue         Mango
Wed    Watermelon
Thu      Pinnaple
Fri        Grapes
dtype: object


---------------------------------------------------------------------------------------------
import pandas as pd
dataset = pd.read_csv('E:/Knowledge Shelf/csv Files/pokemon.csv' , squeeze=True , usecols=['Name'])
print(dataset)


dataset.head()
#################
0                Bulbasaur
1                  Ivysaur
2                 Venusaur
3    VenusaurMega Venusaur
4               Charmander
Name: Name, dtype: object

dataset.head(10) # Here you will get 10 values from starting.

dataset.sample() # Any one value # 489    Chatot

dataset.sample(5) # Any 5 values from dataset.

dataset.tail() 
#######################
715         MeloettaAria Forme
716    MeloettaPirouette Forme
717                   Genesect
718                    Chespin
719                  Quilladin
Name: Name, dtype: object

dataset.tail(10) # Any 10 values from last end.

dataset.values # Here it will show all those values types.

dataset.index # RangeIndex(start=0, stop=720, step=1)

dataset.dtypes # dtype('O')

dataset.is_unique # True

dataset.size # 720

dataset.ndim # 1

dataset.shape # (720,)

dataset.name # Name

dataset.name='Pokemon_new'

dataset.name # Pokemon_new
-----------------------------------------------------------------------------------------------
"""
Sort_Values & Inplace in Pandas  :-
-------------------------------
"""
import pandas as pd
pokemon = pd.read_csv('E:/Knowledge Shelf/csv Files/pokemon.csv' , squeeze=True , usecols=['Name'])

pokemon.sort_values().head()
#########################################
510                  Abomasnow
511    AbomasnowMega Abomasnow
68                        Abra
392                      Absol
393            AbsolMega Absol
Name: Name, dtype: object

pokemon.sort_values(ascending=True) # BY default it takes the Ascending order values only.
 
pokemon.sort_values(ascending=False) # Here it will start by descending order.

---------------------------------------------------------------------------------------------
import pandas as pd
Inc_data = pd.read_csv('E:/Knowledge Shelf/csv Files/Income_Data.csv' , squeeze=True , usecols=['Income'])

Inc_data = Inc_data.sort_values(ascending=False,inplace=True)
Inc_data

--------------------------------------------------------------------------------------------------------------
import pandas as pd
pokemon = pd.read_csv('E:/Knowledge Shelf/csv Files/pokemon.csv' , squeeze=True , usecols=['Name'])

pokemon.sort_values().head()
pokemon.sort_values(ascending=False,inplace=True)
pokemon.head(4)

695    Zweilous
46        Zubat
631       Zorua
632     Zoroark

--------------------------------------------------------------------------------------------------
"""
Sort_index() in Pandas :-
--------------------------
"""
import pandas as pd
pokemon = pd.read_csv('E:/Knowledge Shelf/csv Files/pokemon.csv' , squeeze=True , usecols=['Name'])

pokemon.sort_values(ascending=False,inplace=True)
pokemon.head()

695     Zweilous
46         Zubat
631        Zorua
632      Zoroark
286    Zigzagoon
Name: Name, dtype: object


pokemon.sort_values(ascending=False)
pokemon.head()


695     Zweilous
46         Zubat
631        Zorua
632      Zoroark
286    Zigzagoon
Name: Name, dtype: object

pokemon.sort_index(ascending=False,inplace=True)
pokemon.head()

719                  Quilladin
718                    Chespin
717                   Genesect
716    MeloettaPirouette Forme
715         MeloettaAria Forme
Name: Name, dtype: object

-----------------------------------------------------------------------------------------------------
"""
Extract Values by Index Position in Pandas:-
------------------------------------------
"""

import pandas as pd
pokemon = pd.read_csv('E:/Knowledge Shelf/csv Files/pokemon.csv' , squeeze=True , usecols=['Name'])
#pokemon.sort_values(ascending=False,inplace=True)
#pokemon.sort_index(ascending=False,inplace=True)
pokemon.head()

pokemon[10] # Wartortle'

pokemon[21] # 'Pidgeotto'

pokemon[[100,200,300,400]]
################################
100      Haunter
200    Sudowoodo
300      Swellow
400      Walrein

pokemon[50:101] # It shows the result from 50th position to till 100th position from list.

pokemon[:50] # It starts from 0 & ends with fifty nine. [0-49] elements.

pokemon[50:] # It starts from 50th index and ends with the last one.

pokemon[:] # It starts with 0 & ends with the last index.

pokemon[:-30] # It starts from 0 index & till 689 index elements.





























