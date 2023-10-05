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

#画实心圆
d = 400
img =np.ones((d,d,3), dtype="uint8")*255
for i in range(0, 100):
	centerX = np.random.randint(0, high=d)
	centerY = np.random.randint(0, high=d)
	radius = np.random.randint(5, high=d/5)

	color = np.random.randint(0, high= 256, size= (3,)).tolist()

	cv2.circle(img, (centerX, centerY), radius, color, -1)
cv2.imshow("Demo19.4",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#画椭圆
d = 400
img =np.ones((d,d,3), dtype="uint8")*255
center = (round(d/2), round(d/2))
size = (100, 200)
for i in range(0,10):
	angle = np.random.randint(0,361)
	color = np.random.randint(0, high=256, size = (3,)).tolist()
	thickness = np.random.randint(1,9)
	cv2.ellipse(img, center, size, angle, 0, 360, color, thickness)
cv2.imshow("demo19.5", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##画多边形

d=400

img=np.ones((d,d,3),dtype="uint8")*255

# 生成白色背景
pts=np.array([[200,50],[300,200],[200,350],[100,200]],np.int32)

# 生成各个顶点，注意数据类型为int32

pts=pts.reshape((-1,1,2))

# 第1个参数为-1，表明它未设置具体值，它所表示的维度值是通过其他参数值计算得到的

cv2.polylines(img,[pts],True,(0,255,0),8)

# 调用函数cv2.polylines()完成多边形绘图。注意，第3个参数控制多边形是否封闭

cv2.imshow("demo19.6",img)

cv2.waitKey(0)

cv2.destroyAllWindows()


# 写文字
import numpy as np

import cv2

d=400

img=np.ones((d,d,3),dtype="uint8")*255

# 生成白色背景

font=cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img,'OpenCV',(0,200),font,3,(0,255,0),15)

cv2.putText(img,'OpenCV',(0,200),font,3,(0,0,255),5, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, True)

cv2.imshow("demo19.7",img)

cv2.waitKey(0)

cv2.destroyAllWindows()

##鼠标交互

def Demo(evnet, x, y, flags, param):
	if evnet == cv2.EVENT_LBUTTONDOWN:
		print("单击了鼠标左键")
	elif evnet == cv2.EVENT_RBUTTONDOWN:
		print("单击了鼠标右键")
	elif flags == cv2.EVENT_FLAG_LBUTTON:
		print("按住左键拖动了鼠标")
	elif evnet == cv2.EVENT_MBUTTONDOWN:
		print("单击了中间键")

img = np.ones((300,300,3), np.uint8)* 255
cv2.namedWindow('Demo19.9')
cv2.setMouseCallback('Demo19.9', Demo)
cv2.imshow('Demo19.9', img)
cv2.waitKey()
cv2.destroyAllWindows()


##
Type = 0
Value = 0
def onType(a):
	Type = cv2.getTrackbarPos(tType, windowName)
	Value = cv2.getTrackbarPos(tValue, windowName)
	ret, dst = cv2.threshold(o, Value, 255, Type)
	cv2.imshow(windowName, dst)

def onValue(a):
	Type = cv2.getTrackbarPos(tType, windowName)
	Value = cv2.getTrackbarPos(tValue, windowName)
	ret, dst = cv2.threshold(o, Value, 255, Type)
	cv2.imshow(windowName, dst)

o = cv2.imread("../images/lena.bmp", 0)
windowName = "Demo19.13"
cv2.namedWindow(windowName)
cv2.imshow(windowName, o)

tType = "Type"
tValue = "Value"
cv2.createTrackbar(tType, windowName, 0, 4, onType)
cv2.createTrackbar(tType, windowName, 0, 255, onValue)
if cv2.waitKey(0) == 27:
	cv2.destroyAllWindows()
