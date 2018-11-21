import pandas as pd
from pandas import DataFrame
import numpy as np
data=pd.read_excel(r'C:\Users\Pasto\Desktop\etar.xlsx',sheet_name='Sheet3')
data.rename(columns={'赛事':'A','独赢':'B','全场 - 让球':'C','全场 - 大小':'D','单双':'E','胜负':'F'},inplace=True)
data=data[['A','B','C','D','E','F']]
data=data[['A','B','C','D','E']][data.F>0]
print(data.fillna(0))
