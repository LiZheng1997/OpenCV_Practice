# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 23:58:25 2019

@author: 14290
"""

#使用cvtcolor()函数进行色彩空间的转换

import cv2 as cv
import numpy as np

img=np.random.randint(0,256,size=[2,4,3], dtype=np.uint8)
rst=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print("img=\n", img)
print("rat=\n",rst)
print("像素点(1,0)直接计算得到的值=",img[1,0,0]*0.144+img[1,0,1]*0.587+img\
      [1,0,2]*0.299)
print("像素点(1,0)使用公式转换值为",rst[1,0])