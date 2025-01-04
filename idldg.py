# All together now                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
# By: Cymberly Tsai 12/28/2021

import sys
sys.path.append("..")
from detector import detector
import locater
import distancer
#import motor_driver
#import servo_motor
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button = 26
led = 16
L1 = 17  
L2 = 27
LE = 22
R1 = 23
R2 = 24
RE = 25
motors = [R1, R2, RE, L1, L2, LE]
for o in motors:
    GPIO.setup(o, GPIO.OUT)
cycle = [1, 0]
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_OFF)

pin = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)

def servoTest():
    i = 0
    while i < 1: 
        p.ChangeDutyCycle(cycle[0])
        time.sleep(.5)
        p.ChangeDutyCycle(0)
        i += 1

def motorTest(go):
    if go == "r":
        print("one on")
        GPIO.output(R1,GPIO.HIGH)
        GPIO.output(R2,GPIO.LOW)
        GPIO.output(RE,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(RE,GPIO.LOW)
    elif go == "l":
        print("two on")
        GPIO.output(L1,GPIO.HIGH)
        GPIO.output(L2,GPIO.LOW)
        GPIO.output(LE,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LE,GPIO.LOW)
    elif go == "s":
        print("both on")
        GPIO.output(R1,GPIO.HIGH)
        GPIO.output(R2,GPIO.LOW)
        GPIO.output(RE,GPIO.HIGH)
        GPIO.output(L1,GPIO.HIGH)
        GPIO.output(L2,GPIO.LOW)
        GPIO.output(LE,GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(RE,GPIO.LOW)
        GPIO.output(LE,GPIO.LOW)
    elif go == "b":
        print("both on")
        GPIO.output(R1,GPIO.LOW)
        GPIO.output(R2,GPIO.HIGH)
        GPIO.output(RE,GPIO.HIGH)
        GPIO.output(L1,GPIO.LOW)
        GPIO.output(L2,GPIO.HIGH)
        GPIO.output(LE,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(RE,GPIO.LOW)
        GPIO.output(LE,GPIO.LOW)

def detectorTest():
    detect = detector.pops()
    if detect[0] == "cup":
        return detect
    else:
        return "nope"

def locaterTest(detect):
    locate = locater.find(detect[3][0])
    if locate[0] == "l":
        motor(L1, L2, R1, R2, locate[1]/100)
    elif locate[0] == "r":
        motor(R1, R2, L1, L2, locate[1]/100)
    elif locate[0] == "s":
        return "straight"         

def distanceTest(detect):
    distance = distancer.measure(detect[1][0], detect[1][1], detect[2][0], detect[2][1])
    return distance

def detectorTest():
    detect = detector.pops()
    while detect[0] != "cup":
        if cycle[0] != 13 and cycle[0] != 1:
            if cycle[1] == 0:
                cycle[0] = cycle[0] - 1
                print("left?")
            elif cycle[1] == 1:
                cycle[0] = cycle[0]  + 1
                print("right?")
        elif cycle[0] == 13:
            cycle[1] = 0
            cycle[0] = cycle[0] - 1
            print("left?")
        elif cycle[0] == 1:
            cycle[1] = 1
            cycle[0] = cycle[0] + 1
            print("right?")
        servoTest()
        detect = detector.pops()
    print("found")
    if cycle != 7:
        for n in range(abs(6 - cycle[0])):
            if cycle[0] > 7:
                motorTest('r')
            elif cycle[0] < 7:
                motorTest('l')
    cycle[0] = 7
    servoTest()
    return detect

def letsGo():
    servoTest()
    detect = detectorTest()
    locate = locater.find(detect[3][0])
    while locate[0] != "s":
        motorTest(locate[0])
        detect = detectorTest()
        locate = locater.find(detect[3][0])
    detect = detectorTest()
    distance = distancer.measure(detect[1][0], detect[1][1], detect[2][0], detect[2][1])
    while not (distance > 9.4 and distance < 11.6):
        if distance > 11.6:
            motorTest("s")
        elif distance < 9.4:
            motorTest("b")
        detect = detectorTest()
        distance = distancer.measure(detect[1][0], detect[1][1], detect[2][0], detect[2][1])
    print("complete")
    GPIO.output(led, GPIO.HIGH)
                                
    p.stop()
    GPIO.cleanup()

while True:
    if GPIO.input(button) == GPIO.HIGH:
        letsGo()