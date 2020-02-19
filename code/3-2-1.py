import pandas as pd 

#对每位学生的最大消费间隔天数单独进行统计
def f(df):
    maxDay = {}
    for no in set(df['CardNo']):
        df2 = df[df['CardNo']==no]
        df2.index = df2['CardNo']
        df2 = df2.sort_values(by='Date') #将该名学生的消费数据按消费时间升序排列
        #逐个比较，得出相邻两次消费的最大消费间隔天数
        maxdate = 0
        for i in range(1,len(df2)):
            day = (df2.iloc[[i],[1]]-df2.iloc[[i-1],[1]]).loc[no,'Date'].days
            if day > maxdate:
                maxdate = day
        maxDay[no] = maxdate

    return maxDay

df = pd.read_csv('../appendix/data2.csv',encoding='gbk',usecols=['CardNo','Date','Money','CardCount','Type','Dept'])
df = df[df['Type']=='消费']
df['Date'] = pd.to_datetime(df['Date'])
df1 = df.groupby(['CardNo'])
#得出每位学生四月份的消费总金额
money = df1['Money'].sum()
#得出每位学生四月份的消费总次数
totalCount = df1['CardNo'].count()
#得出每位学生四月份最大消费间隔天数
maxDay = f(df)
s1 = pd.Series(maxDay)

data = pd.concat([s1,totalCount,money],axis=1)
data.to_csv('消费特点.csv')