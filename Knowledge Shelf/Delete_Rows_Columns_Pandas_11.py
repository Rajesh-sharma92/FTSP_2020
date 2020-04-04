# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:03:03 2020

@author: Rajesh
"""
"""
Delete Rows or Columns in Pandas :- 
--------------------------------
"""
import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv' , index_col='Film')
bond.sort_index(inplace=True)

bond.head()

# How to delete the values Row wise.

bond.drop('A View to a Kill')

bond.drop('Casino Royale')

bond.drop(['Diamonds Are Forever','Die Another Day','Dr. No'])

# How to delete the values Column wise.
# Here We can write axis = column also instead of numbers.

bond.drop('Box Office' , axis = 1)
bond.head()

bond.drop(['Box Office','Bond Actor Salary','Year'] , axis = 1 , inplace = True)
bond.head()
-------------------------------------------------------------------------------------------

# NOTE :- Here we can use the pop() method also to drop the row & columns.
import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv' , index_col='Film')
bond.sort_index(inplace=True)

actor = bond.pop('Actor')
bond.head()
print(actor)

# Here we can use the delete method also.

del bond['Director'] 
bond.head()

del(bond['Year'])
bond.head()

------------------------------------------------------------------------------------------------
"""
Create Random Sample with the .sample() in Pandas :-
----------------------------------------------------
"""
import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv' , index_col='Film')
bond.sort_index(inplace=True)

# Here if we are not passing any of values for n then it will taking of Random values & display it.
bond.sample()
***************
      Year         Actor  ... Budget  Bond Actor Salary
Film                        ...                          
Dr. No  1962  Sean Connery  ...    7.0                0.6

# Here we can define the No. of rows we want to display on to console.
bond.sample(n=10)

bond.sample(5)

# Here we want to take the data into fraction like 25% of total data.
bond.sample(frac=0.25)

# Here we want to select the data Rows wise like this.
bond.sample(n = 5 , axis = 0)
bond.sample(n = 5 , axis = 'rows')
bond.sample(n = 5 , axis = 'index')

# Here we want to select the data Columns wise like this.
bond.sample(n = 3 , axis = 1)
bond.sample(n = 3 , axis = 'columns')

-----------------------------------------------------------------------------------------------
"""
The nsmallest() and nlargest() Methods in Pandas :-
----------------------------------------------------
"""
import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv' , index_col='Film')
bond.sort_index(inplace=True)

bond.head()

# Here if want to get the smallest & largest No. from dataset below the traditional method.
bond.sort_values('Box Office' , ascending=False , inplace = True)
bond.sort_values('Box Office' , inplace = True)

# Here we have some of the methods to get the smallest & largest No. from dataset.
bond.nlargest(n=3 , columns='Bond Actor Salary')
******************
Film                                           ...                          
Die Another Day          2002  Pierce Brosnan  ...  154.2               17.9
Skyfall                  2012    Daniel Craig  ...  170.2               14.5
The World Is Not Enough  1999  Pierce Brosnan  ...  158.3               13.5

bond.nsmallest(n=3 , columns='Bond Actor Salary')
********************
Film                                   ...                  
On Her Majesty's Secret Service  1969  ...               0.6
Dr. No                           1962  ...               0.6
From Russia with Love            1963  ...               1.6

bond.nlargest(n=1 , columns='Bond Actor Salary')
************
Die Another Day          2002  Pierce Brosnan  ...  154.2               17.9

NOTE :- Here compulsory we need to pass the n value or else it will throw an error.

bond.nlargest(3, columns='Budget')
**********
                   Year         Actor  ... Budget  Bond Actor Salary
Film                                   ...                          
Spectre            2015  Daniel Craig  ...  206.3                NaN
Quantum of Solace  2008  Daniel Craig  ...  181.4                8.1
Skyfall            2012  Daniel Craig  ...  170.2               14.5

bond.nsmallest(5,columns='Year')
************
                      Year         Actor  ... Budget  Bond Actor Salary
Film                                       ...                          
Dr. No                 1962  Sean Connery  ...    7.0                0.6
From Russia with Love  1963  Sean Connery  ...   12.6                1.6
Goldfinger             1964  Sean Connery  ...   18.6                3.2
Thunderball            1965  Sean Connery  ...   41.9                4.7
Casino Royale          1967   David Niven  ...   85.0                NaN

# Here we can get the details like this below types also.
bond['Bond Actor Salary'].nlargest(3)
**********
Film
Die Another Day            17.9
Skyfall                    14.5
The World Is Not Enough    13.5
Name: Bond Actor Salary, dtype: float64

bond['Bond Actor Salary'].nsmallest(3)
****************
Film
On Her Majesty's Secret Service    0.6
Dr. No                             0.6
From Russia with Love              1.6
Name: Bond Actor Salary, dtype: float64

-----------------------------------------------------------------------------------
"""
The .where() Methods in Pandas :-
--------------------------------
"""
import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv' , index_col='Film')
bond.sort_index(inplace=True)

mask = bond['Actor'] == 'Sean Connery'
bond[mask].head()
*********
                       Year         Actor  ... Budget  Bond Actor Salary
Film                                       ...                          
Diamonds Are Forever   1971  Sean Connery  ...   34.7                5.8
Dr. No                 1962  Sean Connery  ...    7.0                0.6
From Russia with Love  1963  Sean Connery  ...   12.6                1.6
Goldfinger             1964  Sean Connery  ...   18.6                3.2
Never Say Never Again  1983  Sean Connery  ...   86.0                NaN


bond.where(mask).head()
**********
                        Year         Actor  ... Budget  Bond Actor Salary
Film                                        ...                          
A View to a Kill         NaN           NaN  ...    NaN                NaN
Casino Royale            NaN           NaN  ...    NaN                NaN
Casino Royale            NaN           NaN  ...    NaN                NaN
Diamonds Are Forever  1971.0  Sean Connery  ...   34.7                5.8
Die Another Day          NaN           NaN  ...    NaN                NaN


bond.where(bond['Box Office'] > 800)

mask1 = bond['Box Office'] > 800
bond.where(mask & mask1)













