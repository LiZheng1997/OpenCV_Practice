# -*- coding: utf-8 -*-
# @Time    : 2023/3/23 上午3:51
# @Author  : lizheng
# @FileName: demo01-1.py
# @Software: PyCharm

"""
This demo is showing how to use waitkey when imshow an image
"""
import cv2 as cv

lena = cv.imread("../images/lena.bmp")
cv.imshow("demo", lena)
key = cv.waitKey(0)
if key == ord('a'):
    print(str(key) + "is input")
    cv.imshow("PressA", lena)
elif key == ord('b'):
    print(str(key)+"is input")
    cv.imshow("PressB", lena)
cv.destroyAllWindows()
