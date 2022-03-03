'''
Description: 人脸图片识别
Author: jiayuchen
Date: 2022-03-03 10:44:29
LastEditTime: 2022-03-03 11:18:11
IDE: VS code
'''

import cv2

filepath = r'faceai/img/xingye-1.png'
img = cv2.imread(filepath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 图片转换为灰色
cv2.imshow("Image", gray)
a = cv2.waitKey(0)
# cv2.destroyAllWindows()

