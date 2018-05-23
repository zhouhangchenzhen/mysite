# # # ##uple是长度固定，不可改变的序列。创建元祖的方法是用逗号
# # # tup=4,5,6
# # # print(tup)
# # # nested_tup=(4,5,6),(7,8)
# # # print(nested_tup)
# # # tuple([4,0,2])
# # # print(tuple([4,0,2]))
# # # tup_str=tuple('string')
# # # # print(tup_str)
# # # # tup_str1=tuple(['foo',[1,2],True])
# # # # print(tup_str1)
# # # # tup_str1[1].append(3)
# # # # s=(4,None,'for')+(6,0)+('bar',)
# # # # print(s)
# # # # s1=('zhou','hang')*4
# # # # print(s1)
# # # #
# # # # ##unpacking tuples 取出元组
# # # # tup=(4,5,6)
# # # # a,b,c=tup
# # # # ##
# # # # print(a)
# # # # print(b)
# # # # print(c)
# # #
# # # tup1=4,5,(6,7),'fuck'
# # # a,b,(c,d),e=tup1
# # # print(a)
# # # print(b)
# # # print(c)
# # # print(d)
# # # print((c,d))
# # # print(e)
# # # tmp=a
# # # a=b
# # # b=tmp
# # # print(a)
# # ##python中有更简洁的交换变量名称的做法
# # # b,a=a,b
# # # print(a)
# # ##这种unpacking通常用在迭代序列上
# # # seq=[(1,2,3),(4,5,6),(7,8,9)]
# # # for a,b,c in seq:
# # #     print('a={1},b={0},c={2}'.format(a,b,c))
# # ##另外一种更高级的unpacking方法只提取tuple开头几个元素，剩余元素直接赋予给*rest
# # # values='god',1,2,3,'True'
# # # print(values)
# # # a,b,*rest=values
# # # print(a)
# # # print(b)
# #
# # #print(rest)会报错，因为rest是你想丢弃的，名字本身无所谓
# # #a,b,c=values 也会报错
# #
# # ######################
# # #tuple methods 元组方法
# # ######################
# #
# # ##由于tuple大小和内容不能改变，因此方法也很少，count用来计算某个数值出现的次数，list中也有这个方法
# # # a=(1,2,2,"count",True)
# # # print(a)
# # # print(a.count(2))
# # # print(a.count(True))  ##为什么这个现实出现了两次？？
# # # print(a.count(False))  ##为什么这个现实出现了两次？？
# #
# # ######################
# # #list 列表
# # ######################
# #
# #
# # ##list的灵活性更强，大小和内容都可以改变
# # a_list=[2,3,7,None]
# # tup=('god','love','you')
# # b_list=list(tup)
# # print(a_list,b_list)
# # print(b_list[1])
# # b_list[1]='miss'
# # print(b_list)
# #
# # ##list 具有现化迭代器或生成器
# # gen =range(10)
# # print(gen) ## 这是一个迭代器，无法看到里面的内容
# # print(list(gen)) ##list 具现化后就可以观察到
# # ##添加或者移除元素
# #
# # ##append把元素加在最后面
# # b_list.append('and your family')
# # ##insert将元素插入到特定位置
# # b_list.insert(0,'Almighty')
# # print(b_list)
# # ##pop 是insert的反向操作，能够删除序列中特定位置的元素
# # b_list.pop(0)
# # print(b_list)
# # ##remove可以通过移除指定的element，如果同一个值在序列中出现了多次，可以实现只移除第一个
# # b_list.append("god")
# # b_list.remove("god")
# # print(b_list)
# # ##检查一个值是否在list中，用in
# # print('god' in b_list)
# # ##合并list
# # c_list=a_list+b_list
# # print(c_list)
# # ##append不剩添加多个元素，多个元素用extend
# # d_list=a_list.extend([7,8,(2,3)])
# # print(d_list)
# # import numpy as np
# # from sklearn.datasets import make_blobs
# # blobs=1
# # blob=make_blobs(n_samples=1000,n_features=2,centers=blobs,cluster_std=1.5,shuffle=True,random_state=5)
# # ##robust covariance estimate
# # from sklearn.covariance import EllipticEnvelope
# # robust_covariance_est=EllipticEnvelope(contamination=0.1).fit(blob[0])
# # detection=robust_covariance_est.predict(blob[0])
# # outliers=np.where(detection==-1)
# # inliers=np.where(detection==1)
# # import matplotlib.pyplot as plt
# # plt.plot(blob[0][:,0],blob[0][:,1],'x',markersize=10,color='red',alpha=0.8)
# # plt.show()
# #
# # import matplotlib.pyplot as plt
# # input_values=list(range(1,1001))
# # ##
# # squares=[input_value**3 for input_value in input_values]
# # plt.plot(input_values,squares,linewidth=5)
# # ##设置图表标题，并给坐标轴加上标签
# # plt.title('square numbers',fontsize=24)
# # plt.xlabel('input_value',fontsize=20)
# # plt.ylabel('squares',fontsize=20)
# # #设置刻度标记的大小
# # plt.tick_params(axis='both',labelsize=14)
# # plt.scatter(input_values,squares,c=squares,cmap=plt.cm.Blues,edgecolor='none',s=200)#c=red 设置数据点点颜色
# # #colormap 颜色映射
# # plt.savefig('squares_plot.png',bbox_inches='tight')
# #
# #
# # ##
# # from random import choice
# #
# #
# # class RandomWalk():
# #     """一个生成随机漫步的类"""
# #
# #     def __init__(self, num_points=5000):
# #         """初始化随机漫步的属性"""
# #         self.num_points = num_points
# #         ##所有随机漫步都始于（0，0）
# #         self.x_values = [0]
# #         self.y_values = [0]
# #
# #     def fill_walk(self):
# #         while len(self.x_values) < self.num_points:
# #             x_direction = choice([1, -1])
# #             x_distance = choice([0, 1, 2, 3, 4])
# #             x_step = x_direction * x_distance
# #
# #             y_dirction = choice([1, -1])
# #             y_distance = choice([0, 1, 2, 3, 4])
# #             y_step = y_dirction * y_distance
# #             ##拒绝原地踏步
# #             if x_step and y_step == 0:
# #                 continue
# #             ##计算下一个x和y的值
# #             next_x = self.x_values[-1] + x_step
# #             next_y = self.y_values[-1] + y_step
# #
# #             self.x_values.append(next_x)
# #             self.y_values.append(next_y)
# #
# #
# # import matplotlib.pyplot as plt
# #
# # ##模拟多次随机漫步
# # m = 0
# # keep_running = int(input("Make how many walk?:"))
# # while m < keep_running:
# #     rw = RandomWalk()
# #     rw.fill_walk()
# #     num_points = list(range(rw.num_points))
# #     plt.scatter(rw.x_values[0], rw.y_values[0], c='black', s=100)
# #     plt.scatter(rw.x_values, rw.y_values, c=num_points, cmap=plt.cm.Blues, s=15)
# #     plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
# #     m += 1
# # ##隐藏坐标轴
# # plt.figure(figsize=(100, 60))
# #
# # from random import randint
# #
# #
# # class Die():
# #     """表示一个骰子的类"""
# #
# #     def __int__(self, num_sides=6):
# #         self.num_sides = num_sides
# #
# #     def roll(self):
# #         """返回一个位于1和骰子面数之间的随机值"""
# #         return randint(1, self.num_sides + 1)
# #
# #
# # die = Die()
# # ##掷骰子并将结果存在一个列表中
# # results = []
# # for roll_num in range(100):
# #     result = die.roll()
# #     results.append(result)
# # frequencies = []
# # for value in range(1, die.num_sides):
# #     frequency = results.count(value)
# #     frequencies.append(frequency)
# # ##绘制直方图
# # import pygal
# #
# # # 分析摇骰子的结果
# # hist = pygal.Bar()
# # hist.title = "摇🎲的直方图"
# # hist.x_labels = ['1', '2', '3', '4', '5', '6']
# # hist.y_labels = "骰子频数"
# # from sklearn import datasets
# # X,y=datasets.make_classification(n_samples=10**6,n_features=10,random_state=101)
# # import random
# # a=random.randint(0,100)
# # print(a)
#
# # #
# # from sklearn  import datasets
# # from sklearn.feature_selection import SelectKBest,f_regression
# # from sklearn.linear_model import LinearRegression
# # from sklearn.svm import SVR
# # from sklearn.ensemble import RandomForestClassifier
# # boston_dataset=datasets.load_boston()
# # x=boston_dataset.data
# # y=boston_dataset.target
# #
# # print(boston_dataset.keys())
# # seletor=SelectKBest(f_regression,k=1)
# # seletor.fit(x,y)
# # x_sl=x[:,seletor.get_support()]
# # print(x_sl.shape)
# # print(x_sl)
# # regressor=LinearRegression(fit_intercept=True,normalize=True)
# # regressor.fit(x_sl,y)
# from sklearn import datasets
# iris=datasets.load_iris()
# print(iris.data)
# print(iris.DESCR)
# print(iris.data.shape)
# print(iris.feature_names)
# print(iris.target)
# print(iris.target.shape)
# print(iris.target.names)
# import pandas as pd
# import numpy as np
# colors=list()
# palette={0:"red",1:"green",2:"blue"}
# for c in np.nditer(iris.target):colors.append(palette[int(c)])
# dataframe=pd.DataFrame(iris.data,columns=iris.feature_names)
# scatterplot=pd.scatter_matrix(dataframe,alpha=0.3,figsize=(10,10),diagonal='hist',colors=colors,marker='o',grid=True)
# iris_head=iris.head()
# print(iris_head)
#
#
# %matplotlib inline
# import matplotlib.pyplot as plt
# from sklearn import datasets
# from sklearn.feature_selection import SelectKBest,f_regression
# from sklearn.linear_model import LinearRegressor
# from sklearn.svm import SVR
# from sklearn.ensemble import RandomForestRegresor
# boston_dataset=datasets.load_boston()
# x_full=boston_dataset.data
# y=boston_dataset.target
import pygame