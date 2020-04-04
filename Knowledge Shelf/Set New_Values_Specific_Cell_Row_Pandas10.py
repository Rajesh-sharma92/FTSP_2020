# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 20:54:32 2020

@author: Rajesh
"""
"""
Set New Values for a Specific Cell or Row in Pandas :-
---------------------------------------------------
"""
import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv' , index_col='Film')
bond.sort_index()

bond.ix['Dr. No']

bond.loc['Dr. No']

bond.iloc[1]

bond.loc['Dr. No' , 'Actor'] = 'Sir Sean Connery'

bond.loc['Dr. No'] # Actor   Sir Sean Connery
**************************
Year                             1962
Actor                Sir Sean Connery
Director                Terence Young
Box Office                      448.8
Budget                              7
Bond Actor Salary                 0.6


bond.loc['Dr. No' ,['Box Office','Budget','Bond Actor Salary']] = [470,9,6]

bond.loc['Dr. No']
***********************
Year                             1962
Actor                Sir Sean Connery
Director                Terence Young
Box Office                        470
Budget                              9
Bond Actor Salary                   6
Name: Dr. No, dtype: object


bond.loc['Dr. No' , 'Box Office']
***********
470.0

bond.loc['Dr. No' , 'Budget'] # 9.0

-----------------------------------------------------------------------------------------------------------------
"""
Set Multiple Values in DataFrame in Pandas :- 
------------------------------------------
"""
import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv' , index_col='Film')
bond.sort_index(inplace=True)

mask = bond['Actor'] == 'Sean Connery'

bond[mask].shape # (7, 6)

bond[mask]['Actor']

bond[mask]['Actor'] = 'Sir Sean Connery'

NOTE :- If we are trying to make any changes like above but w are getting an error.
NOTE :- To Avoid such kinds of errors, we will be using the loc method.

bond.loc[mask , 'Actor'] = 'Sir Sean Connery'
bond.head()

----------------------------------------------------------------------------------------------
"""
The .query() Methods in Pandas :- 
--------------------------------
"""
NOTE :- query() method always works iff when there is NO spaces between the columns Name
and Column Name should be always strings.

import pandas as pd

bond = pd.read_csv('E:\Knowledge Shelf\csv Files\jamesbond.csv' , index_col='Film')
bond.sort_index(inplace=True)

bond.columns

bond.columns = [ column_name.replace(' ' , '_') for column_name in bond.columns ]
bond.head()

bond.query('Actor == "Sean Connery"')

bond.query('Director == "Terence Young"')

bond.query('Actor == "Roger Moore "')

bond.query('Box_Office > 600') # It shows the result into dataset.

bond.query("Actor == 'Roger Moore' and Director == 'John Glen'")
bond.query("Actor == 'Roger Moore' & Director == 'John Glen'")


bond.query("Actor == 'Roger Moore' or Director == 'John Glen'")

bond.query("Actor in ['Timothy Dalton ','George Lazenby']") # Valid

bond.query("Actor not in ['Sean Connery','George Lazenby']") # Valid











