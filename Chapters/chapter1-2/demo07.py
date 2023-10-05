# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:55:36 2019

@author: 14290
"""

import numpy as np
import cv2 as cv

a=cv.imread("../images/lena.bmp", cv.IMREAD_UNCHANGED)
face=a[250:400, 250:300]
cv.imshow("original", a)
cv.imshow("face", face)
cv.waitKey()
cv.destroyAllWindows()

##脸部打码使用如下代码
#face=np.random.randint(0,256,(180,100,3))#设置像素值和通道
#a[220:400,250:350]=face
#赋值效果如同打码