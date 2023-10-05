# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 下午6:47
# @Author  : lizheng
# @FileName: demo1.py.py
# @Software: PyCharm

##形态学操作
import cv2

import numpy as np

img1=cv2.imread("../images/erode.png")

img2=cv2.imread("../images/opening.png")
k=np.ones((10,10),np.uint8)

r1=cv2.morphologyEx(img1,cv2.MORPH_OPEN,k)

r2=cv2.morphologyEx(img2,cv2.MORPH_OPEN,k)

cv2.imshow("img1",img1)

cv2.imshow("result1",r1)

cv2.imshow("img2",img2)

cv2.imshow("result2",r2)

cv2.waitKey()

cv2.destroyAllWindows()