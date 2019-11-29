import pandas as pd 

df = pd.read_csv('../result/task1_2_1.csv',encoding='gbk',usecols=[1,2,4,5,7,11])
df = df[df['Type']=='消费'] #筛选出类别为消费的数据

#计算本月人均刷卡频次和人均消费额
def f():
    total = len(set(df['PeoNo'].values)) #计算学生总数
    print('本月人均刷卡频次：{}次'.format('%d' % (df['Index'].count()/total)))
    print('本月人均消费额：{}元'.format('%.2f' % (df['Money'].sum()/total)))

#不同专业不同性别学生群体的消费情况
def h():
    group = df.groupby(['Major','Sex']) #按专业性别分组
    print(group['Money'].sum(),group.size())
    print(group['Money'].sum()/group.size())

f()