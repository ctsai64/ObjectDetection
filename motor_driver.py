# 5v power pin and 9v external power, 4 output pins, 4 gnd pins
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

oneA = 17
oneB = 27
oneE = 22
twoA = 23
twoB = 24
twoE = 25


GPIO.setup(oneA,GPIO.OUT)
GPIO.setup(oneB,GPIO.OUT)
GPIO.setup(oneE,GPIO.OUT)
GPIO.setup(twoA,GPIO.OUT)
GPIO.setup(twoB,GPIO.OUT)
GPIO.setup(twoE,GPIO.OUT)

while True:
    go = input("l,s,r,b?")
    if go == "l":
        print("one on")
        GPIO.output(oneA,GPIO.HIGH)
        GPIO.output(oneB,GPIO.LOW)
        GPIO.output(oneE,GPIO.HIGH)
        #GPIO.output(twoA,GPIO.LOW)
        #GPIO.output(twoB,GPIO.HIGH)
        #GPIO.output(twoE,GPIO.HIGH)
        sleep(1.5)
        GPIO.output(oneE,GPIO.LOW)
        #GPIO.output(twoE,GPIO.LOW)
    elif go == "r":
        print("two on")
        #GPIO.output(oneA,GPIO.LOW)
        #GPIO.output(oneB,GPIO.HIGH)
        #GPIO.output(oneE,GPIO.HIGH)
        GPIO.output(twoA,GPIO.HIGH)
        GPIO.output(twoB,GPIO.LOW)
        GPIO.output(twoE,GPIO.HIGH)
        sleep(1.5)
        GPIO.output(twoE,GPIO.LOW)
        #GPIO.output(oneE,GPIO.LOW)
    elif go == "s":
        print("both on")
        GPIO.output(oneA,GPIO.HIGH)
        GPIO.output(oneB,GPIO.LOW)
        GPIO.output(oneE,GPIO.HIGH)
        
        GPIO.output(twoA,GPIO.HIGH)
        GPIO.output(twoB,GPIO.LOW)
        GPIO.output(twoE,GPIO.HIGH)
        
        sleep(.5)
        GPIO.output(oneE,GPIO.LOW)
        GPIO.output(twoE,GPIO.LOW)
    elif go == "b":
        print("both on")
        GPIO.output(oneA,GPIO.LOW)
        GPIO.output(oneB,GPIO.HIGH)
        GPIO.output(oneE,GPIO.HIGH)
        
        GPIO.output(twoA,GPIO.LOW)
        GPIO.output(twoB,GPIO.HIGH)
        GPIO.output(twoE,GPIO.HIGH)
        
        sleep(1)
        GPIO.output(oneE,GPIO.LOW)
        GPIO.output(twoE,GPIO.LOW)


GPIO.cleanup()
