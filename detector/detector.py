# YOLO cup detection
# 12/26/2021

import cv2
import numpy as np

classi = []
#with open('coco.names', 'rt') as f:
with open('detector/coco.names', 'rt') as f:
    classi = f.read().rstrip('\n').split('\n')
net = cv2.dnn.readNetFromDarknet('detector/yolov3-320.cfg', 'detector/yolov3-320.weights')
#net = cv2.dnn.readNetFromDarknet('yolov3-320.cfg', 'yolov3-320.weights')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


def crackle(outs, img):
    boxi = []
    idi = []
    confi = []
    midi = []
    for a in outs:
        for b in a:
            scores = b[5:]
            classid = np.argmax(scores)
            con = scores[classid]
            if con > 0.4:
                wi = int(b[2] * 640)
                he = int(b[3] * 640)
                x = int(b[0] * 640 - wi / 2)
                y = int(b[1] * 480 - he / 2)
                boxi.append([x, y, wi, he])
                idi.append(classid)
                confi.append(float(con))
                midi.append([int(b[0]*640), int(b[1]*640)])
    keep = cv2.dnn.NMSBoxes(boxi, confi, 0.4, 0.3)
    trueOut = []
    for k in keep:
        b = boxi[k[0]]
        x = b[0]
        y = b[1]
        w = b[2]
        h = b[3]
        trueOut.append([classi[idi[k[0]]], [x, y], [x+w, y+h], midi[k[0]]])
    return trueOut


def snap():
    cam = cv2.VideoCapture("/dev/video0")
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
    success, img = cam.read()
    nImg = cv2.dnn.blobFromImage(img, 1 / 255, (320, 320), [0, 0, 0], 1, crop=False)
    net.setInput(nImg)
    outLayeri = []
    for n in net.getUnconnectedOutLayers():
        outLayeri.append(net.getLayerNames()[n[0] - 1])
    outputs = net.forward(outLayeri)
    #cv2.imshow("Image", img)
    cv2.waitKey(0)
    return [outputs, nImg]


def pops():
    notFound = True
    snapped = snap()
    crackled = crackle(snapped[0], snapped[1])
    if len(crackled) > 0:
        for t in crackled:
            if t[0] == "cup":
                hold = False
                return crackled[crackled.index(t)]
    if notFound:
        return ["no cup"]

def lasting():
    snapped = snap()
    crackled = crackle(snapped[0], snapped[1])
    if len(crackled) > 0:
        for t in crackled:
            if t[0] == "cup":
                print(crackled[crackled.index(t)])
                return crackled[crackled.index(t)]
    else:
        print("no cup :(")
        return ["no cup :("]
     
