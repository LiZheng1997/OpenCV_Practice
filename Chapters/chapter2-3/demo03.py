# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 19:03:48 2019

@author: 14290
"""

#位平面分解代码

#每个8位灰度图像都有8个位平面，以二进制位计算单位，其中高位的
#的平面图像占比更大,生成8个位平面图

import cv2 as cv
import numpy as np

lena=cv.imread("../images/lena.bmp",0)
cv.imshow("lena",lena)
r,c = lena.shape
x = np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    x[:,:,i]=2**i ##通过创建8位二进制的矩阵提取每个位平面
r=np.zeros((r,c,8),dtype=np.uint8)
for i in range(8):
    r[:,:,i]=cv.bitwise_and(lena,x[:,:,i])
    mask=r[:,:,i]>0
    r[mask]=255
    cv.imshow(str(i),r[:,:,i])

cv.waitKey()
cv.destroyAllWindows()