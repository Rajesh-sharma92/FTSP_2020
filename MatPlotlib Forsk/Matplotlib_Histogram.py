# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:52:37 2020

@author: Rajesh
"""
"""
Ramesh is the branch manager at a local bank. 
Recently, Ramesh’s been receiving customer feedback saying that the wait times 
for a client to be served by a customer service representative are too long. 
Ramesh decides to observe and write down the time spent by each customer on waiting.

Write down the wait times spent by 20 customers
[43.1,35.6,37.6,45.3,43.5,40.3,50.2,47.3,31.2,42.2,45.5,30.3,31.4,35.6,45.2,
54.1,45.6,36.5,43.1]
"""
import matplotlib.pyplot as plt
# Customers wait times in seconds ( n = 20 customers )
customerWaitTime = [43.1,35.6,37.6,45.3,43.5,40.3,50.2,47.3,31.2,42.2,45.5,30.3,31.4,35.6,45.2,54.1,45.6,36.5,43.1]

customerWaitTime.sort()
# [1 to 35]      30.3, 31.2, 31.4                     [3]
# [35 to 40]     35.6, 35.6, 36.5, 37.6               [4]
# [40 to 45]     40.3, 42.2, 43.1, 43.1, 43.5         [5]
# [45 to 50]     45.2, 45.3, 45.5, 45.6, 47.3         [5]
# [50 to 55]     50.2, 54.1                           [2]

# Ramesh can conclude that the majority of customers wait between 35.1 and 50 seconds.
print(customerWaitTime)

plt.hist(customerWaitTime,bins=[25,30,35,40,45,50,55])
plt.axis([25, 60, 0, 6]) 
plt.xlabel('Seconds')
plt.ylabel('Customers')
plt.title('Bank Customer Timing Details')
plt.xticks([25,30,35,40,45,50,55])
plt.figure(figsize=(15,3))
plt.savefig('E:\MatPlotlib Forsk\Histogram.jpg')

plt.show()

-------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

CustomerChoosingItemsTime = [10.1,20.3,11.5,22.5,40.5,42.5,45.8,60.5,65.9,70.9,75.5]
CustomerChoosingItemsTime.sort()
# [10 to 12] --> 10.1 , 11.5 --> [2]
# [20 to 23] --> 20.3 , 22.5 --> [2]
# [40 to 46] --> 40.5 , 42.5 , 45.8--> [3]
# [60 to 66] --> 60.5 , 65.9 --> [2]
# [80 to 91] --> 70.9 , 75.5 --> [2]

print(CustomerChoosingItemsTime)
plt.hist(CustomerChoosingItemsTime , bins=[10,15,20,30,40,50,60,70,80])#bins=[10,20,30,40,50,60,70,80])
plt.axis([0,90,0,5])

plt.xlabel('Seconds')
plt.ylabel('Customers')
plt.title('Reliance Fresh Timing Details')
plt.savefig('E:\MatPlotlib Forsk\Histogram1.jpg')

plt.show()

-----------------------------------------------------------------------------

import matplotlib.pyplot as plt

CustomerChoosingItemsTime = [5,5.2,6.2,7.2,11.2,13.2,20.2]
CustomerChoosingItemsTime.sort()
# [10 to 12] --> 10.1 , 11.5 --> [2]
# [20 to 23] --> 20.3 , 22.5 --> [2]
# [40 to 46] --> 40.5 , 42.5 , 45.8--> [3]
# [60 to 66] --> 60.5 , 65.9 --> [2]
# [80 to 91] --> 70.9 , 75.5 --> [2]

print(CustomerChoosingItemsTime)
plt.hist(CustomerChoosingItemsTime , bins=[5,10,15,20,25])#bins=[10,20,30,40,50,60,70,80])
plt.axis([0,30,0,5])

plt.xlabel('Seconds')
plt.ylabel('Customers')
plt.title('Reliance Fresh Timing Details')
plt.savefig('E:\MatPlotlib Forsk\Histogram1.jpg')

plt.show()

------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

CustomerChoosingItemsTime = [9.5,10.2,20.2,23.3,24.6,25.3]
CustomerChoosingItemsTime.sort()
# [10 to 12] --> 10.1 , 11.5 --> [2]
# [20 to 23] --> 20.3 , 22.5 --> [2]
# [40 to 46] --> 40.5 , 42.5 , 45.8--> [3]
# [60 to 66] --> 60.5 , 65.9 --> [2]
# [80 to 91] --> 70.9 , 75.5 --> [2]

print(CustomerChoosingItemsTime)
plt.hist(CustomerChoosingItemsTime , bins=[5,10,15,20,25,30])
plt.axis([0,35,0,5])

plt.xlabel('Seconds')
plt.ylabel('Customers')
plt.title('Reliance Fresh Timing Details')
# plt.savefig('E:\MatPlotlib Forsk\Histogram2.jpg')

plt.show()
--------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

CustomerChoosingItemsTime = [20.2,30.2,35.4,40.6,45.8]
CustomerChoosingItemsTime.sort()

print(CustomerChoosingItemsTime)
plt.hist(CustomerChoosingItemsTime , bins=[10,20,30,40,50])
plt.axis([0,55,0,5])

plt.xlabel('Seconds')
plt.ylabel('Customers')
plt.title('Reliance Fresh Timing Details')
# plt.savefig('E:\MatPlotlib Forsk\Histogram1.jpg')

plt.show()
------------------------------------------------------------------------------------------------------

































