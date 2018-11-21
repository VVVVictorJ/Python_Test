import pandas as pd

data=pd.read_excel(r'C:\Users\Pasto\Desktop\etar.xlsx',sheet_name='Sheet3')
data.rename(columns={'赛事':'A','独赢':'B','全场 - 让球':'C','全场 - 大小':'D','单双':'E','胜负':'F'},inplace=True)
data=data[['A','B','C','D','E','F']]

i=1
j=1.24
getizhi=[]
all=38

for z in range(0,25):
    count=data['B'][(data.F==1)&(data.B>i)&(data.B<j)].value_counts()
    i=j
    j=j+0.04
    ll=len(count)
    if ll>0:
        jisuan='precent: {:.2f}%'.format(count[0]/all)
    else:
        continue
    print(jisuan)
    getizhi.append(jisuan)

print(getizhi)