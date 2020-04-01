# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:01:59 2020

@author: Rajesh
"""
"""
set_index & .reset_index() in Pandas :- 
-------------------------------------
"""
import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv')
bond.head()

# Here IF we want we can change the index of the any columns like by passing index_col = 'column name' into reading csv file.
# Other we can set the index also.

bond.set_index('Film' , inplace = True)
bond.head()

# NOTE :- Now here Film column is used as Index values but if we want remove that column also.

bond.reset_index(drop=True , inplace =True)

bond.reset_index()

bond.reset_index(drop=True)

bond.set_index('Year' , inplace = True)

bond.reset_index(inplace = True)

bond.set_index(drop=True , inplace = True)

------------------------------------------------------------------------------------------------------------
"""
Retrieve Row Values Using loc in Pandas :- 
-----------------------------------------
"""
import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv' , index_col = 'Film')

bond.sort_index(inplace= True)
bond.head()

bond.loc['Goldfinger']
******************
Year                         1964
Actor                Sean Connery
Director             Guy Hamilton
Box Office                  820.4
Budget                       18.6
Bond Actor Salary             3.2
Name: Goldfinger, dtype: object

bond.loc['GoldenEye']
******************

Year                            1995
Actor                 Pierce Brosnan
Director             Martin Campbell
Box Office                     518.5
Budget                          76.9
Bond Actor Salary                5.1
Name: GoldenEye, dtype: object

# If the passes Movie is not in the dataset. Then it will throw an error.
bond.loc['Dangal']

# It the Repaeted movie also in the different year by different Actor.
bond.loc['Casino Royale']

# Here loc we can use as the Range function.
bond.loc['Diamonds are Forever' : 'Moonraker']

# It starts from GoldenEye & ends with the last one. 
bond.loc['GoldenEye':]

# It starts from first movie name  & ends with the GoldenEye. 
bond.loc[:'GoldenEye']

# To get the multiple values details.
bond.loc[['Moonraker','GoldenEye']]

# Here 2 movie details are matched and 1 is not matched then it will show as Nan into result.
bond.loc[['Diamonds are Forever','GoldenEye','dangal']]

# NOTE :- We have one Interseting thing to get the details like this partcular movie 
# is there or not into dataset.

'Dangal' in bond.index  # False

'GoldenEye' in bond.index # True

----------------------------------------------------------------------------------------------
"""
Retrieve Row Values Using iloc in Pandas :- 
-----------------------------------------
"""
import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv')

# NOTE :- Here ' iloc ' does not consider the last one.

bond.iloc[[10,20]]

bond.iloc[:4]

bond.iloc[4:8]

bond.iloc[23:] 

bond.iloc[5:15:2]

bond.iloc[10:20:4]

bond.iloc[[5,7,10,21]]

----------------------------------------------------------------------------------------------
"""
Retrieve Row Values Using ix in Pandas :- 
---------------------------------------
"""
import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv' , index_col = 'Film')

bond.sort_index(inplace= True)
bond.head()

# NOTE :- Here we can use of the method and both will give the same Result.
bond.loc['GoldenEye']

bond.ix['GoldenEye']

bond.ix[['Moonraker','GoldenEye']]

bond.ix['Goldfinger':'GoldenEye']

bond.iloc[14]

bond.iloc[14, 2:5]

bond.iloc[20, [3,5,2]]










