# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 下午11:54
# @Author  : lizheng
# @FileName: demo2.py.py
# @Software: PyCharm
import cv2

import numpy as np

img=cv2.imread("../images/boat.png")

hist=cv2.calcHist([img],[0],None,[256],[0,255])

print(type(hist))

print(hist.shape)

print(hist.size)

print(hist)