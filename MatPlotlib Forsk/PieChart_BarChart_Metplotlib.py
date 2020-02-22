# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 12:09:21 2020

@author: Rajesh
"""
"""
Pie chart, where the slices will be ordered and plotted counter-clockwise:
"""
import matplotlib.pyplot as plt

labels = 'CSE', 'ECE', 'IT', 'EE'
sizes = [15, 30, 25, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.5, 0, 0, 0)  # explode 1st slice

# plt.pie(sizes, labels=labels, autopct='%.0f%%')

# or

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%', shadow=True, startangle=180)


plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig("E:\MatPlotlib Forsk\pie.jpg")
plt.show()

￼
----------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

labels = 'Python','Java','c++','ML','DL','AI'
sizes = [75 , 20, 40, 90, 85, 90]
colors = ['Blue','Red','Yellow','Green','brown','lightskyblue']    
explode = (0.2,0,0,0,0,0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.2f%%', shadow=True, startangle=180)


plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.savefig("E:\MatPlotlib Forsk\pie1.jpg")
plt.show()

-------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

plt.pie([75 , 20, 40, 90, 85, 90],labels=['Python','Java','c++','ML','DL','AI'],\
        autopct='%1.2f%%',shadow=True,explode = (0.2,0,0,0,0,0),\
        colors = ['Blue','Red','Yellow','Green','brown','lightskyblue'],startangle=30)

plt.savefig("E:\MatPlotlib Forsk\pie2.jpg")

plt.show()

----------------------------------------------------------------------------------------------------------------------
"""
Plotting a bar chart
"""
import matplotlib.pyplot as plt
 
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
performance = [10,8,6,4,2,1]
 
plt.bar([0,1,2,3,4,5], performance, align='center', alpha=1.0)
plt.xticks([0,1,2,3,4,5], objects)
plt.ylabel('Usage')
plt.title('Programming Language Usage')
plt.savefig("E:\MatPlotlib Forsk\bar.jpeg")
 
plt.show()

------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

objects = ('Rajesh','sharma','Ravi','Sandeep','Yogi Londa','Mohit')
performance = [90,80,70,60,50,40]

plt.bar([0,1,2,3,4,5], performance, align = 'center' , alpha = 1.0)
plt.xticks([0,1,2,3,4,5], objects)
plt.ylabel('|_______________________Marks____________________|') 
plt.xlabel('|________________________Student Names ______________|')
plt.title('Forsk School students Marks')
plt.savefig("E:\MatPlotlib Forsk\bar1.jpg")

plt.show()
--------------------------------------------------------------------------------------------------
￼

￼













































 
