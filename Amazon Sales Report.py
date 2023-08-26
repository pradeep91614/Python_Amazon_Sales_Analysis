#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns


# In[ ]:





# In[2]:


df=pd.read_csv("F:\python-data analysis (Data)\Amazon Sale Report (1).csv")


# In[3]:


df


# In[4]:


df.info()


# In[6]:


df.shape


# In[9]:


df.head(10)


# In[8]:


df.tail()


# In[10]:


df.drop(['New','PendingS'],axis =1,inplace = True)


# In[11]:


df


# In[12]:


df.info()


# In[13]:


pd.isnull(df)


# In[14]:


pd.isnull(df).sum()


# In[15]:


df.shape


# In[16]:


df.dropna(inplace=True)


# In[17]:


df.shape


# In[18]:


df.columns


# In[20]:


df[' ship-postal-code']=df['ship-postal-code'].astype('int')


# In[21]:


df[' ship-postal-code'].dtype


# In[22]:


df.info()


# In[23]:


df['Date']= pd.to_datetime(df['Date'])


# In[24]:


df.info()


# In[25]:


df


# In[30]:


df.columns


# In[33]:


df.rename(columns={'Qty':'Quantity'},inplace=True)


# In[34]:


df.columns


# In[36]:


df.describe()


# In[38]:


df.describe(include='object')


# In[39]:


df.columns


# In[46]:


ax=sns.countplot(x='Size',data=df)


# In[49]:


ax=sns.countplot(x='Size',data=df)
for count in ax.containers:
    ax.bar_label(count)


# In[59]:


df.groupby(['Size'],as_index=False)['Quantity'].sum().sort_values(by='Quantity',ascending=False)


# In[63]:


x=df.groupby(['Size'],as_index=False)['Quantity'].sum().sort_values(by='Quantity',ascending=False)
sns.barplot(x='Size',y='Quantity',data=x)


# In[71]:


sns.countplot(data=df,x='Courier Status',hue='Status')


# In[ ]:





# In[75]:


import seaborn


# In[94]:


plt.figure(figsize=(10,5))

x=sns.countplot(data=df, x='Courier Status',hue= 'Status')

plt.show()


# In[80]:


df['Size'].hist()


# In[81]:


df['Category'] = df['Category'].astype(str)
column_data = df['Category']
plt.figure(figsize=(10, 5))
plt.hist(column_data, bins=30, edgecolor='Black')
plt.xticks(rotation=90)
plt.show()


# In[82]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[95]:


df['Category'] = df['Category'].astype(str)
column_data = df['Category']
plt.figure(figsize=(10, 5))
plt.hist(column_data, bins=15, edgecolor='Yellow')
plt.xticks(rotation=90)
plt.show()


# In[100]:


B2B_check = df['B2B'].value_counts()
B2B_check


# In[104]:


plt.pie(B2B_check,labels=B2B_check,autopct='%1.1f%%')
plt.show()


# In[ ]:





# In[108]:


x_data = ['Category']  
y_data = df['Size'] 

# Plot the scatter plot
plt.scatter(x_data, y_data)
plt.xlabel('Category ')  
plt.ylabel('Size')  
plt.title('Scatter Plot') 
plt.show()


# In[122]:


plt.figure(figsize=(14,6))
sns.countplot(data=df,x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=90)
plt.show()


# In[128]:


top_10=df['ship-state'].value_counts().head(10)
plt.figure(figsize=(10,6))
sns.countplot(data=df[df['ship-state'].isin(top_10.index)],x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=40)
plt.show()


# In[ ]:




