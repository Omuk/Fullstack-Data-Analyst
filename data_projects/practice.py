import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

work_proj = pd.read_excel(r'C:\full_stack\eda\Workforce_Projections_Full_Data.xlsx', sheet_name=['WithStateDetail', 'NoStateDetail'])

das = work_proj.parse(sheet_name='WithStateDetail')
print(das)

proj = pd.ExcelFile(r'C:\full_stack\eda\Workforce_Projections_Full_Data.xlsx')

proj0 = proj.parse(0)
proj1 = proj.parse(1)

# print(proj0)
# # print(proj1)

