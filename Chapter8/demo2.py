# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 下午6:50
# @Author  : lizheng
# @FileName: demo2.py.py
# @Software: PyCharm

import cv2

import numpy as np

img1=cv2.imread("../images/closing.png")

img2=cv2.imread("../images/closing2.png")

k=np.ones((10,10),np.uint8)

r1=cv2.morphologyEx(img1,cv2.MORPH_CLOSE,k,iterations=3)

r2=cv2.morphologyEx(img2,cv2.MORPH_CLOSE,k,iterations=3)

cv2.imshow("img1",img1)

cv2.imshow("result1",r1)

cv2.imshow("img2",img2)

cv2.imshow("result2",r2)

cv2.waitKey()

cv2.destroyAllWindows()