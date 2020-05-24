# Using "groupby" in pandas :- 

import pandas as pd

url = 'http://bit.ly/drinksbycountry'

df = pd.read_csv(url)

df.head()

# get mean of the beer_servings' column.

df['beer_servings'].mean() # 106.16062176165804


# using .groupby

df.groupby('continent')[['beer_servings']].mean()
--------------
              beer_servings
continent                   
Africa             61.471698
Asia               37.045455
Europe            193.777778
North America     145.434783
Oceania            89.687500
South America     175.083333


# here we are accessing all of Africa in the column "continent.

df[df['continent'] == 'Africa'].head()

# To get the mean of Africa Continent.

df.columns


df[df['continent'] == 'Africa'].mean()
-------------
beer_servings                   61.471698
spirit_servings                 16.339623
wine_servings                   16.264151
total_litres_of_pure_alcohol     3.007547
dtype: float64


# To find the value of 'beer_servings' into Africa.

df[df['continent'] == 'Africa']['beer_servings'].mean()
# 61.471698113207545

df[df['continent'] == 'Africa']['total_litres_of_pure_alcohol'].mean()
# 3.00754716981132


df[df['continent'] == 'Europe'].mean()
------------------------
beer_servings                   193.777778
spirit_servings                 132.555556
wine_servings                   142.222222
total_litres_of_pure_alcohol      8.617778
dtype: float64

# To find the value of 'beer_servings' into Europe.

df[df['continent'] == 'Europe']['beer_servings'].mean()
# 193.77777777777777

df[df['continent'] == 'Europe']['wine_servings'].mean()

142.22222222222223


#  This is the same as the number given when we used .groupby

#  This is because we are grouping beer_servings by the continent
#    .groupby max and min

df.groupby('continent')[['beer_servings']].max()
---------------------------
               beer_servings
continent                   
Africa                   376
Asia                     247
Europe                   361
North America            285
Oceania                  306
South America            333

df.groupby('continent')[['beer_servings']].min()
------------------
               beer_servings
continent                   
Africa                     0
Asia                       0
Europe                     0
North America              1
Oceania                    0
South America             93


''' Aggregate findings '''

df.groupby('continent')['beer_servings'].agg(['count','min','max','mean'])
-------------------------------------
               count  min  max        mean
continent                                 
Africa            53    0  376   61.471698
Asia              44    0  247   37.045455
Europe            45    0  361  193.777778
North America     23    1  285  145.434783
Oceania           16    0  306   89.687500
South America     12   93  333  175.083333


df.groupby('continent')['beer_servings'].describe()
-------------------------------------------
               count        mean        std   min     25%    50%     75%    max
continent                                                                      
Africa          53.0   61.471698  80.557816   0.0   15.00   32.0   76.00  376.0
Asia            44.0   37.045455  49.469725   0.0    4.25   17.5   60.50  247.0
Europe          45.0  193.777778  99.631569   0.0  127.00  219.0  270.00  361.0
North America   23.0  145.434783  79.621163   1.0   80.00  143.0  198.00  285.0
Oceania         16.0   89.687500  96.641412   0.0   21.00   52.5  125.75  306.0
South America   12.0  175.083333  65.242845  93.0  129.50  162.5  198.00  333.0



# You can get mean of all numeric columns instead of specifying beer_servings.

df.groupby('continent').mean()
----------------------
               beer_servings  ...  total_litres_of_pure_alcohol
continent                     ...                              
Africa             61.471698  ...                      3.007547
Asia               37.045455  ...                      2.170455
Europe            193.777778  ...                      8.617778
North America     145.434783  ...                      5.995652
Oceania            89.687500  ...                      3.381250
South America     175.083333  ...                      6.308333



''' Visualization '''


data = df.groupby('continent').mean()


data


data.plot(kind='bar')



￼


