'''
Description: 人脸图片识别
Author: jiayuchen
Date: 2022-03-03 10:44:29
LastEditTime: 2022-03-04 09:48:43
IDE: VS code
'''

import cv2

filepath = r'../faceai/img/xingye-1.png'
img = cv2.imread(filepath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 人脸识别分类器
classifier = cv2.CascadeClassifier(
    "D:/Git_inventory/opencv/data/haarcascades/haarcascade_frontalface_default.xml"
)
color = (0, 0, 255)  # 定义绘制颜色
#调用人脸识别
faceRects = classifier.detectMultiScale(
    gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
if len(faceRects): # 检测到人脸
    print(faceRects)
    for face in faceRects: 
        print(face)
        print(face[0])
        print(type(face[0]))
        x, y, w, h = face # 框出人脸
        cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)

cv2.imshow("Image", img)  # 显示图像
cv2.waitKey(0)
cv2.destroyAllWindows()  # 释放所有的窗体资源


