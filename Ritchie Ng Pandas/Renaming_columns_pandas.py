# Renaming columns in a pandas DataFrame :- 

import pandas as pd

url = 'http://bit.ly/uforeports'

df = pd.read_csv(url)

df.head()

# To check out only the columns
# It will output a list of columns
df.columns
----------------
Index(['City', 'Colors Reported', 'Shape Reported', 'State', 
       'Time'], dtype='object')


# Method 1 : Renaming a single column.

df.rename(columns = {'Colors Reported':'Colors_Reported' , 'Shape Reported':'Shape_Reported'}, inplace = True)

df.columns
--------------
Index(['City', 'Colors_Reported', 'Shape_Reported', 'State',
       'Time'], dtype='object')



# Method 2 : Renaming multiple columns.

df_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']

df.columns = df_cols

df.columns
---------------
Index(['city', 'colors reported', 'shape reported', 'state',
       'time'], dtype='object')

df.head()


# Method 3: Change columns while reading.

url = 'http://bit.ly/uforeports'

df_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']

df = pd.read_csv(url , names = df_cols , header = 0)

df.columns

df.head()


# Method 4: Replacing spaces with underscores for all columns.

If you have a 100 columns, some had spaces in them and you want to replace 
all the spaces with underscores.

url = 'http://bit.ly/uforeports'

df = pd.read_csv(url)

df.columns
---------------
Index(['City', 'Colors Reported', 'Shape Reported', 'State', 
       'Time'], dtype='object')



df.columns = df.columns.str.replace(' ' , '_')

df.columns
-------------
Index(['City', 'Colors_Reported', 'Shape_Reported', 'State', 
       'Time'], dtype='object')


df.head()


df.columns = df.columns.str.replace('_' , ' ')

df.columns
-----------
Index(['City', 'Colors Reported', 'Shape Reported', 'State', 
       'Time'], dtype='object')

df.head()


df.columns = df.columns.str.replace(' ' , '$')

df.columns
------------
Index(['City', 'Colors$Reported', 'Shape$Reported', 'State', 
       'Time'], dtype='object')

df.head()


df.columns = df.columns.str.replace('$', ' ')

df.columns
-------------
Index(['City', 'Colors Reported', 'Shape Reported', 'State',
       'Time'], dtype='object')

df.head()





