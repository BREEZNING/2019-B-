import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv('消费特点.csv',encoding='gbk',index_col='CardNo') #读取数据
model = KMeans(n_clusters=3,n_jobs=4,max_iter=500) #分为3类，并发数4，最大迭代次数为500
model.fit(data) #开始聚类

#打印结果
r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(data.columns) + ['类别数目'] #重命名表头
print(r)

#给每个学生标记群体
r = pd.concat([data, pd.Series(model.labels_,index=data.index)],axis=1)  #详细输出每个样本对应的类别
r.columns = list(data.columns) + ['聚类类别'] #重命名表头

#作图
def density_plot(data):
    plt.rcParams['font.sans-serif'] = ['SimHei'] #正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False #正常显示负号
    p = data.plot(kind='kde',linewidth=2,subplots=True,sharex=False)
    [p[i].set_ylabel('密度') for i in range(3)]
    plt.legend()
    return plt 

for i in range(3):
    density_plot(data[r['聚类类别']==i]).savefig('群组%s.png'%(i))