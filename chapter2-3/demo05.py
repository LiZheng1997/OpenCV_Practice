# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 00:37:18 2019

@author: 14290
"""
#获取指定颜色，在HSV颜色空间内对应得值，
#将RGB得色彩空间进行映射到HSV空间中

import cv2 as cv
import numpy as np

imgBlue=np.zeros([1,1,3], dtype=np.uint8)
imgBlue[0,0,0]=255
Blue=imgBlue
BlueHSV= cv.cvtColor(Blue,cv.COLOR_BGR2HSV)
print("blue\n",Blue)
print("BlueHSV=\n", BlueHSV)

img=np.random.randint(0,256,size=[5,5], dtype=np.uint8)
min =100
max=200
mask=cv.inRange(img,min,max)
print("img=\n", img)
print("mask=\n", mask)
#cv.imshow("img",img)

