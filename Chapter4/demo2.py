# -*- coding: utf-8 -*-
# @Time    : 2023/3/26 下午11:07
# @Author  : lizheng
# @FileName: demo2.py.py
# @Software: PyCharm
import cv2

import numpy as np

img=np.random.randint(0,256,size=[5,5],dtype=np.uint8)

min=100

max=200

mask=cv2.inRange(img,min,max)

print("img=\n",img)

print("mask=\n",mask)