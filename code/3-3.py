import pandas as pd 
import matplotlib.pyplot as plt

#提取低消费学生的学号
df = pd.read_csv('julei.csv',encoding='gbk',index_col='CardNo')
df = df.sort_values(by='Money') #按消费总额升序排列
length = int(len(df)*0.1) #设定提取低消费学生的数目，为全体学生消费总额最低的前10%
df0 = df.head(length)
df0.columns = ['最大消费间隔天数','消费次数','消费总额']

#读取学生消费数据
data1 = pd.read_csv('../result/task_1_1_2.csv',encoding='gbk',usecols=['CardNo','Money','FundMoney','Surplus','Type'])
#提取低消费学生的消费和门禁数据
data1 = data1[data1['CardNo'].isin(df0.index)]

#统计低消费学生的校园卡消费存储行为数据
def f(df):
    df1 = df[df['Type']=='消费']
    df1 = df1.groupby('CardNo').mean()['Money']
    df2 = df[df['Type']=='存款']
    df2 = df2.groupby('CardNo').mean()['FundMoney']
    df3 = df.groupby('CardNo').max()['Surplus']
    return df1,df2,df3

avgCost,avgFund,maxSurplus = f(data1)
df1 = pd.concat([avgCost,avgFund,maxSurplus],axis=1)
df1.columns = ['次均消费金额','次均存款金额','最大余额']

df2 = pd.concat([df0,df1],axis=1)

#绘图
def draw(data,subNum):
    plt.rcParams['font.sans-serif'] = ['SimHei'] #正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False #正常显示负号
    p = data.plot(kind='kde',linewidth=2,subplots=True,sharex=False)
    [p[i].set_ylabel('密度') for i in range(subNum)]
    plt.legend()
    plt.show() 

draw(df2,len(df2.columns))