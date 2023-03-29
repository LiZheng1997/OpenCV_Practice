# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 上午1:57
# @Author  : lizheng
# @FileName: demo2.py.py
# @Software: PyCharm

import cv2

img=cv2.imread("lena.bmp")

x=cv2.flip(img,0)

y=cv2.flip(img,1)

xy=cv2.flip(img,-1)

cv2.imshow("img",img)

cv2.imshow("x",x)

cv2.imshow("y",y)

cv2.imshow("xy",xy)

cv2.waitKey()

cv2.destroyAllWindows()

##
import cv2

import numpy as np

img=cv2.imread("../images/lena.bmp")

height,width=img.shape[:2]

x=100

y=200

M=np.float32([[1,0,x],[0,1,y]])

move=cv2.warpAffine(img,M,(width,height))

cv2.imshow("original",img)

cv2.imshow("move",move)

cv2.waitKey()

cv2.destroyAllWindows()


##

img=cv2.imread("../images/lena.bmp")

height,width=img.shape[:2]

M=cv2.getRotationMatrix2D((width/2,height/2),45,0.6)

rotate=cv2.warpAffine(img,M,(width,height))

cv2.imshow("original",img)

cv2.imshow("rotation",rotate)

cv2.waitKey()

cv2.destroyAllWindows()


##
import cv2

import numpy as np

img=cv2.imread('lena.bmp')

rows,cols,ch=img.shape

p1=np.float32([[0,0],[cols-1,0],[0,rows-1]])

p2=np.float32([[0,rows*0.33],[cols*0.85,rows*0.25],[cols*0.15,rows*0.7]])

M=cv2.getAffineTransform(p1,p2)

dst=cv2.warpAffine(img,M,(cols,rows))

cv2.imshow("origianl",img)

cv2.imshow("result",dst)