# -*- coding: utf-8 -*-
# @Time    : 2023/3/28 下午9:50
# @Author  : lizheng
# @FileName: demo1.py.py
# @Software: PyCharm

import cv2
import numpy as np

import matplotlib.pyplot as plt
img = cv2.imread("../images/computer.png")
gray = cv2.cvtColor(img, cv2.COLOR_BayerRG2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
orgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
oshow = orgb.copy()
lines = cv2.HoughLines(edges, 1, np.pi/180, 140)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)

x0 = a * rho
y0 = b * rho
x1 = int(x0 + 1000 * (-b))
y1 = int(y0 + 1000 * (a))
x2 = int(x0 - 1000 * (-b))
y2 = int(y0 - 1000 * (a))
cv2.line(orgb, (x1, y1), (x2, y2), (0, 0, 255), 2)

plt.subplot(121)
plt.show(oshow)
plt.axis("off")
plt.subplot(122)
plt.show(orgb)
plt.axis("off")
