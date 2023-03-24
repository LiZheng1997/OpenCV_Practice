# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:37:54 2019

@author: 14290

This demo is showing how opencv read an image file
"""

import cv2 as cv

lena = cv.imread("../images/lenacolor.png")  # read an image 读取一张图片
cv.namedWindow("lesson")    # create a window named lesson 创建一个名为lesson的窗口
cv.imshow("lesson", lena)   # showing an image with a window named lesson
key = cv.waitKey()  # wait for a key to interface with user 等待一个键盘的指令，这个用来座位用户交互的
if key != -1:
    print("触发了按键")
    cv.destroyAllWindows("lesson")
