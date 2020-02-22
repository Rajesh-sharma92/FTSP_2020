# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:56:16 2020

@author: Rajesh
"""
"""
Mean, Median, Mode

Let's create some fake income data, centered around 27,000 
with a normal distribution and standard deviation of 15,000, with 10,000 data points. 
Then, compute the mean (average)
"""
import numpy as np
                          # mean, sd, total
incomes = np.random.normal(27000, 15000, 10000)
#loc=150, scale=20, size=1000

print (type(incomes)) # <class 'numpy.ndarray'>
print(incomes.size) # 10000
print (incomes)
print (len(incomes)) # 10000
print (incomes.ndim) # 1
print (incomes.shape) # (10000,)
print (incomes.dtype) # float64

print("Mean value is: ", np.mean(incomes)) # 27226.15240457021
print("Median value is: ", np.median(incomes)) # 27460.591779782546


from scipy import stats
print("Mode value is: ", stats.mode(incomes)[0])
 

print("Minimum value is: ", np.min(incomes))
print("Maximum value is: ", np.max(incomes))
print("Standard Deviation is: ", np.std(incomes))
#print("Correlation coefficient value is: ", np.corrcoef(incomes))



#We can segment the income data into 50 buckets, and plot it as a histogram:
import matplotlib.pyplot as plt
plt.hist(incomes, 20)
plt.show()


#box and whisker plot to show distribution
#https://chartio.com/resources/tutorials/what-is-a-box-plot/
plt.boxplot(incomes)

# Explain NumPy_boxplot.png


print("Mean value is: ", np.mean(incomes))
print("Median value is: ", np.median(incomes))

#Adding Bill Gates into the mix. income inequality!(Outliers)
incomes = np.append(incomes, [10000000000])

#Median Remains Almost SAME
print("Median value is: ", np.median(incomes))

#Mean Changes distinctly
print("Mean value is: ", np.mean(incomes))

      
# Give an example for bincount function
# num = np.bincount(incomes).argmax()
