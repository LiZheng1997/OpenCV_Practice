# -*- coding: utf-8 -*-
# @Time    : 2023/3/27 上午3:31
# @Author  : lizheng
# @FileName: demo5.py.py
# @Software: PyCharm

##阈值处理
import cv2

import numpy as np

img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)

t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

print("img=\n",img)

print("t=",t)

print("rst=\n",rst)


img=cv2.imread("lena.bmp")

t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow("img",img)

cv2.imshow("rst",rst)

cv2.waitKey()

cv2.destroyAllWindows()

##
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)

t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

print("img=\n",img)

print("t=",t)

print("rst=\n",rst)


##
t,rst=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

cv2.imshow("img",img)

cv2.imshow("rst",rst)

cv2.waitKey()

cv2.destroyAllWindows()


##
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)

t,rst=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)

print("img=\n",img)

print("t=",t)

print("rst=\n",rst)


##
img=cv2.imread("lena.bmp")

t,rst=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)

cv2.imshow("img",img)

cv2.imshow("rst",rst)

cv2.waitKey()

cv2.destroyAllWindows()


##
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)

t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

print("img=\n",img)

print("t=",t)

print("rst=\n",rst)


##
img=cv2.imread("lena.bmp")

t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow("img",img)

cv2.imshow("rst",rst)

cv2.waitKey()

cv2.destroyAllWindows()


##
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)

t,rst=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

print("img=\n",img)

print("t=",t)

print("rst=\n",rst)
