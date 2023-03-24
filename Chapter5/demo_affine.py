import cv2
import numpy as np

#进行平移的操作，
# img=cv2.imread("lena.jpg")
# height,width=img.shape[:2]
# x=100
# y=200
# M=np.float32([[1,0,x],[0,1,y]])
# move=cv2.warpAffine(img,M,(width,height))
# cv2.imshow("original",img)
# cv2.imshow("move",move)
# cv2.waitKey()
# cv2.destroyAllWindows()


#进行旋转操作
# img=cv2.imread("lena.jpg")
# height,width=img.shape[:2]
# M=cv2.getRotationMatrix2D((width/2,height/2),45,0.6)
# rotate=cv2.warpAffine(img,M,(width,height))
# cv2.imshow("original",img)
# cv2.imshow("rotation",rotate)
# cv2.waitKey()
# cv2.destroyAllWindows()

#更复杂的仿射变化
# img=cv2.imread('lena.bmp')
# rows,cols,ch=img.shape
# p1=np.float32([[0,0],[cols-1,0],[0,rows-1]])
# p2=np.float32([[0,rows*0.33],[cols*0.85,rows*0.25],[cols*0.15,rows*0.7]])
# M=cv2.getAffineTransform(p1,p2)
# print("仿射矩阵",M)
# dst=cv2.warpAffine(img,M,(cols,rows))
# cv2.imshow("origianl",img)
# cv2.imshow("result",dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

#透视
img=cv2.imread('lena.bmp')
rows,cols=img.shape[:2]
print(rows,cols)
pts1=np.float32([[150,50],[400,50],[60,450],[310,450]])
pts2=np.float32([[50,50],[rows-50,50],[50,cols-50],[rows-50,cols-50]])
M=cv2.getPerspectiveTransform(pts1,pts2)
print("透视矩阵变化：",M)
dst=cv2.warpPerspective(img,M,(cols,rows))
cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()