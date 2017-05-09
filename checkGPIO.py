#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time
FWD= 14
BAK= 15
LEFT = 17
RIGHT = 18

STEPSIZE = 0.1

def left(steps=1):
    print("left", steps)
    GPIO.output(LEFT,GPIO.LOW)
    time.sleep(STEPSIZE*steps)
    GPIO.output(LEFT,GPIO.HIGH)

def right(steps=1):
    print("right", steps)
    GPIO.output(RIGHT,GPIO.LOW)
    time.sleep(STEPSIZE*steps)
    GPIO.output(RIGHT,GPIO.HIGH)

def fwd(steps=1):
    print("forward", steps)
    GPIO.output(FWD,GPIO.LOW)
    time.sleep(STEPSIZE*steps)
    GPIO.output(FWD,GPIO.HIGH)

def bak(steps=1):
    print("back", steps)
    GPIO.output(BAK,GPIO.LOW)
    time.sleep(STEPSIZE*steps)
    GPIO.output(BAK,GPIO.HIGH)

def initializeGPIO():
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FWD,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(BAK,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(LEFT,GPIO.OUT,initial=GPIO.HIGH)
    GPIO.setup(RIGHT,GPIO.OUT,initial=GPIO.HIGH)

def checkStatus():
    fwd(3)
    time.sleep(0.5)
    bak(2)
    time.sleep(1)
    left()
    time.sleep(0.5)
    left(2)
    time.sleep(0.5)
    right()
    time.sleep(0.5)
    right(2)
    print("Check OK. Please you should now check your Autobot status to see if that is right.")

def main():
    initializeGPIO()
    checkStatus()
    GPIO.cleanup()

main()
