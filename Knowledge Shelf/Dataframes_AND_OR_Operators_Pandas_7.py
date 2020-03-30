# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:18:35 2020

@author: Rajesh
"""
"""
Filter Dataframe with AND & OR Operators :- 
-----------------------------------------
"""
import pandas as pd

df = pd.read_csv('E:\Knowledge Shelf\csv Files\employees.csv' , parse_dates = ['Start Date','Last Login Time'])

df['Senior Management'] = df['Senior Management'].astype('bool') 
df['Gender'] = df['Gender'].astype('category')

df.head()

# Question :- To find the details of the employees those are working into Marketing team and should be Male ?
mask1 = df['Gender'] == 'Male'

mask2 = df['Team'] == 'Marketing'

df[mask1 & mask2].shape # (41, 8)

df[mask1 & mask2].head()


mask3 = df['Senior Management']

mask4 = df['Start Date'] > '1990-01-01'

df[mask3 | mask4].shape # (625, 8)

df[mask3 | mask4].head()

# Question :- To find the details of the employees who is First Name is 'Robert' and working in Team of clent services 
# or Joined before on 2016-06-01.

mask5 = df['First Name'] == 'Robert'
mask6 = df['Team'] = 'Client Services'
mask7 = df['Start Date'] < '2016-06-01'

df[(mask5 & mask6) | mask7] # It will shows the result here.

--------------------------------------------------------------------------------------------------------------

"""
isin() Method in Pandas :- 
------------------------
"""
import pandas as pd

df = pd.read_csv('E:\Knowledge Shelf\csv Files\employees.csv' , parse_dates = ['Start Date','Last Login Time'])

df['Senior Management'] = df['Senior Management'].astype('bool') 
df['Gender'] = df['Gender'].astype('category')


mask1 = df['Team'] == 'Legal'
mask2 = df['Team'] == 'Sales'
mask3 = df['Team'] == 'Product'

df[mask1 | mask2 | mask3].shape # (277, 8)

df[mask1 | mask2 | mask3].head()
----------------------------

# We can do like this also the above code.
mask = df['Team'].isin(['Legal','Sales','Product'])

df[mask].shape # (277, 8)

----------------------
# We can do like this also the above code.
# Here we can remove & Add some Team Names as per company requirements.
df[df['Team'].isin(['Legal','Sales','Product'])].shape # (277, 8)

df[df['Team'].isin(['Finance','Sales','Product'])].shape # (291, 8)

---------------------------------------------------------------------------------------------------------

"""
isnull() & .notnull() Method in Pandas :- 
-------------------------------------
"""
NOTE :- Here we can seperat the not null & Null Values from series or Dataframes.

import pandas as pd

df = pd.read_csv('E:\Knowledge Shelf\csv Files\employees.csv' , parse_dates = ['Start Date','Last Login Time'])

df['Senior Management'] = df['Senior Management'].astype('bool') 
df['Gender'] = df['Gender'].astype('category')
df.head()

# Question :- How to the not Null or Nan values from Dataset.

df['Team'] == 'NaN' # It is not good Approach & not recommanded also.

mask = df['Team'].isnull()

df[mask].shape # (43, 8)


mask1 = df['Gender'].notnull()

df[mask1].shape # (855, 8)














