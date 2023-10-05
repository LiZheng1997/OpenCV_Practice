# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 18:08:14 2019

@author: 14290
"""

import cv2 
import numpy as np

print(cv2.__version__)
a = cv2.imread("../images/lena.bmp",1)
w ,h ,c = a.shape
mask = np.zeros((w,h), dtype=np.uint8)#8位单通道图像作为掩码
mask[100:400,200:400]=255
mask[100:500,100:200]=255
c = cv2.bitwise_and(a,a,mask)
print("a.shape=",a.shape)
print("mask.shape=",mask.shape)
cv2.imshow("a",a)
cv2.imshow("mask",mask)
cv2.imshow("c",c)
cv2.waitKey()
cv2.destroyAllWindows()

#有问题 不知道为啥与运算之后 图像没有在掩码区域进行切割。

#cv2.add函数可以进行亮度调节，将像素点进行累加