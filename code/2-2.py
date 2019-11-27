import pandas as pd 
import datetime
import matplotlib.pyplot as plt

#判断消费日期为工作日还是非工作日
def f(x):
    if (x.weekday()<5):
        return '工作日'
    else:
        return '非工作日'

#提取消费日期中的时间部分
def w(x):
    return datetime.time(x.hour,x.minute)

def k(x):
    return pd.to_timedelta(str(x))

df = pd.read_csv('setMeal.csv',encoding='gbk',usecols=[2,5]) #读取食堂消费记录表中消费时间和同一次就餐行为标记列的数据
df = df[df['sameAction']==0] #筛选出单独一次就餐行为的数据
df['Date'] = pd.to_datetime(df['Date'])
df['WorkDay'] = df['Date'].map(f) #标记消费日期为工作日还是非工作日
df['Time'] = df['Date'].map(w) #提取消费时间

#设置时间划分区间，每半小时为一区间
cuts = []
for h in range(0,24):
    time1 = datetime.time(h)
    time2 = datetime.time(h,30)
    cuts.append(pd.to_timedelta(str(time1)))
    cuts.append(pd.to_timedelta(str(time2)))
cuts.append(pd.to_timedelta(str(datetime.time(23,59))))
groupTime = pd.cut(df['Time'].map(k),cuts)

#按消费时间每半小时和工作日非工作日分组，计算每个时段的消费人数
group = df.groupby([groupTime,'WorkDay'])
df2 = pd.DataFrame(group.size())
df2 = df2.unstack()
df2 = df2.fillna(0)

#绘图
plt.rcParams['font.sans-serif']=['SimHei'] #设置正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #设置正常显示负号
df2.plot(title='工作日和非工作日食堂不同时间就餐人次折线图')
plt.show()