import sys
sys.path.append("..")
from detector import detector
import locater
import distancer
import RPi.GPIO as GPIO
import time

button = 26
led = 16
R1 = 17  
R2 = 27
RE = 22
L1 = 23
L2 = 24
LE = 25
servoPin = 5
GPIO.setmode(GPIO.BCM)
outs = [led, R1, R2, RE, L1, L2, LE, servoPin]
for o in outs:
    GPIO.setup(o, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_OFF)
servo = GPIO.PWM(servoPin, 50)
servo.start(0)

def motor(A1, A2, B1, B2, long):
    GPIO.output(A1,GPIO.HIGH)
    GPIO.output(A2,GPIO.LOW)
    GPIO.output(LE,GPIO.HIGH)
    GPIO.output(B1,GPIO.LOW)
    GPIO.output(B2,GPIO.HIGH)
    GPIO.output(RE,GPIO.HIGH)
    time.sleep(long)
    GPIO.output(LE, GPIO.LOW)
    GPIO.output(RE,GPIO.LOW)

def letsGo():
    detect = detector.pops()
    if detect[0] == "cup":
        print("found")
        locate = locater.find(detect[3][0])
        if locate[0] = "l":
            motor(L1, L2, R1, R2, locate[1]/100)
        elif locate[0] = "r":
            motor(R1, R2, L1, L2, locate[1]/100)
        elif locate[0] = "s":
            distance = distancer.measure(detect[1][0], detect[1][1], detect[2][0], detect[2][1])
            if distance > 9.4 and distance < 11.6:
               GPIO.output(led, GPIO.HIGH) 
    else:
        print("no")
        servo.ChangeDutyCycle(10)
        time.sleep(0.23)
        servo.ChangeDutyCycle(0)

while True:
    if GPIO.input(button) == GPIO.HIGH:
        letsGo()

GPIO.cleanup()