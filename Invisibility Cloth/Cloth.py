import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
time.sleep(2)
background = 0
for i in range(30):
    ret,background = cap.read() # used to capture the image
while(cap.isOpened()): #To check if the cam is on
    ret,img = cap.read()
    if not ret: #if cam is not on
        break
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#Because the R, G, and B components of an object’s color in a digital image are all correlated with the amount of light hitting the object, and therefore with each other, image descriptions in terms of those components make object discrimination difficult. Descriptions in terms of hue/lightness/chroma or hue/lightness/saturation are often more relevant.
    #Detecting color red
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
    mask1=mask1+mask2
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations = 2)
    mas2 = cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8),iterations=1)
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(background,background,mask = mask1)
    res2 = cv2.bitwise_and(img,img,mask=mask2)
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow('Invisiblity Cloak',final_output)
    k=cv2.waitKey(10)
    if k==27:
        break
cap.release()
cv2.destroyAllWindow()
    