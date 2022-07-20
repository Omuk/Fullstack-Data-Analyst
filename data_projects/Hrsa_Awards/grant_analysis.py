#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
from sklearn.impute import SimpleImputer
import io 


# In[3]:


df = pd.read_excel(r'C:\Github\Fullstack-Data-Analyst\data_projects\Hrsa_Awards\grant_data.xlsx')


# In[4]:


df


# In[6]:


df.columns = df.columns.str.replace(' ', '')


# In[7]:


df


# In[ ]:


df = df.astype({'AwardYear': 'int64', 'GrantSerialNumber': 'int64', 'ProjectPeriodStartDate': 'datetime64[ns]', 'DataWarehouseRecordCreateDate': 'datetime64[ns]', 'GrantProgramDescription': 'object', 'DUNSNumber': 'float64', 'UniqueEntityIdentifier' : 'object', 'GeocodingArtifactAddressPrimaryXCoordinate': 'float64', 'GeocodingArtifactAddressPrimaryYCoordinate': 'float64'})


# In[ ]:


df['GrantProjectPeriodEndDate'] = pd.to_datetime(df['GrantProjectPeriodEndDate'], errors='coerce')


# In[8]:


df.info()


# In[10]:


df.isna().sum() * 100 /len(df)


# In[16]:


aft_dropdf = df.drop(columns = ['GrantProgramDescription', 'UniformDataSystemGrantProgramDescription'])


# In[17]:


aft_dropdf.isna().sum() * 100 /len(df)


# In[22]:


sns.histplot(aft_dropdf['GeocodingArtifactAddressPrimaryYCoordinate'], color='blue')


# In[26]:


sns.histplot(aft_dropdf['GeocodingArtifactAddressPrimaryXCoordinate'], color='blue')


# In[30]:


sns.histplot(aft_dropdf['DUNSNumber'], color='orange')


# In[33]:


sns.histplot(aft_dropdf['U.S.-MexicoBorderCountyIndicator'], color='red')


# In[36]:


sns.histplot(aft_dropdf['GrantProgramDirectorE-mail'], color='lime')


# In[39]:


sns.histplot(aft_dropdf['GrantProgramDirectorPhoneNumber'], color='yellow')


# In[40]:


sns.histplot(aft_dropdf['GranteeStateAbbreviation'], color='blue')


# In[43]:


sns.histplot(aft_dropdf['GranteeZIPCode'], color='blue')


# In[ ]:






