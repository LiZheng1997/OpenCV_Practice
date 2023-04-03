# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 下午11:10
# @Author  : lizheng
# @FileName: demo.py.py
# @Software: PyCharm
import cv2

o=cv2.imread('../images/sobel.png',cv2.IMREAD_GRAYSCALE)

Laplacian=cv2.Laplacian(o,cv2.CV_64F)

Laplacian=cv2.convertScaleAbs(Laplacian)

cv2.imshow("original",o)

cv2.imshow("Laplacian",Laplacian)

cv2.waitKey()

cv2.destroyAllWindows()