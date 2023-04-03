# -*- coding: utf-8 -*-
# @Time    : 2023/3/26 下午11:18
# @Author  : lizheng
# @FileName: demo4.py.py
# @Software: PyCharm

##通过HSV空间对不同的颜色的内容进行提取
import cv2

import numpy as np

opencv=cv2.imread("../images/opencv-logo.png")

hsv=cv2.cvtColor(opencv,cv2.COLOR_BGR2HSV)

cv2.imshow('opencv',opencv)

#=============指定蓝色值的范围=============

minBlue=np.array([110,50,50])

maxBlue=np.array([130,255,255])

#确定蓝色区域

mask=cv2.inRange(hsv,minBlue,maxBlue)

#通过掩码控制的按位与运算，锁定蓝色区域

blue=cv2.bitwise_and(opencv,opencv,mask=mask)

cv2.imshow('blue',blue)

#=============指定绿色值的范围=============

minGreen=np.array([50,50,50])

maxGreen=np.array([70,255,255])

#确定绿色区域
mask=cv2.inRange(hsv,minGreen,maxGreen)

#通过掩码控制的按位与运算，锁定绿色区域

green=cv2.bitwise_and(opencv,opencv,mask=mask)

cv2.imshow('green',green)

#=============指定红色值的范围=============

minRed=np.array([0,50,50])

maxRed=np.array([30,255,255])

#确定红色区域

mask=cv2.inRange(hsv,minRed,maxRed)

#通过掩码控制的按位与运算，锁定红色区域

red=cv2.bitwise_and(opencv,opencv,mask=mask)

cv2.imshow('red',red)

cv2.waitKey()

cv2.destroyAllWindows()