#!/usr/bin/env python
# coding: utf-8

# # Making an Example Histogram Plot

# Given some randomly distributed data, bin the data to create a histogram using matplotlib. See PME Ch 10.

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


#Create some random data

#Specify number of data points
n = 500

x = np.random.randn(n) #Generate random data

#Create the histogram bins
width = 0.5
histmin = np.floor(min(x))
histmax = np.ceil(max(x)) + width

bins = np.arange(histmin, histmax, width)
plt.hist(x, bins=bins, alpha = 0.5, edgecolor = "black")
plt.ylabel("N per bin")
plt.xlabel("x")
plt.savefig("exampleHistogram.png", bbox_inches = "tight", facecolor = "white")


# In[ ]:




