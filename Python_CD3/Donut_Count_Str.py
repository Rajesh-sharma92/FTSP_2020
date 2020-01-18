# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:25:59 2020

@author: Rajesh
"""
""" 
# Take donut count from the user and print a string of the 
# form 'Number of donuts: <count>'
# where <count> is the donut count entered by the user. 
# However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# Number of donuts: 15
# Number of donuts: many

"""

donut=input('Enter the Donut Counts numbers :')
x=int(donut)
if x>=10:
   x='Many'
elif x<10:
    x=x
print('Number of Donuts : {}'.format(x))
    



pizza=input('Enter the No. of Pizza :')
pz=int(pizza) 
if pz>=20:
   pz='Dominos'
elif pz<5:
     pz=pz
print('Number of Pizza :{}'.format(pz))
        