#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np 
a = np.array([[1,2,3],[5,8,7]])
print("Array created using passed list:\n",a)


# In[6]:


b = np.zeros((3,4))
print("\n An array initialized with all zeros.\n",b)


# In[8]:


c = np.full((3,3),6)
print("\n Array initialized with all 6\n",c)


# In[9]:


d = np.random.random((2,2))
print("\n A random array\n",d)


# In[12]:


e = np.arange(0,30,5)
print("\n A sequential array with step of 5.\n",e)


# In[15]:


arr = np.array([[1,2,3,4],[5,2,4,2],[1,2,0,1]])
reshaped_arr = arr.reshape (4,3)
print(arr)
print(reshaped_arr)


# In[16]:


fl_arr = arr.flatten()
print(arr)
print(fl_arr)


# In[18]:


print(arr.ndim)


# In[19]:


print (arr.shape)


# In[20]:


print(arr.size)


# In[21]:


print(arr.dtype)


# In[22]:


c = arr.astype('f')
print(c)
b = arr.astype('i')
print(b)


# In[23]:


p = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print(p[3:3])


# In[24]:


p = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
c = p.astype('i')
print(c)


# In[25]:


p = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print(p[2:,2:])


# In[ ]:




