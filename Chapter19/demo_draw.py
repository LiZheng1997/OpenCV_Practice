#OpenCV提供了函数cv2.line()用来绘制直线(线段)

#划线

# import numpy as np
# import cv2
# n=300
# img=np.zeros((n+1,n+1,3),np.uint8)
# img=cv2.line(img,(0,0),(n,n),(255,0,0),3)
# img=cv2.line(img,(0,100),(n,100),(0,255,0),1)
# img=cv2.line(img,(100,0),(100,n),(0,0,255),6)
# winname='Demo19.1'
# cv2.namedWindow(winname)
# cv2.imshow(winname,img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 画矩形

import numpy as np
import cv2
# n=300
# img=np.ones((n,n,3),np.uint8)*255
# img=cv2.rectangle(img,(50,50),(n-100,n-50),(0,0,255),-1)
# winname='Demo19.1'
# cv2.namedWindow(winname)
# cv2.imshow(winname,img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#画圆
d = 400
img =np.ones((d,d,3), dtype="uint8")*255
(centerX, centerY) = (round(img.shape[1]/2), round(img.shape[0]/2))
red = (0,0,255) #设置白色变量
for r in range(5,round(d/2),12):
	cv2.circle(img,(centerX,centerY),r, red,3)
cv2.imshow("Demo19.3",img)
cv2.waitKey(0)
cv2.destroyAllWindows()