#!/usr/bin/env python
# coding: utf-8

# ### 1.write python code to create array in different ways

# In[2]:


import numpy as np


# In[3]:


# method 1

arr = np.array([20,30,40,50,60])
arr


# In[8]:


# method 2 using tuple

arr = np.array((1,2,3,4,5))
arr


# In[4]:


# method -  np.zeros()-array filled with all zeros

arr = np.zeros(5)
arr


# In[5]:


# method - np.ones()-array filled with all ones

arr = np.ones(5)
arr


# In[6]:


# method - np.arange()-array filled with regularly spaced values


arr = np.arange(1,10)
arr


# In[7]:


# method - np.linspace()-array filled with evenly spaced values

arr = np.linspace(1,10,4)
arr


# ### 2.array creation

# #### a.create a 1D Numpy array containing the first 12 positive integer as arr1

# In[96]:


arr1 = np.arange(1,13)
arr1


# In[97]:


len(arr1)


# In[98]:


id(arr1)


# In[99]:


type(arr1)


# #### b.create a 1D Numpy array1 with 20 elements containing  integer between 0 and 12 using linspace

# In[100]:


arr2 = np.linspace(1,12,20)
arr2


# In[101]:


len(arr2)


# In[102]:


type(arr2)


# In[103]:


id(arr2)


# ### 3.find all attributes of arr1 and arr2

# #### arr1

# In[11]:


arr1.dtype  # dtype-data type of array


# In[14]:


arr1.size  # size-no.of elements


# In[15]:


arr1.nbytes  #nbytes-memory occupied by array


# In[16]:


arr1.itemsize #itemsize-memory occupied by each item


# #### arr2

# In[17]:


arr2.dtype  # dtype-data type of array


# In[18]:


arr2.size  # size-no.of elements


# In[19]:


arr2.nbytes #nbytes-memory occupied by array


# In[20]:


arr2.itemsize #itemsize-memory occupied by each item


# ### 4.apply measure and describe the data(attribue and statistics) to above arrays using Numpy

# ### arr1

# In[59]:


arr1


# In[67]:


np.mean(arr1) # mean-avg


# In[24]:


np.median(arr1) # median-middle value


# In[81]:


Range =  max(arr1) - min(arr1) # range-max-min
Range


# In[82]:


np.var(arr1)  # variance-how data values spread from mean


# In[83]:


np.std(arr1)  # standard deviation-deviating from mean


# In[84]:


Q1 = np.percentile(arr1,25)  # IQR = Q3-Q1
Q3 = np.percentile(arr1,75)
IQR = Q3 - Q1
IQR


# In[85]:


lower_limit = Q1 - (1.5)*(IQR)
print("lower_limit:",lower_limit)
upper_limit = Q3 + (1.5)*(IQR)
print("upper_limit:",upper_limit)


# In[86]:


print(arr1[arr1>upper_limit])  # outlier-there is no outliers in arr1
print(arr1[arr1<lower_limit])


# ### arr2

# In[87]:


arr2


# In[88]:


np.mean(arr2)  # mean-avg


# In[89]:


np.median(arr2) # median-middle value


# In[90]:


np.var(arr2)  # var- how data values spread from mean


# In[91]:


np.std(arr2) # std-deviating from mean


# In[92]:


Range = max(arr2) - min(arr2) # Range-max-min
Range


# In[93]:


Q3 = np.percentile(arr2,75) 
Q1 = np.percentile(arr2,25)  # Range = max-min
IQR =Q3 - Q1
IQR


# In[94]:


lower_limit = Q1 - (1.5)*(IQR)
print("lower_limit:",lower_limit)
upper_limit = Q3 + (1.5)*(IQR)
print("upper_limit:",upper_limit)


# In[95]:


print(arr1[arr1>upper_limit])  # outlier-there is no outliers in arr2
print(arr1[arr1<lower_limit])

