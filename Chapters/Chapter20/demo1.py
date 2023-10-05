# -*- coding: utf-8 -*-
# @Time    : 2023/3/29 下午5:34
# @Author  : lizheng
# @FileName: demo1.py.py
# @Software: PyCharm
import cv2

import numpy as np

import matplotlib.pyplot as plt

# 用于训练的数据

# rand1数据位于(0,30)

rand1=np.random.randint(0,30,(20,2)).astype(np.float32)

# rand2数据位于(70,100)

rand2=np.random.randint(70,100,(20,2)).astype(np.float32)

# 将rand1和rand2拼接为训练数据

trainData=np.vstack((rand1,rand2))

# 数据标签，共两类：0和1

# r1Label对应着rand1的标签，为类型0

r1Label=np.zeros((20,1)).astype(np.float32)

# r2Label对应着rand2的标签，为类型1
r2Label=np.ones((20,1)).astype(np.float32)

tdLable=np.vstack((r1Label,r2Label))

# 使用绿色标注类型0

g=trainData[tdLable.ravel()==0]

plt.scatter(g[:,0],g[:,1],80,'g','o')

# 使用蓝色标注类型1

b=trainData[tdLable.ravel()==1]

plt.scatter(b[:,0],b[:,1],80,'b','s')

# plt.show()

# test为用于测试的随机数，该数在0到100之间

test=np.random.randint(0,100,(1,2)).astype(np.float32)

plt.scatter(test[:,0],test[:,1],80,'r','*')

# 调用OpenCV内的K近邻模块，并进行训练

knn=cv2.ml.KNearest_create()

knn.train(trainData,cv2.ml.ROW_SAMPLE,tdLable)

# 使用K近邻算法分类

ret,results,neighbours,dist=knn.findNearest(test,5)

# 显示处理结果

print("当前随机数可以判定为类型：",results)

print("距离当前点最近的5个邻居是：",neighbours)

print("5个最近邻居的距离：",dist)