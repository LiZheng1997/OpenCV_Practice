# -*- coding: utf-8 -*-
# @Time    : 2023/3/28 上午12:10
# @Author  : lizheng
# @FileName: demo3.py.py
# @Software: PyCharm

import cv2

import matplotlib.pyplot as plt

#-----------读取原始图像--------------

img=cv2.imread('image\\equ.bmp',cv2.IMREAD_GRAYSCALE)

#-----------直方图均衡化处理--------------

equ=cv2.equalizeHist(img)

#-----------显示均衡化前后的图像--------------

cv2.imshow("original",img)

cv2.imshow("result",equ)

#-----------显示均衡化前后的直方图--------------

plt.figure("原始图像直方图") #构建窗口

plt.hist(img.ravel(),256)

plt.figure("均衡化结果直方图") #构建新窗口

plt.hist(equ.ravel(),256)

#----------等待释放窗口--------------------

cv2.waitKey()

cv2.destroyAllWindows()