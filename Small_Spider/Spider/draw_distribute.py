import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

data=pd.read_excel(r'C:\Users\Pasto\Desktop\etar.xlsx',sheet_name='Sheet3')
data.rename(columns={'赛事':'A','独赢':'B','全场 - 让球':'C','全场 - 大小':'D','单双':'E','胜负':'F'},inplace=True)
data=data[['A','B','C','D','E','F']]
data=data[['B','F']][data.F>=-1]
#坐标轴移动
ax = plt.gca()
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data',0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data',0))
#取消显示上，右边框
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')


plt.grid()
#设置图片大小
fig=matplotlib.pyplot.gcf()
fig.set_size_inches(18.5,10.5)
#y轴设置
plt.yticks([-1,0,1],
          ['L','D','W'])
#x轴设置0-15，10个点
# new_ticks=np.linspace(0,15,10)

# for tick in ax.xaxis.get_major_ticks():
#     tick.label1.set_fontsize(1)

# plt.xticks(new_ticks)
xmajorLocator   = MultipleLocator(2) #将x主刻度标签设置为20的倍数
xmajorFormatter = FormatStrFormatter('%1.1f') #设置x轴标签文本的格式
xminorLocator   = MultipleLocator(0.1) #将x轴次刻度标签设置为5的倍数

ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)

ax.xaxis.set_minor_locator(xminorLocator)

ax.xaxis.grid(True, which='minor') #x坐标轴的网格使用主刻度
plt.xticks
plt.scatter(data.B,data.F)
fig.savefig(r'C:\Users\Pasto\Desktop\distribute.png',dpi=300)
plt.show()