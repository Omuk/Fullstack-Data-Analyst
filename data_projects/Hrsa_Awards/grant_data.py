import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

#if its the first time working with excel, import the 'pip install xlrd and openpyxl' as well, it reads excel files

#A Personal advice before starting the project is to just look at the excel file. Sometimes when I do, I start formulating hypothesis not related to the study

        #1. Import the file. TO Avoid going nuts, either open the folder directly from files or use the pwd to read the path. Then use the path exactly as it is
            #Almost went nuts all the time until i accepted this hard truth
                # a)if its just one sheet ----

df = pd.read_excel(r'C:\Github\Fullstack-Data-Analyst\data_projects\Hrsa_Awards\grant_data.xlsx')
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
print(df.info())
print(df)

