#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymysql import connect


# In[2]:


import pandas as pd


# In[3]:


data_base=connect(host='localhost',user='root',password='root')


# In[4]:


cur=data_base.cursor()


# In[5]:


query='show databases'


# In[6]:


cur.execute(query)


# In[8]:


data_bases=cur.fetchall()


# In[10]:


for data in data_bases:
    print(data)


# In[16]:


data_base=connect(host='localhost',user='root',password='root',database='wscube')
cur=data_base.cursor()
query='show tables'
cur.execute(query)
tables=cur.fetchall()
for table in tables:
    print(table)


# In[20]:


query='select * from wscube.emp'


# In[21]:


cur.execute(query)


# In[22]:


df=pd.read_sql(query,data_base)


# In[23]:


display(df)


# In[24]:


df.head(5)


# In[ ]:




