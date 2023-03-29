# -*- coding: utf-8 -*-
# @Time    : 2023/3/28 上午12:19
# @Author  : lizheng
# @FileName: demo1.py.py
# @Software: PyCharm
import cv2

import numpy as np

import matplotlib.pyplot as plt

img=cv2.imread('image\\boat.bmp',0)

f=np.fft.fft2(img)

fshift=np.fft.fftshift(f)

ishift=np.fft.ifftshift(fshift)

iimg=np.fft.ifft2(ishift)

#print(iimg)

iimg=np.abs(iimg)

#print(iimg)

plt.subplot(121),plt.imshow(img,cmap='gray')

plt.title('original'),plt.axis('off')

plt.subplot(122),plt.imshow(iimg,cmap='gray')

plt.title('iimg'),plt.axis('off')

plt.show()