import os
import numpy as np 
import pandas as pd 

s = pd.Series([1,2,3,np.nan,6,8])

#print(s)

dates = pd.date_range('20230401',periods=6)
#print(dates[0])

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
#print(df)

df2 = pd.DataFrame({
    'A':1.,
    'B':pd.Timestamp('20230401'),
    'C':pd.Series(1, index=list(range(4)), dtype='float32'),
    'D':np.array([3]*4, dtype='int32'),
    'E':pd.Categorical(["test", "train", "test", "train"]),
    'F':'foo'
    })

print(df2)
