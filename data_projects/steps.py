# 1. Import python libraries and pip install xlrd

# 2. Import the data

# 3.Get Initial information

# 4. Display the first 5 and last 5 observations, number of variables and observations, Variables names and their data types (info has most of this, this is good practice)

# 5. Get the characteristics of the dataset

# 6. Modify the column name and or White-spaces as needed. Remember its crucial since you may have to select individual columns later.

# 7. Change the data types as appropriate for the study based on the study.

# 8. Find if there is any unique values within the columns. Alternatively, the values can be observable i.e. $9 or #9 or (9) 

# 9. Decide what to do with the unique values if any

#                                     MISSING VALUES 
# 10. Get sum of missing data by column 
# 11. Find Missing values by percentage (shows importance of missing data).

# 12.Decide the importance of including the missing data in the study (high missing values might indicate less importance/skew data)

#                                 WHat To Do
# 13. Replace all missing data with NaN or just specific column 
#                                 Specific 
#                                 All 

# 14. Drop all missing data or just specific column 
#                                 Specific 
#                                 All 
# 15. Impute all missing data or just specific column with either Mean, Mode or Median
#                                 Specific 
#                                 All 
# 16. Perform a Front-fill or a Backfill of all or specific column 
#                                 Specific 
#                                 All 
#                                     DUPLICATES VALUES 
# 17. Find duplicates in the data 
# 18. Decide wether to drop or keep  all or specific duplicates 
#                                 Drop specific duplicates 
#                                 Drop All duplicates 

#                                     CHECK FOR ZEROES 
# 19. Check if the number zero exists in the file (important because the 0 can have a meaning or just indicate empty) --eg Age(0) or row is empty(0)
# 20. Decide to keep or drop the Zero
#                                 Drop Specific zeros 
#                                 Drop All columns with zeroes 
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

                                    
#                                     DATA VISUALIZATIONS