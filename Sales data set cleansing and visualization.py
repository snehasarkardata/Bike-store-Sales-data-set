#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[13]:


sales = pd.read_csv('sales_data.csv')
sales.head()


# In[14]:


sales['Customer_Age'].mean()


# In[16]:


sales['Customer_Age'].plot(kind='kde',figsize=(14,8))


# In[23]:


sales['Customer_Age'].plot(kind='box',vert=False ,figsize=(30,40))


# In[25]:


#Mean of the order quantity

sales['Order_Quantity'].mean()


# In[32]:


sales['Order_Quantity'].plot(kind='hist', bins=30, figsize=(14,6))


# In[31]:


sales['Order_Quantity'].plot(kind='box', vert=False, figsize=(14,6))


# In[33]:


# How many sales per year do we have?
sales['Year'].value_counts()


# In[34]:


sales['Year'].plot(kind='box', vert=False, figsize=(14,6))


# In[35]:


sales['Year'].plot(kind='hist', bins=30, figsize=(14,6))


# In[38]:


# How many sales per month do we have?
sales['Month'].value_counts().plot(kind='hist', figsize=(6,6))


# In[62]:


#Which country has the most sales quantity of sales?
sales['Country'].value_counts().head(1)


# In[70]:


sales['Country'].value_counts().plot(kind='bar',figsize=(14,6))


# In[72]:


#Create a list of every product sold
sales['Product'].unique()


# In[74]:


#Create a bar plot showing the 10 most sold products (best sellers):
sales['Product'].value_counts().head(10).plot(kind='bar', figsize=(14,6))


# In[78]:


#Can you see any relationship between Unit_Cost and Unit_Price?
sales.plot(kind='scatter',x='Unit_Cost',y='Unit_Price',figsize=(6,6))


# In[79]:


#Can you see any relationship between Order_Quantity and Profit?
sales.plot(kind='scatter',x='Order_Quantity',y='Profit',figsize=(6,6))


# In[81]:


#Can you see any relationship between the Customer_Age per Country?
sales[['Customer_Age','Country']].boxplot(by='Country',figsize=(10,6))


# In[83]:


#Can you see any relationship between Profit per Country?
sales[['Profit','Country']].boxplot(by='Country',figsize=(6,6))


# In[86]:


#Add and calculate a new Calculated_Date column

sales['Calculated_Date'] = sales[['Year', 'Month', 'Day']].apply(lambda x:  '{}-{}-{}'.format(x[0], x[1], x[2]), axis=1)
sales['Calculated_Date'].head()


# In[88]:


#How did sales evolve through the years?
sales['Calculated_Date'].value_counts().plot(kind='line',figsize=(15,6))


# In[ ]:


# Increase 50 U$S revenue to every sale
sales['Revenue']+=50


# In[91]:


#How many orders were made in Canada or France?
sales.loc[(sales['Country']=='Canada') | (sales['Country']=='France')].shape[0]


# In[100]:


#How many Bike Racks orders were made from Canada?
sales.loc[(sales['Country'] == 'Canada') & (sales['Sub_Category'] == 'Bike Racks')].shape[0]


# In[104]:


#How many orders were made in each region (state) of France?
france_states= sales.loc[sales['Country']=='France','State'].value_counts()
france_states


# In[110]:


france_states.plot(kind= 'bar', figsize=(14,6))


# In[112]:


#How many sales were made per category?
sales['Product_Category'].value_counts()


# In[118]:


sales['Product_Category'].value_counts().plot(kind='pie',figsize=(4,6))


# In[130]:


#How many orders were made per accessory sub-categories?
accesories = sales.loc[sales['Product_Category']=='Accesories','Sub_Category'].value_counts()

accesories


# In[135]:


accessories.plot(kind='bar', figsize=(14,6))


# In[143]:


#How many orders were made per bike sub-categories?

bikes=sales.loc[sales['Product_Category']=='Bikes','Sub_Category'].value_counts()
bikes

#bikes = sales.loc[sales['Product_Category'] == 'Bikes', 'Sub_Category'].value_counts()


# In[144]:


bikes.plot(kind='pie',figsize=(6,6))


# In[149]:


#Which gender has the most amount of sales?
sales['Customer_Gender'].value_counts()


# In[151]:


sales['Customer_Gender'].value_counts().plot(kind='pie',figsize=(6,6))


# In[152]:


#How many sales with more than 500 in Revenue were made by men?
sales.loc[(sales['Customer_Gender'] =='M') & (sales['Revenue']== 500)].shape[0]


# In[155]:


#Get the top-5 sales with the highest revenue
sales.sort_values(['Revenue'],ascending=False).head(5)


# In[163]:


#Get the sale with the highest revenue
#sales['Revenue'].max()
cond=sales['Revenue'].max()
sales.loc[cond]


#cond = sales['Revenue'] == sales['Revenue'].max()
#sales.loc[cond]


# In[166]:


#What is the mean Order_Quantity of orders with more than 10K in revenue?

cond = sales['Revenue'] > 10_000

sales.loc[cond, 'Order_Quantity'].mean()


# In[167]:


#What is the mean Order_Quantity of orders with less than 10K in revenue?
ond = sales['Revenue'] < 10_000

sales.loc[ond, 'Order_Quantity'].mean()


# In[168]:


#How many orders were made in May of 2016?
cond = (sales['Year'] == 2016) & (sales['Month'] == 'May')

sales.loc[cond].shape[0]


# In[ ]:


#How many orders were made between May and July of 2016?


# In[169]:


cond = (sales['Year'] == 2016) & (sales['Month'].isin(['May', 'June', 'July']))

sales.loc[cond].shape[0]


# In[171]:


# Add 7.2% TAX on every sale Unit_Price within United States
#sales.loc[sales['Country'] == 'United States', 'Unit_Price'] = sales.loc[sales['Country'] == 'United States', 'Unit_Price'] * 1.072

sales.loc[sales['Country'] == 'United States', 'Unit_Price'] *= 1.072


# In[ ]:




