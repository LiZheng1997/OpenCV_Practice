# dst=cv2.Scharr(src,ddepth,dx,dy[,scale[,delta[,borderType]]])
# 叠加的时候使用的是addWeight加权，gamma也就是最后一个参数通常设置为0
# 不允许将函数cv2.Scharr()的参数dx和dy的值同时设置为1。
# 因此，本例中将这两个参数的值都设置为1后，程序会报错
# 对比两个算子的方法效果。

import cv2
o=cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
Sobelx=cv2.Sobel(o,cv2.CV_64F,1,0,ksize=3)
Sobely=cv2.Sobel(o,cv2.CV_64F,0,1,ksize=3)

Sobelx=cv2.convertScaleAbs(Sobelx)
Sobely=cv2.convertScaleAbs(Sobely)
Sobelxy=cv2.addWeighted(Sobelx,0.5,Sobely,0.5,0)
Scharrx=cv2.Scharr(o,cv2.CV_64F,1,0)
Scharry=cv2.Scharr(o,cv2.CV_64F,0,1)
Scharrx=cv2.convertScaleAbs(Scharrx)
Scharry=cv2.convertScaleAbs(Scharry)
Scharrxy=cv2.addWeighted(Scharrx,0.5,Scharry,0.5,0)
cv2.imshow("original",o)
cv2.imshow("Sobelxy",Sobelxy)
cv2.imshow("Scharrxy",Scharrxy)
cv2.waitKey()
cv2.destroyAllWindows()

# Sobel算子和Scharr算子计算的都是一阶近似导数的值。通常情况下，可以将它们表示为：
# Sobel算子=|左-右| /|下-上|
# Scharr算子=|左-右| /|下-上|
# 式中“|左-右|”表示左侧像素值减右侧像素值的结果的绝对值，“|下-上|”表示下方像素值减上方像素值的结果的绝对值。
# Laplacian算子计算的是二阶近似导数值，可以将它表示为：
# Laplacian算子=|左-右|+|左-右|+|下-上|+|下-上|

## 
import cv2

o=cv2.imread('Scharr.bmp',cv2.IMREAD_GRAYSCALE)

Scharrx=cv2.Scharr(o,cv2.CV_64F,1,0)

Scharrx=cv2.convertScaleAbs(Scharrx)

cv2.imshow("original",o)

cv2.imshow("x",Scharrx)

cv2.waitKey()

cv2.destroyAllWindows()


#
import cv2

o=cv2.imread('Sobel4.bmp',cv2.IMREAD_GRAYSCALE)

Scharrx=cv2.Sobel(o,cv2.CV_64F,1,0,-1)

Scharry=cv2.Sobel(o,cv2.CV_64F,0,1,-1)

Scharrx=cv2.convertScaleAbs(Scharrx)

Scharry=cv2.convertScaleAbs(Scharry)

cv2.imshow("original",o)

cv2.imshow("x",Scharrx)

cv2.imshow("y",Scharry)

cv2.waitKey()

cv2.destroyAllWindows()