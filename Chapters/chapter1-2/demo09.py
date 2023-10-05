# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:29:52 2019

@author: 14290
"""
#shape是判别图像是彩色还是二值或者灰色
#彩色的有三个通道
#size返回的是图像的像素数目，将shape中的元素相乘
#dtype不用说就是数据类型

import cv2 as cv

gray=cv.imread("../images/lenacolor.png",0)
color=cv.imread("../images/lenacolor.png")
print("图像gray的属性")
print(gray.shape)
print(gray.size)
print(gray.dtype)

print("图像color的属性")
print(color.shape)
print(color.size)
print(color.dtype)


cv.waitKey()
cv.destroyAllWindows()