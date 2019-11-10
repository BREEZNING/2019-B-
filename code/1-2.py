import pandas as pd 

#读取三个表的数据
df1 = pd.read_csv('../result/task_1_1_1.csv',encoding='gbk',usecols=['CardNo','Sex','Major','AccessCardNo'])
df2 = pd.read_csv('../result/task_1_1_2.csv',encoding='gbk')
df3 = pd.read_csv('../result/task_1_1_3.csv',encoding='gbk')
#表连接，分别以校园卡号和门禁卡号作为连接键
data1 = pd.merge(df1,df2,on='CardNo')
data2 = pd.merge(df1,df3,on='AccessCardNo')
#保存数据
data1.to_csv('../result/task1_2_1.csv',encoding='gbk')
data2.to_csv('../result/task1_2_2.csv',encoding='gbk')