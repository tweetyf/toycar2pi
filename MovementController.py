#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time
FWD= 14
BAK= 15
LEFT = 17
RIGHT = 18

STEPSIZE = 0.1

class Controller:
    def __init__():
        initializeGPIO()
        
    def initializeGPIO():
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(FWD,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(BAK,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(LEFT,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(RIGHT,GPIO.OUT,initial=GPIO.HIGH)
        
    def left():
        print("left")
        GPIO.output(LEFT,GPIO.LOW)

    def right():
        print("right")
        GPIO.output(RIGHT,GPIO.LOW)

    def fwd():
        print("forward")
        GPIO.output(FWD,GPIO.LOW)

    def bak():
        print("back")
        GPIO.output(BAK,GPIO.LOW)

    def stop():
        print("stop")
        GPIO.output(FWD,GPIO.HIGH)
        GPIO.output(BAK,GPIO.HIGH)

    def middle():
        print("stop")
        GPIO.output(LEFT,GPIO.HIGH)
        GPIO.output(RIGHT,GPIO.HIGH)

    def keep(step):
        print("keep",steps)
        time.sleep(STEPSIZE*steps)

    def checkStatus():
        print("Checking... Please you should now check your Autobot status to see if that is right.")
        fwd()
        keep(3)
        stop()
        keep(1)
        bak()
        keep(2)
        stop()
        keep(1)
        left()
        keep(1)
        middle()
        keep(2)
        left()
        keep(2)
        middle()
        keep(2)
        right()
        keep(1)
        middle()
        keep(1)
        right()
        keep(2)
        middle()
        keep(2)
        print("All Check Done!")

def main():
    initializeGPIO()
    checkStatus()
    GPIO.cleanup()

main()
