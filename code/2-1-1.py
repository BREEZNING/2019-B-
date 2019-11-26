import pandas as pd 

#筛选出在食堂就餐的数据
def choose():
    df = pd.read_csv('../result/task_1_1_2.csv',encoding='gbk',usecols=['Index','PeoNo','Date','Type','Dept'])
    df = df[df['Type']=='消费']
    #筛选出地点在食堂的数据
    df = df[df['Dept'].isin(['第一食堂','第二食堂','第三食堂','第四食堂','第五食堂','教师食堂'])]
    df.to_csv('mealData.csv',encoding='gbk',index=False)


#标记同一次就餐行为
def mark():
    df = pd.read_csv('mealData.csv',encoding='gbk')
    df['Date'] = pd.to_datetime(df['Date'])
    students = list(set(df['PeoNo'].values)) #获取所有学生的学号
    #对每个学生查看同一次就餐行为的消费记录
    for student in students:
        di = df[df['PeoNo']==student]
        didians = di['Dept'] #获取该学生就餐过的食堂
        #对该学生就餐过的每个食堂查看同一次就餐行为的消费记录
        for didian in list(set(didians.values)):
            detail = di[di['Dept']==didian] #获取该学生在当前查看食堂的消费记录
            indexs = detail.index.values #获取消费记录的索引
            #如果学生在当前食堂的消费记录只有一条，标记该条记录为单独的一次就餐行为
            if len(indexs) == 1:
                df.loc[indexs,'sameAction'] = 0
            '''
            如果学生在当前食堂的消费记录大于一条，因消费记录的顺序是按时间排列的，
            故逐一比较当前记录与上一条消费记录的时间差，时间差小于一小时，
            则标记当前记录为同一就餐行为
            '''
            else:
                for i in range(0,len(indexs)):
                    if i==0:
                        df.loc[indexs[0],'sameAction'] = 0
                    else:
                        meal = detail.loc[indexs[i],'Date']
                        meal2 = detail.loc[indexs[i-1],'Date']
                        delta = meal-meal2
                        if (delta.days==0 and abs(delta.seconds)<=3600):
                            df.loc[indexs[i],'sameAction'] = 1
                        else:
                            df.loc[indexs[i],'sameAction'] = 0
        print(student)
    df.to_csv('../result/setMeal.csv',encoding='gbk',index=False)