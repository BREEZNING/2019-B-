import pandas as pd 

'''
单独对每个学生查看早中晚餐就餐地点是否有差别
'''

def f(x):
    if (x.hour < 11):
        return '早餐'
    elif (x.hour >= 11 and x.hour < 17):
        return '午餐'
    elif (x.hour >= 17):
        return '晚餐'
    else:
        return '非正餐'

df = pd.read_csv('../result/setMeal.csv',encoding='gbk')
df = df[df['sameAction'] == 0] #选出为单独一次就餐行为的消费记录
df['Date'] = pd.to_datetime(df['Date'])
df['Meal'] = df['Date'].map(f) #生成具体早中晚餐的消费
students = list(set(df['PeoNo'].values))

#设置早中晚餐就餐地点有无差别和无法判别的人数
DK = 0
difference = 0
indifference = 0

#对每个学生进行判断
for stu in students:
    print(stu,':')
    studentMeal = df[df['PeoNo']==stu]
    mealDict = {} #存放该学生早中晚餐就餐地点的字典
    #将该学生各餐的就餐地点放入字典
    for meal in list(set(studentMeal['Meal'].values)):
        mealDept = studentMeal[studentMeal['Meal']==meal]
        mealDeptDetail = list(set(mealDept['Dept'].values))
        mealDict[meal] = mealDeptDetail
    '''
    判断该学生各餐就餐地点是否有差别，
    若该学生各餐的就餐地点包含同一个地点，则该学生就餐地点无差别，
    若该学生只有一餐的就餐地点，则无法判别该学生就餐地点有无差别
    '''
    mealCount = mealDict.keys()
    if(len(mealCount)==0 or len(mealCount)==1 or len(mealCount)>3):
        DK += 1
    elif(len(mealCount)==2):
        value = list(mealDict.values())
        same = [x for x in value[0] if x in value[1]]
        print(same)
        if (len(same)!=0):
            indifference += 1
        else:
            difference += 1
    else:
        value = list(mealDict.values())
        same = [x for x in value[0] if (x in value[1] and x in value[2])]
        print(same)
        if (len(same)!=0):
            indifference += 1
        else:
            difference += 1

print('\n无法判别的人数：{}\n就餐地点无差别的人数：{}\n就餐地点有差别的人数：{}\n就餐地点无差别人数占比：{}%'.format(DK,
    indifference,difference,(indifference/(DK+indifference+difference))*100))