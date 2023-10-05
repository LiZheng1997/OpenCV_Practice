# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:38:26 2019

@author: 14290
"""
import numpy as np
import cv2 as cv

img=np.random.randint(10, 99, size=[5, 5], dtype=np.uint8)
print("img\n", img)
print("读取像素点img.item(3,2)=", img.item(3, 2))
img.itemset((3, 2), 255)
print("修改后img=\n", img)
print(img.item(3, 2))