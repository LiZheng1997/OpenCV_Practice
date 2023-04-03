# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:17:15 2019

@author: 14290

This demo is showing an effect of a pixel in an image
"""


import cv2 as cv
import numpy as np

img = np.zeros((8, 8), dtype=np.uint8)  # Using numpy zeros to create an array
print("img=\n", img)
cv.imshow("one", img)
print("读取像素点", img[0, 3])
img[0, 3] = 255     # change a pixel value in a images
print("img=\n", img)
print("修改之后的像素点", img[0, 3])
cv.imshow("two", img)
cv.waitKey()
cv.destroyAllWindows()