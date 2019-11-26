import pandas as pd
import matplotlib.pyplot as plt 

'''
绘制各大食堂就餐人次占比饼图
'''

#根据消费时间划分早中晚餐类型
def f(x):
    if (x.hour < 11):
        return '早餐'
    elif (x.hour >= 11 and x.hour < 17):
        return '午餐'
    elif (x.hour >= 17):
        return '晚餐'
    else:
        return '非正餐'

df = pd.read_csv('setMeal.csv',encoding='gbk')
df = df[df['sameAction'] == 0] #选出为单独一次就餐行为的消费记录
df['Date'] = pd.to_datetime(df['Date'])
df['Meal'] = df['Date'].map(f) #生成具体早中晚餐的消费
group1 = df.groupby(['Meal','Dept'])
group2 = df.groupby(['Dept'])
df1 = pd.DataFrame(group1.size())
df1.columns = ['就餐人次']
df2 = pd.DataFrame(group2.size())
df2.columns = ['就餐人次']
#将晚餐在教师食堂的就餐人数设置为0，方便作图
df3 = pd.DataFrame({'就餐人次':0},index=pd.MultiIndex.from_product([['晚餐'],['教师食堂']]))
df1 = pd.concat([df3,df1])

#绘图
plt.rcParams['font.sans-serif']=['SimHei'] #设置正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #设置正常显示负号
df2.plot(kind='pie',autopct='%.2f%%',title='各大食堂总就餐人次占比饼图',subplots=True)
plt.legend(loc=3, borderaxespad=0)
plt.savefig('../result/各大食堂总就餐人次占比饼图.png')
df1.loc['早餐'].plot(kind='pie',autopct='%.2f%%',title='各大食堂早餐就餐人次占比饼图',subplots=True)
plt.legend(loc=3, borderaxespad=0)
plt.savefig('../result/各大食堂早餐就餐人次占比饼图.png')
df1.loc['午餐'].plot(kind='pie',autopct='%.2f%%',title='各大食堂午餐就餐人次占比饼图',subplots=True)
plt.legend(loc=3, borderaxespad=0)
plt.savefig('../result/各大食堂午餐就餐人次占比饼图.png')
df1.loc['晚餐'].plot(kind='pie',autopct='%.2f%%',title='各大食堂晚餐就餐人次占比饼图',subplots=True)
plt.legend(loc=3, borderaxespad=0)
plt.savefig('../result/各大食堂晚餐就餐人次占比饼图.png')
plt.show()
