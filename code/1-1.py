import pandas as pd 
from datetime import datetime

if __name__ == '__main__':
    for i in ['1','2','3']:
        df = pd.read_csv('../appendix/data'+i+'.csv',encoding='gbk')
        if (i == '1'):
            checkData1(df)
            data = dealData1(df)
        elif (i == '2'):
            checkData2(df)
            data = dealData2(df)
        else:
            checkData3(df)
            data = dealData3(df)
        saveData(data,i)

#查看学生ID表的异常情况
def checkData1(df):
    Card = df['CardNo'].nunique()
    AccessCard = df['AccessCardNo'].nunique()
    if (Card != len(df)):
        print('校园卡号有重复')
    if (AccessCard != len(df)):
        print('门禁卡号有重复',len(df)-AccessCard)
    #查看每列是否有空值
    print(df.isnull().any())
    #查看性别中是否有异常值
    print(set(list(df['Sex'])))
    #查看门禁卡号重复的记录
    li = []
    for i in df['AccessCardNo'].values:
        if i in li:
            data = df[df['AccessCardNo']==i]
            print(data)
        else:
            li.append(i)

#保存数据
def saveData(df,X):
    df.to_csv('../result/task_1_1_'+X+'.csv',encoding='gbk',index=False)
    print('保存成功')

#检查消费记录表的异常值
def checkData2(df):
    #查看空值
    print(df.isnull().any())
    df1 = df[df['Type']=='存款']
    df2 = df[df['Type'].isin(['取款','消费'])]
    #查看取款记录和消费记录中是否有存款金额不为0的数据
    print(df2[df2['FundMoney'] != 0])
    #查看存款记录中是否有存款金额大于余额和消费金额不为0的数据
    print(df1[df1['FundMoney']>df1['Surplus']],df1[df1['Money'] != 0])
    #查看是否有金钱小于0的数据
    print(df[df['Money']<0],df[df['FundMoney']<0],df[df['Surplus']<0])
    #查看是否有不在四月份的记录
    df['Date'] = pd.to_datetime(df['Date'])
    print(df[df['Date']>datetime(2019,4,30,23,59,59)])

#删除消费记录表的重复值
def dealData2(df):
    df1 = df.drop_duplicates()
    return df1

#查看门禁记录表的异常情况
def checkData3(df):
    #查看空值
    print(df.isnull().any())
    df1 = df[df['Describe']=='允许通过']
    df2 = df[df['Describe']=='禁止通过-没有权限']
    #查看描述与是否通过不匹配的记录
    print(df1[df1['Access']==0],df2[df2['Access']==1])
    #查看是否有不在四月份的记录
    df['Date'] = pd.to_datetime(df['Date'])
    print(df[df['Date']>datetime(2019,4,30,23,59,59)])
    #查看是否有重复的序号
    if (df['Index'].nunique() == len(df)):
        print('无重复序号')

#处理门禁记录表的重复值
def dealData3(df):
    #删除完全重复的记录
    df1 = df.drop_duplicates()
    #删除门禁卡号和时间一样的记录
    df2 = df1.drop_duplicates(['AccessCardNo','Date'])
    return df2
