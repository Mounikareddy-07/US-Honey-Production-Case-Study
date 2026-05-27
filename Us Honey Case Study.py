#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[ ]:


dataset -- https://drive.google.com/file/d/1cyX7Piq9jEA_VR1x4BnwqgLkDChOAqe4/view


# In[3]:


df = pd.read_csv("US_honey_dataset.csv")


# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df.head()


# In[7]:


df = df.drop(columns = "Unnamed: 0")

''' Other methods '''
# df = df.drop(['Unnamed: 0'], axis = 1)

# df.drop(columns = "Unnamed: 0", inplace = True)
# df.drop(['Unnamed: 0'], axis = 1, inplace = True)


# In[8]:


df.info()


# In[9]:


df.isnull().sum()


# In[11]:


# if you want direct single answer we will use this
df.isnull().sum().sum()


# In[10]:


df.duplicated().sum()


# In[ ]:


--> the data is now absolutely clean


# In[12]:


df.to_csv("Cleaned_honey_data.csv")


# In[13]:


# Create a loop which prints the number of unique values and also the unique values inside the columns

for col in df.columns:
    print("Name of the column:",col)
    print("Number of unique values:", df[col].nunique())
    print("nunique values:",df[col].unique())
    print()


# In[ ]:


''' Find the state which appers the most number of times and mininum number of time '''


# In[14]:


# The state which is appearing most number of times in dataset
df["state"].value_counts().idxmax()               


# In[17]:


# The state which is appearing least number of times in dataset
df['state'].value_counts().idxmin()


# In[18]:


# top 5 most frequent states
df['state'].value_counts().head(5)


# In[19]:


# top 10 most frequent states
df['state'].value_counts().head(10)


# In[20]:


df['state'].value_counts()


# In[21]:


# How many percentage of rows data belongs to each state?
df['state'].value_counts(normalize=True)*100
# df['state'] -> selects the state column
# .value_counts()  -> counts how many times each state appears.
# normalize=True  -> instead of normal count ,it converts them into proportions(fractions)
# * 100 -> converts proportions into percentages.


# In[22]:


# find total honey production per state
df.groupby('state')['production'].sum()


# In[23]:


# the state with highest honey production
df.groupby('state')['production'].sum().idxmax()


# In[24]:


df.groupby('state')['production'].sum().sort_values(ascending = False)


# In[25]:


df.columns


# In[26]:


# find average yield per colony per state
df.groupby('state')['yield_per_colony'].mean()


# In[27]:


# find max and min price per state
df.groupby('state')['average_price'].max()


# In[30]:


df.groupby('state')['average_price'].max().sort_values(ascending = False).head()


# In[28]:


df.groupby('state')['average_price'].min()


# In[33]:


df.groupby('state')['average_price'].min().sort_values(ascending = False).head()


# In[35]:


df.columns


# In[36]:


''' on the basis of state column find total production per state,
    average price per state and total value of prouduction per state '''

df.groupby('state').agg({
    'production':'sum',
    'average_price':'mean',
    'value_of_production':'sum'
})


# In[38]:


# give custom_names to the columns and sort the data wrt to any column

df.groupby('state').agg(
    Total_productions = ('production','sum'),
    Average_price = ('average_price','mean'),
    Total_value = ('value_of_production','sum')
).sort_values("Total_productions", ascending = False)


# In[40]:


# find the states which are having high production but they are having low average price

df1 = df.groupby('state').agg({
    'production':'sum',
    'average_price':'mean'
})

mean_prod = df1['production'].mean()
mean_price = df1['average_price'].mean()

df1[(df1['production']>df1['production'].mean())&(df1['average_price']<df1['average_price'].mean())]
# both the commands will give same output

df1[(df1['production']>mean_prod)&(df1['average_price']<mean_price)]


# In[41]:


# which state is most efficient?
# production , yield per colony / number of colonies
# production - stock / colonies

state_eff = df.groupby('state').agg({
    'production':'mean',
    'colonies_number':'mean'
})
print(state_eff)


# In[42]:


state_eff['efficiency'] = state_eff['production']/state_eff['colonies_number']
print(state_eff)


# In[44]:


state_eff.sort_values('efficiency', ascending = False)


# In[47]:


# this method is used to ignore the decimal error
if np.allclose(df['yield_per_colony'], df['production']/df['colonies_number']):
    print("They are same")
else:
    print("the values are different and we can say that yes the yield per colony is an average value")


# In[48]:


df[['production','yield_per_colony']].corr()

