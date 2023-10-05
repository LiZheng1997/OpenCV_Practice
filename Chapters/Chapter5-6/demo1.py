# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 上午1:32
# @Author  : lizheng
# @FileName: demo1.py.py
# @Software: PyCharm

import cv2

import numpy as np

img=np.ones([2,4,3],dtype=np.uint8)

size=img.shape[:2]

rst=cv2.resize(img,size)

print("img.shape=\n",img.shape)

print("img=\n",img)

print("rst.shape=\n",rst.shape)

print("rst=\n",rst)



img=cv2.imread("../images/lenacolor.png")

rows,cols=img.shape[:2]

size=(int(cols*0.9),int(rows*0.5))

rst=cv2.resize(img,size)

print("img.shape=",img.shape)

print("rst.shape=",rst.shape)

import cv2

img=cv2.imread("../images/lenacolor.png")

rst=cv2.resize(img,None,fx=2,fy=0.5)

print("img.shape=",img.shape)

print("rst.shape=",rst.shape)