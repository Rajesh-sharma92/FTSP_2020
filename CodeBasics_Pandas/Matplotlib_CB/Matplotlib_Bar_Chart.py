# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:02:48 2020

@author: Rajesh
"""
'''
Matplotlib Bar Chart :- 
---------------------- 
'''
# Lets create the Bar Chart of the One of the company as USA.

import matplotlib.pyplot as plt

import numpy as np

company = ['GOOGLE','AMAZON','MICROSOFT','FACEBOOK']

revenue = [90,136,89,27]

profit = [40,8,34,12]

xpos = np.arange(len(company))

xpos # [0, 1, 2, 3]

plt.xticks(xpos,company)
plt.bar(xpos,revenue ,label= 'Revenue') 
plt.xlabel('Companies')
plt.ylabel('Revenue')
plt.title('USA Tech Revenue Bar Chart')
plt.bar(xpos,profit , label= 'Profit')
plt.legend()

-------------------------------------------------------------------------------------------

# NOTE :- Here in the above code we were just getting Revenue & prfit on the same line and 
# we are not sure about revenue & profit details. So , we need to use the some points numbers.

import matplotlib.pyplot as plt

import numpy as np

company = ['GOOGLE','AMAZON','MICROSOFT','FACEBOOK']

revenue = [90,136,89,27]

profit = [40,8,34,12]

xpos = np.arange(len(company))

xpos # [0, 1, 2, 3]

plt.xticks(xpos,company)
plt.bar(xpos - 0.2 , revenue , width = 0.4 , label= 'Revenue') 
plt.bar(xpos + 0.2 , profit , width = 0.4 ,  label= 'Profit')
plt.xlabel('Companies')
plt.ylabel('Revenue')
plt.title('USA Tech Revenue Bar Chart')
plt.legend()


------------------------------------------------------------------------------------------

# If we want ot generate the chart at Horizontal plan.
# We need to take the ysticks here for Horizontal and barh() function.

import matplotlib.pyplot as plt

import numpy as np

company = ['GOOGLE','AMAZON','MICROSOFT','FACEBOOK']

revenue = [90,136,89,27]

profit = [40,8,34,12]

xpos = np.arange(len(company))

xpos # [0, 1, 2, 3]

plt.yticks(xpos,company)
plt.barh(xpos - 0.2 , revenue , label= 'Revenue') 
plt.barh(xpos + 0.2 , profit , label= 'Profit')
plt.xlabel('Revenue')
plt.ylabel('Companies')
plt.title('USA Tech Revenue Bar Chart')
plt.legend()


