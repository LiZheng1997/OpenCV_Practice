# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:09:31 2019

@author: 14290
"""
##图像翻转
import cv2 as cv
import numpy as np

img=cv.imread("../images/lena.bmp")
x =cv.flip(img,0)
y=cv.flip(img,1)
xy=cv.flip(img,-1)

cv.imshow("img",img)
cv.imshow("x",x)
cv.imshow("y",y)
cv.imshow("xy",xy)

cv.waitKey()
cv.destroyAllWindows()