# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 下午11:48
# @Author  : lizheng
# @FileName: demo1.py.py
# @Software: PyCharm
import cv2

import matplotlib.pyplot as plt

o=cv2.imread("../images/boat.png")

cv2.imshow("original",o)

plt.hist(o.ravel(),256)

cv2.waitKey()

cv2.destroyAllWindows()