# Using "axis" Parameter in Pandas :- 

import pandas as pd

url = 'http://bit.ly/drinksbycountry'

df = pd.read_csv(url)

df.head()

df.columns
-----------------
Index(['country', 'beer_servings', 'spirit_servings', 'wine_servings',
       'total_litres_of_pure_alcohol', 'continent'],
      dtype='object')


# let's remove "continent" column
# axis=1 drops the column

df.drop('continent' , axis=1 , inplace = True)

df.head()

df.columns
---------------
Index(['country', 'beer_servings', 'spirit_servings', 'wine_servings',
       'total_litres_of_pure_alcohol'],
      dtype='object')

# drops second row
# axis=0 drops the row

rows = 3
df.drop(rows , axis = 0 , inplace = True)

# drops multiple rows

row_drop = [4,5,6,7,8]

df.drop(row_drop , axis=0 , inplace = True)

df


row_drop = range(10,50)

df.drop(row_drop , axis = 0 , inplace = True)

df.head()
---------------
              country  ...  total_litres_of_pure_alcohol
0          Afghanistan  ...                           0.0
1              Albania  ...                           4.9
9              Austria  ...                           9.7
50            Dominica  ...                           6.6
51  Dominican Republic  ...                           6.2



# mean of each numeric column
# it is the same as the following command as axis=0 is the default
# drinks.mean(axis=0)
# it instructs pandas to move vertically

df.mean() # drinks.mean(axis=0)
-------------
beer_servings                   102.095890
spirit_servings                  80.027397
wine_servings                    47.568493
total_litres_of_pure_alcohol      4.581507
dtype: float64


# mean of each row
# drinks.mean(axis='columns)

df.mean(axis=1).head()
0       0.000
1      69.975
9     138.675
50     92.650
51     88.800
dtype: float64



# this is the same as 
# drinks.mean(axis=0).head()

df.mean(axis='index').head()
------------------
beer_servings                   102.095890
spirit_servings                  80.027397
wine_servings                    47.568493
total_litres_of_pure_alcohol      4.581507
dtype: float64



df.mean(axis='columns').head()
---------------
0       0.000
1      69.975
9     138.675
50     92.650
51     88.800
dtype: float64


df.mean(axis='rows').head()
--------------
beer_servings                   102.095890
spirit_servings                  80.027397
wine_servings                    47.568493
total_litres_of_pure_alcohol      4.581507
dtype: float64


# NOTE :- We should know that we axis Parameter in the Different ways.

axis = 0 |  axis = 'rows' | axis = 'index' # All are same only.

axis = 1 | axis = 'columns' # All are same only.

 
''' For columns drop '''


df.drop('beer_servings' , axis = 'columns' , inplace = True)

df.columns # beer_servings will be dropped.

df.drop('country' , axis = 1 , inplace = True)

df.columns # country will be dropped.


''' For Rows drop '''

row_drop = [1,2]
df.drop(row_drop , axis = 0 , inplace = True)
df.head()


row_drop = [3,4,5,6,7]
df.drop(row_drop , axis = 'index' , inplace = True)
df.head()



row_drop = [8,9,10,11,12,13]
df.drop(row_drop , axis = 'rows' , inplace = True)
df.head()






