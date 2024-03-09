#!/usr/bin/env python
# coding: utf-8

# #  MACHINE LEARNING & PATTERN RECOGNITION PROJECT 

#                                                                                         PRESENTED BY : FAUZIYA KHATOON

# # #TOPIC : QR WORLD RAKING UNIVERSITY

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("cwurData.csv")             # read_csv() function is used to read data from a CSV file named "cwurData.csv"


# In[3]:


df


# # # Taking Sampling

# In[4]:


p= df.sample(620)          #sample() function is used to randomly select the number of rows from the DataFrame.
p


# #  #  Exploratory Data Analysis (EDA)

# In[5]:


p.describe().T    #  to display statistics discription  of numeric columns of a DataFrame


# In[6]:


p.info()   #  to display information about column data types and missing values.


# In[7]:


p.count()           #count() method is used  to count occurrences or occurrences of a particular element.


# In[8]:


p.isnull().sum()           # check the number of  NULL VALUES , broad_impact have 55 NULL VALUES


# ## SORTING 

# In[9]:


p.sort_index()     #  this method is used to sort the rows of a DataFrame


# # #MAX & MIN DATA

# In[10]:


p.max()


# In[11]:


p.min()


# # # DATA VISUALIZATION 

# In[12]:


s=df.sample(20)
s


# In[13]:


d=pd.DataFrame(s['year'].value_counts())     #value_counts() function count the unique values from column "year".
d.reset_index(inplace=True)                 
d


# In[14]:


plt.figure(figsize=(10,10,))
plt.plot(d["year"],d["index"])               # how many times each year appears in the 'year' column
plt.style.use("seaborn-white")


# In[15]:


d=pd.DataFrame(s['country'].value_counts())
d.reset_index(inplace=True)     3                         #how many times each country appears in the 'country' column
d


# In[ ]:


plt.figure(figsize=(10,10,))
plt.plot(d["country"],d["index"])
plt.style.use("seaborn-white")   


# In[ ]:


sns.violinplot(x='quality_of_education', y='year', data=s)


# # # CONCLUSION 

# 1.From this Data Analysis, we get to know about the universities ranking  in world & at national level.
# 

# 2.Analysing tha various graphs between different parameters of universities.

#                             

#                                             
