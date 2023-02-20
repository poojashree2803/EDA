#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('d:\\crop1.csv',encoding='latin-1')
df.head()


# In[4]:


df.describe()


# In[5]:


df.info()


# In[13]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12,6)
sns.barplot(x="Item",y="Year",data=df)


# In[14]:


df.corr()


# In[15]:


sns.heatmap(df.corr())


# In[19]:


Item_name=df.Item.value_counts().index
Year_val=df.Year.value_counts().values


# In[21]:


plt.pie(Year_val[:3],labels=Item_name[:3],autopct='%1.2f%%')


# In[22]:


df


# In[23]:


df.columns


# In[ ]:




