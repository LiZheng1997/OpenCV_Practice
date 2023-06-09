# -*- coding: utf-8 -*-
# @Time    : 2023/3/29 下午11:31
# @Author  : lizheng
# @FileName: demo3.py.py
# @Software: PyCharm
import cv2

import numpy as np

images=[]

images.append(cv2.imread("f01.png",cv2.IMREAD_GRAYSCALE))

images.append(cv2.imread("f02.png",cv2.IMREAD_GRAYSCALE))

images.append(cv2.imread("f11.png",cv2.IMREAD_GRAYSCALE))

images.append(cv2.imread("f12.png",cv2.IMREAD_GRAYSCALE))

labels=[0,0,1,1]

#print(labels)

recognizer=cv2.face.FisherFaceRecognizer_create()

recognizer.train(images,np.array(labels))

predict_image=cv2.imread("fTest.png",cv2.IMREAD_GRAYSCALE)

label,confidence=recognizer.predict(predict_image)

print("label=",label)

print("confidence=",confidence)
