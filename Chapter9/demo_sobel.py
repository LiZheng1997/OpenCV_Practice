#Sobel 算子的函数使用。
# dst=cv2.Sobel(src,ddepth,dx,dy[,ksize[,scale[,delta[,borderType]]]])式中
# 函数cv2.Sobel(）内参数ddepth的值设置为“cv2.CV_64F”
# 使用函数cv2.convertScaleAbs(）对参数取绝对值
# dst=cv2.convertScaleAbs(src[,alpha[,beta]]）

#参数区绝对值的函数，
# import cv2
# import numpy as np
# img=np.random.randint(-256,256,size=[4,5],dtype=np.int16)
# rst=cv2.convertScaleAbs(img)
# print("img=\n",img)
# print("rst=\n",rst)
# cv2.imshow('rst',rst)

# cv2.waitKey()
# cv2.destroyAllWindows()

# 在两个方向边缘进行计算，然后使用addWeighted()进行叠加，
import cv2
o=cv2.imread('lena.bmp',cv2.IMREAD_GRAYSCALE)
Sobelx=cv2.Sobel(o,cv2.CV_64F,1,0)
Sobely=cv2.Sobel(o,cv2.CV_64F,0,1)
Sobelx=cv2.convertScaleAbs(Sobelx)
Sobely=cv2.convertScaleAbs(Sobely)
Sobelxy=cv2.addWeighted(Sobelx,0.5,Sobely,0.5,0)
Sobelxy11=cv2.Sobel(o,cv2.CV_64F,1,1)
Sobelxy11=cv2.convertScaleAbs(Sobelxy11)
cv2.imshow("original",o)
cv2.imshow("xy",Sobelxy)
cv2.imshow("xy11",Sobelxy11)
cv2.waitKey()
cv2.destroyAllWindows()

