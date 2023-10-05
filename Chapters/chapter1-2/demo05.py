# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:42:47 2019

@author: 14290
"""

import numpy as np
import cv2 as cv

img=np.random.randint(0,256, size=[256,256], dtype=np.uint8)
cv.imshow("demo", img)
cv.waitKey()
cv.destroyAllWindows()
