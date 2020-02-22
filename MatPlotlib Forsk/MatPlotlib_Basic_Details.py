# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:10:30 2020

@author: Rajesh
"""
"""
Basics of Matplotlib
    Scatter Plot
    Line Plot
    Pie Chart
    Bar Chart
"""
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]

y = [1,2,3,4,5,6,7,8,9,10]

# Setting the title
plt.title('A Line Graph')

# Setting the X Label 
plt.xlabel('x')

# Setting the Y Label
plt.ylabel('y')

# Displaying the Grid
plt.grid(True)
# plt.grid(False)

# Changing the x axes limits of the scale.
plt.xlim(0,10)

# Changing the y axes limits of the scale
plt.ylim(0,10)

#OR 

plt.axis([0,10,0,10])

# Showing the points on the graph.
plt.scatter(x,y)

# Simple Line plot
plt.plot(x,y) # Stright Line will be coming.

# To save the plot Image.
plt.savefig('E:\MatPlotlib Forsk\scatter.jpg')

plt.show()

-----------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

x = [10,20,30,40,50,60,70]

y = [100,200,300,400,500,600,700]

# Setting the title
plt.title('Forsk coding school')

# Setting the X Label 
plt.xlabel('No.of week')

# Setting the Y Label
plt.ylabel('Monthly Increment')

# Displaying the Grid
plt.grid(True)
# plt.grid(False)

# Changing the x axes limits of the scale.
# plt.xlim(0,10)

# Changing the y axes limits of the scale
# plt.ylim(0,10)

#OR 

# plt.axis([0,10,0,10])

# Showing the points on the graph.
plt.scatter(x,y)

# Simple Line plot
plt.plot(x,y) # Stright Line will be coming.

# To save the plot Image.
plt.savefig('E:\MatPlotlib Forsk\scatter1.jpg')

plt.show()

----------------------------------------------------------------------------

# Changing the color of the line.

plt.plot(x,y,color='green') # #000000
plt.plot(x,y,color='blue') # #000000
plt.plot(x, y, color="#FF0000") # #000000

# Changing the style of the line.
plt.plot(x,y,linestyle='dashed') # solid dashed  dashdot dotted
----------------------------------------------------------------------------------
# For Plotting Scatter Plot.
plt.plot(x ,y , 'd' , color = 'red') # D --> Dimons shape points.

plt.savefig('E:\MatPlotlib Forsk\scatter1.jpg')

plt.show()

plt.plot(x ,y , 'd' , color = 'yellow') # D --> Dimons shape points.

NOTE :- There are so many patterns to print the line . ( o  .  , x  +  v  ^  <  >  s d )

plt.plot(x ,y , 'o' , color = 'red') # o --> oval shape points.

plt.plot(x ,y , '.' , color = 'red') # . --> Dotted  shape points.

plt.plot(x ,y , ',' , color = 'red') # , --> very small shape points.

plt.plot(x ,y , 'x' , color = 'red') # x --> x  shape points.

plt.plot(x ,y , '+' , color = 'red') # + --> + operator shape points.

plt.plot(x ,y , 'v' , color = 'red') # v --> Diamond bottom shape points.

plt.plot(x ,y , '^' , color = 'red') # ^ --> Dimond Top  shape points.

plt.plot(x ,y , '<' , color = 'red') # < --> Dimond Left side shape points.

plt.plot(x ,y , '>' , color = 'red') # > --> Dimons Right side shape points.
 
plt.plot(x ,y , 's' , color = 'red') # s --> square shape points.
--------------------------------------------------------------------------------------------------
# Scatter Plot with scatter method.

plt.scatter(x, y, marker='.', color='black',label="marker='{0}'".format('.')); # o  .  , x  +  v  ^  <  >  s d 
plt.legend(numpoints=1)
plt.legend(numpoints=2)

NOTE :- There are so many patterns to print the line . ( o  .  , x  +  v  ^  <  >  s d )

plt.scatter(x, y, marker='o', color='blue',label="marker='{0}'".format('0'))


plt.scatter(x, y, marker='d', color='green',label="marker='{0}'".format('0'))

-------------------------------------------------------------------------------------------------------



























         
         






































