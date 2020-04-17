# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:55:16 2020

@author: Rajesh
"""
'''
Histograms :- 
-----------
'''
import matplotlib.pyplot as plt

blood_sugar = [113,85,90,150,149,85,93,115,150,80,78,82,129]

# To create the Histogram we just need to use the hist() function.
plt.hist(blood_sugar)
***************
(array([5., 1., 1., 0., 1., 1., 0., 1., 0., 3.]),
 array([ 78. ,  85.2,  92.4,  99.6, 106.8, 114. , 121.2, 128.4, 135.6,
        142.8, 150. ]),
 <a list of 10 Patch objects>)
# It will shows the Histogram here.
------------------------------------------------------------

# Default bins values will be always = 10 
# If we want to set the new values then easily we can change it.
# we will change the value for the rwidth = 0.95 and ,maximum rwidth = 1.

import matplotlib.pyplot as plt

blood_sugar = [113,85,90,150,149,85,93,115,150,80,78,82,129]

# To create the Histogram we just need to use the hist() function.
plt.hist(blood_sugar , bins=3 , rwidth=0.95)

*************
(array([7., 2., 4.]),
 array([ 78., 102., 126., 150.]),
 
-------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

blood_sugar = [113,85,90,150,149,85,93,115,150,80,78,82,129]

# To create the Histogram we just need to use the hist() function.
plt.hist(blood_sugar , bins=[80,100,125,150] , rwidth=0.95)

****************
(array([6., 2., 4.]), array([ 80, 100, 125, 150]), <a list of 3 Patch objects>)

------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

blood_sugar = [113,85,90,150,149,85,93,115,150,80,78,82,129]

# To create the Histogram we just need to use the hist() function.
plt.hist(blood_sugar , bins=[80,100,125,150] , rwidth=0.95 ,color='r',histtype='step')
 
-----------------------------------------------------------------------------------------

# For the example lets create the Histogram for Mens& Womens as well.

import matplotlib.pyplot as plt

blood_sugar_men = [113,85,90,150,149,85,93,115,150,80,78,82,129]
blood_sugar_women = [95,65,70,135,65,73,99,130,70,45,55,100]


# To create the Histogram we just need to use the hist() function.
plt.xlabel('Sugar Range')
plt.ylabel('Total No. of Patients')
plt.title('Blood Sugar Analysis')
plt.hist([blood_sugar_men , blood_sugar_women] , bins=[80,100,125,150] , rwidth=0.95 ,color=['g','b'],
         label=['Mens','Womens'])

plt.legend()


-----------------------------------------------------------------------------------------------------
# To make it Horizontal Histogram we just need to change the Orientation 

import matplotlib.pyplot as plt

blood_sugar_men = [113,85,90,150,149,85,93,115,150,80,78,82,129]
blood_sugar_women = [95,65,70,135,65,73,99,130,70,45,55,100]


# To create the Histogram we just need to use the hist() function.
plt.xlabel('Sugar Range')
plt.ylabel('Total No. of Patients')
plt.title('Blood Sugar Analysis')
plt.hist([blood_sugar_men , blood_sugar_women] , bins=[80,100,125,150] , rwidth=0.95 ,color=['g','b'],
         label=['Mens','Womens'] , orientation='horizontal')

plt.legend()
