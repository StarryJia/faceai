#coding=utf-8
#练习类
import datetime
import time
import cv2
import numpy as np
#开始计时
startTime = datetime.datetime.now()

time.sleep(1)

#结束计时
endTime = datetime.datetime.now()
print(endTime - startTime)
#输出：0:00:01.000791

drawing = False


def drawDef(event, x, y, flags, param):
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False

    if event == cv2.EVENT_MOUSEMOVE and drawing == True:
        cv2.circle(img, (x, y), 10, (255, 0, 0), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', drawDef)

while (1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()