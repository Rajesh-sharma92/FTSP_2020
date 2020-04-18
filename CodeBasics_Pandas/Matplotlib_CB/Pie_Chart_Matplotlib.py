# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 18:25:00 2020

@author: Rajesh
"""
'''
Pie Chart :- 
---------
'''
import matplotlib.pyplot as plt

exp_vals = [1400,600,300,410,250]

exp_labels = ['Home Rent','Food','Phone/Internet bill','Car','Other Utilities']


plt.axis()
plt.pie(exp_vals,labels=exp_labels , radius=1.5 , autopct='%0.2f%%') # If Need Decimal till 2 places.

plt.pie(exp_vals,labels=exp_labels , radius=1.5 , autopct='%0.0f%%') # If No Decimal 


plt.pie(exp_vals,labels=exp_labels , radius=1.5 , autopct='%0.0f%%',shadow=True) 

# We want to take food out from the chart. We will use the explode=[]
plt.pie(exp_vals,labels=exp_labels , radius=1.5 , autopct='%0.0f%%',shadow=True , explode=[0,0.2,0,0,0.1]) 

# We want to change my Home rent to Angal like 45 , 180.

plt.pie(exp_vals,labels=exp_labels , radius=1.5 , autopct='%0.0f%%',\
        shadow=True , explode=[0,0.2,0,0,0.1],startangle=45) 


plt.pie(exp_vals,labels=exp_labels , radius=1.5 , autopct='%0.0f%%',\
        shadow=True , explode=[0,0.2,0,0,0.2],startangle=180) 


# plt.savefig('E:\CodeBasics_Pandas\Matplotlib_CB\Pie_Chart.png')

# To make the fit the properly chart.
# plt.savefig('E:\CodeBasics_Pandas\Matplotlib_CB\Pie_Chart2.png' ,bbox_inches='tight')

# To extra Padding.
# plt.savefig('E:\CodeBasics_Pandas\Matplotlib_CB\Pie_Chart3.png' ,bbox_inches='tight',pad_inches=0.5)

# To make the Transparent.
# plt.savefig('E:\CodeBasics_Pandas\Matplotlib_CB\Pie_Chart4.png' ,bbox_inches='tight',pad_inches=0.5,transparent=True)

# To store in to jpg Format.
# plt.savefig('E:\CodeBasics_Pandas\Matplotlib_CB\Pie_Chart5.jpg' ,bbox_inches='tight')

# To store in to pdf  Format.
plt.savefig('E:\CodeBasics_Pandas\Matplotlib_CB\Pie_Chart5.pdf' ,bbox_inches='tight')










