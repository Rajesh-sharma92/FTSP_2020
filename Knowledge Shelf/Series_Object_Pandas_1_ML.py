# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:34:47 2020

@author: Rajesh
"""
"""
Extract Values by Index Label in Pandas :- 
-----------------------------------------
"""
NOTE :- Here we want change the index by some of the column name then we can use the 
index_col = 'Column name' like see in the below lines.


import pandas as pd
pokemon = pd.read_csv('E:/Knowledge Shelf/csv Files/pokemon.csv' , index_col = 'Name')
print(pokemon)

**********************
                          #  Type 1
Name                                
Bulbasaur                  1   Grass
Ivysaur                    2   Grass
Venusaur                   3   Grass


NOTE :- We can convert into series this dataset and we will be using this squeeze = True.

import pandas as pd
pokemon = pd.read_csv('E:/Knowledge Shelf/csv Files/pokemon.csv' , index_col = 'Name' , squeeze = True)
pokemon.head()

************************
Name                           
Bulbasaur              1  Grass
Ivysaur                2  Grass
Venusaur               3  Grass
VenusaurMega Venusaur  3  Grass
Charmander             4   Fire

NOTE :- If we want to take indexing we can do it no problem.

Name['Bulbasaur'] # 

Nmae['Ditto'] #  Normal

Name[['Charizard','Jolton']] # Fire , Electric 

# If Name does not exist then it will throw an error.
Name['Digimon'] # An error on the console.

# Here pickachu is there but digimon not available into dataset.
Name[['Pikachu','Digimon']]
# It will show in the result Pickachiu -- Fire , Digimkon --> Nan.

# here you can extract the values by slicing also. One more the last one values like 'Pickachu'
will be included into result. we are slicing in the strings.

Name['Pokemon':'Pickachu']
# It will take the output from Pokemon to Pickachu

"""
get() Method in Pandas :-
-------------------------
"""

import pandas as pd
pokemon = pd.read_csv('E:/Knowledge Shelf/csv Files/pokemon.csv' , index_col = 'pokemon' , squeeze = True)
pokemon.sort_index(inplace=True)
pokemon.head()
******************************
Name                                 
Abomasnow                460    Grass
AbomasnowMega Abomasnow  460    Grass
Abra                      63  Psychic
Absol                    359     Dark
AbsolMega Absol          359     Dark

pokemon.get('Absol') # fire.

pokemon.get(['Absol','Abra']) # It will work properly.

pokemon.get(key = ['Absol','Abra']) # It will work properly.

# Here in the get() method. If we have some pokemon name and which is not available in 
# then it will not throw an error coz default is always None and we can changed default to some values like.


pokemon.get(key='Digimon') # It will not throw an error and it display as Nan.
# It shows Nan into Result.


# Here we can default value for pokemon like.
pokemon.get(key='Digimon',default='This pokemon is not available into dataset')
# 'This pokemon is not available into dataset'

# Here If we take multiple values like into List.
pokemon.get(key=['Digimon','Charmander'],default='This pokemon is not available into dataset')

****************
Digimon --- Nan 
Charmander -- Fire


 





















