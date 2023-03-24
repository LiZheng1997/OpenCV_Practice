# Numpy提供的实现傅里叶变换的函数是numpy.fft.fft2()，它的语法格式是：
# 返回值=numpy.fft.fft2(原始图像)

import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('lena.bmp',0)
f=np.fft.fft2(img)
fshift=np.fft.fftshift(f)
magnitude_spectrum=20*np.log(np.abs(fshift)
plt.subplot(121)
plt.imshow(img,cmap='gray')
plt.title('original')
plt.axis('off')
plt.subplot(122)
plt.imshow(magnitude_spectrum,cmap='gray')
plt.title('result')
plt.axis('off')
plt.show()