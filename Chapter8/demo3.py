# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 下午6:54
# @Author  : lizheng
# @FileName: demo3.py.py
# @Software: PyCharm

import cv2

import numpy as np

o=cv2.imread("../images/erode.png",cv2.IMREAD_UNCHANGED)

k=np.ones((5,5),np.uint8)

r=cv2.morphologyEx(o,cv2.MORPH_GRADIENT,k)

cv2.imshow("original",o)

cv2.imshow("result",r)

cv2.waitKey()

cv2.destroyAllWindows()