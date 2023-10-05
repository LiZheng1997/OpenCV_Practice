# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:34:47 2019

@author: 14290
"""

import numpy as np
import cv2 as cv

#蓝色通道
blue = np.zeros((300, 300, 3), dtype=np.uint8)
blue[:, :, 0] = 255
print("blue=\n", blue)
cv.imshow("blue", blue)

#绿色通道
green = np.zeros((300, 300, 3), dtype=np.uint8)
green[:, :, 1] = 255
print("green=\n", green)
cv.imshow("green", green)

#蓝色通道
red = np.zeros((300, 300, 3), dtype=np.uint8)
red[:, :, 2] = 255
print("red=\n", red)
cv.imshow("red", red)

cv.waitKey()
cv.destroyAllWindows()