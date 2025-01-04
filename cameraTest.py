# last updated 1/1/2022

import cv2
cam = cv2.VideoCapture("/dev/video0")
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
while True:
    success, img = cam.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
