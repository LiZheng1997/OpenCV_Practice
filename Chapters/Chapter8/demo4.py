# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 下午6:57
# @Author  : lizheng
# @FileName: demo4.py.py
# @Software: PyCharm

import cv2

import numpy as np

o1=cv2.imread("../images/erode.png",cv2.IMREAD_UNCHANGED)

o2=cv2.imread("../images/lena.bmp",cv2.IMREAD_UNCHANGED)

k=np.ones((5,5),np.uint8)

r1=cv2.morphologyEx(o1,cv2.MORPH_TOPHAT,k)

r2=cv2.morphologyEx(o2,cv2.MORPH_TOPHAT,k)

cv2.imshow("original1",o1)

cv2.imshow("original2",o2)

cv2.imshow("result1",r1)

cv2.imshow("result2",r2)

cv2.waitKey()

cv2.destroyAllWindows()