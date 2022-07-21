import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
from sklearn.impute import SimpleImputer
import io 


df = pd.read_excel(r'C:\Github\Fullstack-Data-Analyst\data_projects\Hrsa_Awards\grant_data.xlsx')

df.columns = df.columns.str.replace(' ', '')

#Change data types to desired types
df = df.astype({'AwardYear': 'int64', 'GrantSerialNumber': 'int64', 'ProjectPeriodStartDate': 'datetime64[ns]', 'DataWarehouseRecordCreateDate': 'datetime64[ns]', 'GrantProgramDescription': 'object', 'DUNSNumber': 'float64', 'UniqueEntityIdentifier' : 'object', 'GeocodingArtifactAddressPrimaryXCoordinate': 'float64', 'GeocodingArtifactAddressPrimaryYCoordinate': 'float64'})

df['GrantProjectPeriodEndDate'] = pd.to_datetime(df['GrantProjectPeriodEndDate'], errors='coerce')

#Find Missing Values by %


imputer = SimpleImputer(missing_values=np.NaN, strategy='mean')
df[['GeocodingArtifactAddressPrimaryYCoordinate']] = imputer.fit_transform(df[['GeocodingArtifactAddressPrimaryYCoordinate']])
#
# # Imputing with median value
# #
imputer_med = SimpleImputer(missing_values=np.NaN, strategy='median')
df[['GeocodingArtifactAddressPrimaryXCoordinate']] = imputer_med.fit_transform(df[['GeocodingArtifactAddressPrimaryXCoordinate']])

# #
# # Imputing with most frequent / mode value
# #
imputer_mode = SimpleImputer(missing_values=np.NaN, strategy='most_frequent')
df[['DUNSNumber']] = imputer_mode.fit_transform(df[['DUNSNumber']])

imputer_mode = SimpleImputer(missing_values=np.NaN, strategy='most_frequent')
df[['U.S.-MexicoBorderCountyIndicator']] = imputer_mode.fit_transform(df[['U.S.-MexicoBorderCountyIndicator']])
# #
# # Imputing with constant value; The command below replaces the missing
# # value with constant value such as 80
# #

his = sns.distplot(df.DUNSNumber)
print(his)

sns.histplot(aft_dropdf['GeocodingArtifactAddressPrimaryYCoordinate'], color='blue')

sns.histplot(aft_dropdf['GeocodingArtifactAddressPrimaryXCoordinate'], color='blue')

sns.histplot(aft_dropdf['DUNSNumber'], color='blue')

sns.histplot(aft_dropdf['U.S.-MexicoBorderCountyIndicator'], color='blue')

sns.histplot(aft_dropdf['GrantProgramDirectorE-mail'], color='blue')

sns.histplot(aft_dropdf['GrantProgramDirectorPhoneNumber'], color='blue')

sns.histplot(aft_dropdf['GranteeStateAbbreviation'], color='blue')

sns.histplot(aft_dropdf['GranteeZIPCode'], color='blue')












