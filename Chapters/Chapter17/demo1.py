# -*- coding: utf-8 -*-
# @Time    : 2023/3/28 下午10:25
# @Author  : lizheng
# @FileName: demo1.py.py
# @Software: PyCharm

import cv2

import numpy as np

import matplotlib.pyplot as plt

o=cv2.imread("../images/seg.png",cv2.IMREAD_UNCHANGED)

k=np.ones((5,5),np.uint8)

e=cv2.erode(o,k)

b=cv2.subtract(o,e)

plt.subplot(131)

plt.imshow(o)

plt.axis('off')

plt.subplot(132)

plt.imshow(e)

plt.axis('off')

plt.subplot(133)

plt.imshow(b)

plt.axis('off')