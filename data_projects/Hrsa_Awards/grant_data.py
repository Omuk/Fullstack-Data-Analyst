import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

#if its the first time working with excel, import the 'pip install xlrd and openpyxl' as well, it reads excel files

#A Personal advice before starting the project is to just look at the excel file. Sometimes when I do, I start formulating hypothesis not related to the study

        #1. Import the file. TO Avoid going nuts, either open the folder directly from files or use the pwd to read the path. Then use the path exactly as it is
            #Almost went nuts all the time until i accepted this hard truth
                # a)if its just one sheet ----

df = pd.read_excel(r'C:\Github\Fullstack-Data-Analyst\data_projects\Hrsa_Awards\grant_data.xlsx',)
            #If more than one sheet
# df_sheet0 = df.parse(0)
# df_sheet1 = df.parse(1)
            #to align to the right---- variable = (path, skipinitialspace=True) or 'skip_blank_lines=True
                #b) if you want a specific file
                    #data = pd.read_excel(r'Pathname', sheet_name='Name of Sheet')
#print(df)
        #2. While beginner level its advised to print the data, I suggest going straight to info
    #df.info()
            #The info gets you how many columns, names of the columns, data types, the memory size, num rows.
            #You can get shape, tail, or head if you want but I prefer the info style information
            #Also go back and compare with excel files the data especially data types as those are ones we gonna be using
        
        #3.Another useful tool is to describe the data
    # desc=df.describe
    # print(desc)
            # This function is almost similar to the info only that its simpler and shows rows instead of columns

        #4. The first thing I saw in my data is that columns have spaces, as a programmer I know that can't work as so its the
                # the firs thing I will take care of 
            #a) Modify all Columns Titles
df.columns = df.columns.str.replace(' ','') #I chose no space but you can choose another filler
            #b) Modify specific Columns Titles
                # df.rename(columns = {'Abstract': 'Abunuwasi'}, inplace=True)
            #c) Rename all the columns
                # df.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6']
                    # Only rename if you are sure coz it's a hustle if dealing with large data sets with multiple sheets
# df.info()

# ------IF YOU ALREADY KNOW WHAT YOU WANT FROM THE DATA, USE THE FOLLOWING STEPS TO CHANGE DATA TYPES. IF NOT YOU CAN STILL CHANGE THE TYPES BASED ON WHAT YOU VISUALIZE ON EXCEL
        #5.
            #First am going to find there are columns with unwanted characters 
for col in df.columns:

    #print('{} : {}'.format(col,df[col].unique()))
    pass
            #I am doing nothing with the data provided, but you can either remove, replace or impute the unique data AFTER CONVERTING THE COLUMN INTO A STRING
            # Lets assume one of the columns had a $ sign this what I would have done
                # df['column name'] = df['column name].str.replace ('$', '')
                        # OR
                # for column in df.column:
                #   df[column name] = df[column name].str.replace('$', '', regex=True)
        #6. CHANGING DATA TYPES
            # a) TO NUMERIC WHEN DECIMAL/NEGATIVE IS WORTHLESS ***ONLY USE IF SURE '1.2' THE DECIMAL IS USELESS --- 1.2=12, 1.23=123
                # WHOLE DOCUMENT
                    # df = pd.to_numeric
                # SPECIFIC COLUMN
                    # df['column name'] = df['column name'].str.replace(r'\W','')
            # b)CHANGE EVERYTHING TO DESIRED DATA TYPE
df = df.astype(str) #or (int, ,datetime, float)
            # c)

df = df.astype({'AwardYear': 'int64', 'GrantSerialNumber': 'int64', 'ProjectPeriodStartDate': 'datetime64[ns]', 'GrantProjectPeriodEndDate': 'str', 'DataWarehouseRecordCreateDate': 'datetime64[ns]', 'GrantProgramDescription': 'object', 'DUNSNumber': 'float64', 'UniqueEntityIdentifier' : 'object', 'GeocodingArtifactAddressPrimaryXCoordinate': 'float64', 'GeocodingArtifactAddressPrimaryYCoordinate': 'float64'})
                # Again why its important to look at the data is The Grant Program end date is a string when it should be a DateFrame Format. Also, the Grant Program Description is an integer, I don't know why by I am converting it to a string(This will be helpful when am using SQL and Access to query the data)
            # d)In above case, I could not override the Grant Project Period End Date so I am going to try it manually

df['GrantProjectPeriodEndDate'] = pd.to_datetime(df['GrantProjectPeriodEndDate'], errors='coerce')


            #----THE COERCE FUNCTION FORCES PYTHON TO IGNORE ERROR AND CAN BE USED ANYWHERE AS LONG AS YOU KNOW OF ERROR. IN OUR NEW FILE, THE ERROR WILL BE SHOWN AS NaT(because the 64ns only allows upto 584 years, NaT is found if values are over 584 years)


        # ----- FIND ANY MISSING OR DUPLICATED DATA
        #7. Find null or empty values by percentage --- less than 6% is ideal for analysis
                #a) Find total columns with missing values
mis_num = df.isna().any().sum()
                #b) Find which columns has the missing values 
mis_num = df.isna().any()

                #c) Find how many values are missing per column
mis_num = df.isna().sum()

                #******* OR
                #d) F
mis_row = df.isnull().any().sum()
                #e) Find which rows has the missing values 
mis_row = df.isna().any()

                #f) Find how many values are missing per column
mis_row = df.isna().sum()
            # -------FIND MISSING VALUES BY PERCENTAGE
df.isnull().sum() / df.shape[0]*100
# mis_row = df.isnull().sum() * 100 / len(df)
mis_col = df.isna().sum() * 100 / len(df)
# print(mis_data)
            # ^^ shape[0] refers to rows but second option is much cleaner

        #8) Find if the number zero (0) is among the data
check_zero = df.isin([0]).sum()
# print(check_zero)
            #^^ Above values has no zero


        #8.Find any Duplicates in the data
df.duplicated().sum()

        #DECIDE WHAT TO DO WITH THE DATA
        #9.My data has no duplicates, but if I could either ignore them, drop them all, or keep the first or last
# dup_dat = df.drop_duplicates()
        # OR
# dup_dat = df.drop_duplicates('Column Name', keep='first')
        #Lastly I would want to reset my data
# new_data = dup_dat.reset_index(drop=True)

# ######################################################################### ---WHAT TO DO WITH MISSING DATA#############################################################################
#         #10. Before starting to work with missing values, I like to look for values that should not exist, example are '?, -, .' 
# for col in df.columns:
#     # print('{} : {}'.format(col,df[col].unique()))
#     pass

#             # Now this file unique values are expected so am not going to do anything. However lets say '?' was in a column somewhere that it should not be there
# for col in df.columns:
#     df[col].replace({'?':np.nan},inplace=True)


#         #10.With some columns missing data, I could either drop the columns, fill the data with either mean, mode, top value or bottom value
# for col in df.columns:
#     df[col].replace({'?':np.nan},inplace=True)


#         #11.Now the real magic begins
#             #a) Drop duplicates and return new file
# df.drop_duplicates  #OR
# df.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False) #OR ---Subset is column name, --Keep ('first', 'last', 'False) =>False drops all duplicates, --inplace => bool to keep changes or return a copy of new file, ignore => bool of returns new index
#             #***If I wanted to select which subsets I will do it like this

# # df.drop_duplicates(subset=['colname', 'colname2'], keep='first', inplace=False, ignore_index=False)

#             #b)Drop Empty values if they have no meaning
# df.dropna()

#         #Drop specific column (lets say has more than 6%)
# #df.drop(columns='colum name') or columns =['col1', 'col2']

#         #Drop if a NA is found in a column
# df = df.dropna(axis= 0, how='any', thresh=2, subset=None, inplace=False) # ==> axis 0/index --rows, 1--columns, how=>'any' or 'all', thresh=> threshold keep non na values(keep only rows with 2 or more non-NA), inplace=> bool where True happens to current DataFrame while return a copy

#             #c)You could replace missing data if any with zero
# for column in df:
#     df[column].where(df[column] !=0, inplace=True)
#     #If you skipped line b and did line c, the NaN would be replaced by zero
#     pass
#             #d)You can also create bool values by

#             #-------FILLING MISSING DATA
#             #e)
#                 #Filling with specific data --- Really advised to use a distribution plot to decide method of fillna

# # df['column name'].fillna(12, inplace = True)
# # df.fillna(12,inplace=True)
#             #   Fill a specific index
# # df.loc[2,'column name'] = 25

#             #  Fill with Mean -- for entire frame, works if all dtypes are numeric
# col_mean = round(df['column name'].mean(),2)
# df['column name'].fillna(col_mean, inplace=True)
#             # Fill with Median   --for entire frame, works if all dtypes are numeric
# col_med = round(df['column name'].median(),2)
# df['column name'].fillna(col_med, inplace=True)     
#             #  Fill with Mode  -- can be done with mean or mode

# col_mod = df['column name'].mode()
# df['column name'].fillna(col_mod, inplace=True)   

#             #f) Using Front fill or Backfill
#                 #a)Back Fill
# df = df['column name'].bfill(inplace=True)

#                 #b)Front Fill
# df = df['column name'].ffill(inplace=True)
#                 #c) Front or Back fill for entire document
# df.fillna(method='backfill', inplace=True)
# df.fillna(method='ffill', inplace=True)

#                 #d) Impute using Machine Learning
# # Impute with SimpleImputor from the sklearn library
# from sklearn.impute import SimpleImputer
#     # define the imputer
# impu_sklrn = SimpleImputer(missing_values=np.nan, strategy='mean') #mean
# df[['column name']] = impu_sklrn.fit_transform(df[['column name']])

# # For Categorical data, strategy = 'most_frequent'

#                 # Replacing empty categorical values
# df.fillna({'column name':'None'}, inplace=True)
#                 # Replacing empty numerical values
# df.fillna({'column name':0}, inplace=True)

#         #12. ---SAVE THE DATA CLEANED OUT, ANOTHER CATEGORICAL, NUMERICAL
#             #b) Save Categorical
# cate_data = df.select_dtypes(exclude= ['float64', 'int64'])
#             #c) Save Numerical Data
# nume_data = df.select_dtypes(include= ['float64', 'int64'])
#             #a) Save the data so you don't reinvent the whole wheel
# df.to_csv('cleaned_hrsa.csv')
# df.to_excel('cleaned_hrsa_data.xlsx')

# cate_data.to_csv('cleaned_hrsa_categorical.csv')
# cate_data.to_excel('cleanedexcel_hrsa.xlsx')

# nume_data.to_csv('cleaned_hrsa_numerical.csv')
# nume_data.to_excel('cleanedexcel_hrsa_numerical.xlsx')
# # print(df.info())

his = sns.boxplot(df['GrantProjectPeriodEndDate'], color='lime')
print(his)

