# last updated 12/28/2022

#3v3 power pin for button, output pin for button and light, gnd pin for led
import RPi.GPIO as GPIO

button = 23
led = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, GPIO.PUD_OFF)
GPIO.setup(led, GPIO.OUT)
while True:
   if GPIO.input(button) == GPIO.HIGH:
        GPIO.output(led, GPIO.HIGH)
   else:
        GPIO.output(led, GPIO.LOW)
        
GPIO.cleanup()
