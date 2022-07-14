data = pd.read_csv(r'C:\full_stack\eda\amun_amazon.csv', skip_blank_lines=True)

#                                RENAMING THE COLUMNS
# Replacing header with space ---- replace(' ', '') or character ---replace(' ', '_')
data.columns = data.columns.str.replace(' ', '')

#Renaming specific column
data.rename(columns = {'OrderDate':'Order_Date'}, inplace=True)
#Renaming All columns
        # data.columns = ['a', 'b', 'c', 'd', '5'....]

# Replacing specific characters e.g. $ with blank



# If Data has potential whitespace at begging or end(data is not aligned) --- column data
df = pd.read_csv(r'C:\full_stack\eda\amun_amazon.csv', skipinitialspace=True)
    # or
df = pd.read_csv(r'C:\full_stack\eda\amun_amazon.csv', skip_blank_lines=True)

# Display the first 5 Observations

data.head()

# Display the last 5 Observations
dt=data.tail()

# Display Number of Variables and Observations
ds=data.shape

# Display the Variable Names and their Data Types
df=data.dtypes




# Getting columns with just numbers (Numerical categories)
data_num = data.select_dtypes(include= ['float64', 'int64'])

# Getting Categorical columns
data_num = data.select_dtypes(exclude= ['float64', 'int64'])

# Count number of non-empty values aka missing values

data.count()

# Get the characteristics of the dataset

data.describe()

# Get categorical characteristics of entire data

data.describe(include='all')

# Getting snapshot of (rows, columns, dtypes, memory usage, column names, non-null count, ) //Complete summary of dataframe


# HANDLING MISSING VALUES

# data.TotalCharges = pd.to_numeric(data.Total Charged, errors='coerce') ---the coerce replaces all num-numeric values with NaN
# data = pd.to_numeric(data, errors='coerce')

# return number of missing values in dataset
data.isnull().sum()
        # print(data.isnull().sum())

# Drop Variable

data.dropna(how='any',inplace=True)
        # print(data.isnull().sum())

# Drop Observation

# Mean, mode or median imputation 


# Find Duplicate Data ---- check the bottom
data.duplicated().sum()
            # print(data.duplicated().sum())


# Find Unique data as a whole or within a column
data['Subtotal'].unique()

        # print(data['Subtotal'].unique()) --- result is [] if empty or [], dtype=


# Splitting into two columns Values -- e.g. address with city and country or zipcode 97001-2033 to 97001 and 2033


        # data [['ZipCode', 'AddedZip']] = data['ShippingAddressZip'].str.split('-',expand=True)  --- only works if column has same length as key

# Change Data Type
        # Interger
data['Subtotal'] = data['Subtotal'].astype('int')

        # Boolean
data['OrderStatus'] = data['OrderStatus'].astype('bool')

        # Float
data['TotalCharged'] = data['TotalCharged'].astype('bool')   

        # date format change
data['Order_Date'] = pd.to_datetime(data['Order_Date'], format='%Y%m%d')

        # string
data['BuyerName'] = data['BuyerName'].astype('str') 

data.info()


# Find missing numbers by percentage to determine importance

data.isnull().sum() /data.shape[0] *100

# ^^^ The shape[0] refers to rows

# Get Mode of within a column

            # data.Column.value_counts()


# Drop All duplicates

data = data.drop_duplicates()

# or data=data.drop_duplicates('Column', keep='first')
data = data.reset_index(drop=True)

#Checking for wrong entries like symbols -,?,#,*,etc.
for col in data.columns:
    print('{} : {}'.format(col,data[col].unique()))

# ^^^lets say we found a ? which is unique--replace it with NaN
for col in data.columns:
    data[col].replace({'?':np.nan},inplace=True)

##is null function returns zero if complete or num if uncomplete
miss_row = df_train.isnull().sum()
# print(miss_row)

miss_col = df_train.isna().any()
# to get the list of everythin ---miss_col = df_train.isna() can even add .sum() 

#Checking if the number zero exists in the file(important if the zero has a meaning or its just empty)
check_zero = df_train.isin([0]).sum()
# print(check_zero)

#Dropping duplicates
nodup = df_train.drop_duplicates() #or
nodup2 = df_train.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
# print(nodup2)

#Working with Null
#. 1 --> You Can drop them
df_train.dropna()  #----Drops rows and returns a new file
print(df_train)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>WORK ON DROPNA FROM FILE>>>>>>>>>>>>>>>>>>>>>
#. 2 --> You Can forward fill
#. 3 --> You can backfill
#. 4 --> You can fill using the mean value

### Look for text values in file --PY needs to change text to num. i.e. Yes-1 and No-0

dat.replace(np.nan, '0', inplace=True)


# 2. Import the data
data = pd.read_csv(r'C:\full_stack\eda\amun_amazon.csv', skip_blank_lines=True)

# 3.Get Initial information
# data.info()

# # 4. Display the first 5 and last 5 observations, number of variables and observations, Variables names and their data types (info has most of this, this is good practice)
# data.head()
# data.tail()
# data.shape


# # 5. Get the characteristics of the dataset
# # data.describe

# # 6. Modify the column name and or White-spaces as needed. Remember its crucial since you may have to select individual columns later.
#                 # Rename All Columns
data.columns = data.columns.str.replace(' ', '')
#                 # Rename Specific Columns
# data.rename(columns = {'OrderDate':'Order_Date'}, inplace=True)

#                 # Rename All Columns
#         # data.columns = ['a', 'b', 'c', 'd']
#                 # Take out the specific dollar signs 
# data ['TotalCharged'] = data['TotalCharged'].str.replace('$','')
#             # OR
# # data = pd.to_numeric
#                 # Take out all special characters when decimal point is worthless
#         # data ['TaxCharged'] = data['TaxCharged'].str.replace(r'\W','')
#                 # Take all rest specific dollar signs - first make entire table a string
# data=data.astype(str)

# for column in data.columns:
#     data[column] = data[column].str.replace('$', '',regex=True)

# # 7. Change the data types as appropriate for the study based on the study.
#                 # Interger
# data = data.astype({'TotalCharged':'float64', 'TaxCharged':'float64', 'ShippingCharge':'float64', 'TaxBeforePromotions':'float64', 'TotalPromotions':'float64',})
# data['Subtotal'] = data['Subtotal'].astype('float64')


# # 8. Find if there is any unique values within the columns. Alternatively, the values can be observable i.e. $9 or #9 or (9) 

# for col in data.columns:
#     pass
#     # print('{} : {}'.format(col,data[col].unique()))

# # 9. Decide what to do with the unique values if any --- if ? was the one found
#         # If found replace with NAY
# for col in data.columns:
#     data[col].replace({'?':np.nan}, inplace=True)

#                                     MISSING VALUES 
# 10. Get sum of missing data by column 
data.isnull().sum()
# print(data.isnull().sum())
def missing_cols(data):
    total = 0
    for col in data.columns:
        missing_vals = data[col].isnull().sum()
        total += missing_vals
        if missing_vals !=0:
            print(f"{col}-- has {data[col].isnull().sum()} missing data")
    if total == 0:
        print('Data has no missing data')
print(missing_cols(data))
# 11. Find Missing values by percentage (shows importance of missing data).

def perc_missing(data):
    for col in data.columns:
        pct = data[col].isna().mean() * 100
        if (pct !=0):
            print('{}-- missing rate is {}%'.format(col, round(pct,2)))
print(perc_missing(data))

# 12.Decide the importance of including the missing data in the study (high missing values might indicate less importance/skew data)
            # As a general rule, less than 10% missing data can still be stratisfied

#                                 WHat To Do
# 13. Replace all missing data with NaN or just specific column 
#                                 Specific 
colsToDrop = ['PurchaseOrderNumber', 'GroupName']
data.drop(colsToDrop, axis=1, inplace=True)
        # print(perc_missing(data))
        # data.info()
#                                 All 

# 14. Drop all missing data or just specific column 
#                                 Specific 
data['GroupName'].dropna(inplace=True)
#                                 All 
data.dropna()
            # print(data)
# 15. Impute all missing data or just specific column with either Mean, Mode or Median

#                                 Specific 
col_mean = round(data['TotalCharged'].mean(),2)
data['TotalCharged'].fillna(col_mean, inplace=True)

col_median = round(data['TotalCharged'].median(),2)
data['TotalCharged'].fillna(col_median, inplace=True)
#                                 All 

# 16. Perform a Front-fill or a Backfill of all or specific column 
#                                 Specific 
data['TotalCharged'].bfill(inplace=True)
data['TotalCharged'].ffill(inplace=True)
#                                 All 
data.fillna(method='backfill', inplace=True)
data.fillna(method='ffill', inplace=True)

# Impute with SimpleImputor from the sklearn library
from sklearn.impute import SimpleImputer
    # define the imputer
impu_sklrn = SimpleImputer(missing_values=np.nan, strategy='mean') #median
data[['TotalCharged']] = impu_sklrn.fit_transform(data[['TotalCharged']])
        # For Categorical data, strategy = 'most_frequent'

                # Replacing empty categorical values
data.fillna({'BuyerName':'None'}, inplace=True)
                # Replacing empty numerical values
data.fillna({'TaxCharged':0}, inplace=True)
#                                     DUPLICATES VALUES 
# 17. Find duplicates in the data 
# 18. Decide wether to drop or keep  all or specific duplicates 
#                                 Drop specific duplicates 
data.drop_duplicates(subset='BuyerName')
#                                 Drop All duplicates 
data.drop_duplicates()
                                    # Drop all but keep last occurances
data.drop_duplicates(subset=['BuyerName', 'CarrierName&TrackingNumber'], keep='last') #or keep 'first'

#                                     CHECK FOR ZEROES 
# 19. Check if the number zero exists in the file (important because the 0 can have a meaning or just indicate empty) --eg Age(0) or row is empty(0)
data.isin([0]).sum()
print(data.isin([0]).sum())
# 20. Decide to keep or drop the Zero
#                                 Drop Specific zeros 
#                                 Drop All columns with zeroes
for column in data:
    data[column].where(data[column] !=0, inplace=True)
    print('zeros replaced by NaN') 
# 21. Run describe. Based on info decide whether to assign values to numbers or strings -- e.g. (Yes=1 and No=0 or Neutral = 0, Good=1, Bad=2) or (0=Yes and 1=No)
#                                 Change specific columns 
#                                 Change All specific columns 
# 22. Drop unnecessary specific to the study 

# 23. Decide whether you need to assign a variable distinguishing between numerical or categorical data
#                             Categorical Data 
#                             Numerical Data 
# 24. Reset the entire Cleaned data (process)

# 25. Compare the new dataset to original by running both describe and info functions

#                                 BASIC MATH
# 26. The describe function provides instant solutions to basic math problems. To avoid complacency run this formulas for all numerical data or specific
#                             Total
#                             Mean
#                             Mode
#                             Median 
#                             25th, 50th, 75th percentile
#                             0.5, or 0.95%
#                             Central Tendency
#                             Five Number Summary
#                             Variance and Standard Deviation

# print(data.describe) 
# data.info()
                                # SORT THE VALUES
data.sort_values('BuyerName', inplace=True)
#   --------------------------------------SAVE THE CLEANED DATA AS EXCEL FOR FUTURE ANALYSIS WITHOUT REINVENTING WHOLE PROCESS
# data.to_csv('cleaned_amazon.csv')
# data.to_excel('cleaned_amazon_practice.xlsx')
#                                     DATA VISUALIZATIONS