import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
from sklearn.impute import SimpleImputer
import io 

df = pd.read_excel(r'C:\Github\Fullstack-Data-Analyst\data_projects\Hrsa_Awards\current_hrsa_award.xlsx')

df.columns = df.columns.str.replace(' ', '')

df.info()

df['City&State'] = df['GranteeCity'] + ',' + df['GranteeStateAbbreviation']

city = df['City&State']
df = df.drop(columns=['City&State'])
df.insert(loc=3, column='City&State', value=city)

df['GranteeZIPCode'] = df['GranteeZIPCode'].astype(str).str.pad(5, side='left', fillchar='0')

df['GranteeZIPCode'] = df['GranteeZIPCode'].str.replace('00nan', '00000')

df[['ZipCode', 'ZipCodeExt']] = df.GranteeZIPCode.str.split(pat='-', n=1, expand=True)

df.drop(columns=['ZipCodeExt', 'GranteeZIPCode'], inplace=True)

df.rename(columns={'ZipCode': 'GranteeZipCode'}, inplace=True)

zip = df['GranteeZipCode']
df =df.drop(columns=['GranteeZipCode'])
df.insert(loc=4, column='GranteeZipCode', value=zip)

mis_col = df.isna().sum() * 100 / len(df)
mis_col.sort_values(ascending=False)

df.drop(columns=['CCN', 'UniformDataSystemGrantProgramDescription', 'GrantProgramDirectorPhoneNumber'], inplace=True)

df.info()

cat_df = df.select_dtypes(exclude=['float64', 'int64']).columns

cat_df

df = df.astype({'ProjectPeriodStartDate': 'datetime64[ns]', 'ProjectPeriodStartDateTextString': 'datetime64[ns]', 'GrantProjectPeriodEndDate': 'datetime64[ns]', 'GrantProjectPeriodEndDateText': 'datetime64[ns]', 'DataWarehouseRecordCreateDate': 'datetime64[ns]', 'DataWarehouseRecordCreateDateText' :'datetime64[ns]'})

hist_dist = df.hist(bins=20, figsize=(25,15))

