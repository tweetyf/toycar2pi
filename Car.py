#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time,random

FWD= 14
BAK= 15
LEFT = 17
RIGHT = 18
KEEP = 10000
STOP = 10001
MIDDLE = 10002

STEPSIZE = 0.001

class Controller:
    def __init__(self):
        self.initializeGPIO()
    
    def initializeGPIO(self):
        print("Controller initiating...")
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(FWD,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(BAK,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(LEFT,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(RIGHT,GPIO.OUT,initial=GPIO.HIGH)
        self.STATE_X = MIDDLE
        self.STATE_Y = STOP
        
    def left(self):
        if self.STATE_X == RIGHT:
            self.middle()
        print("left")
        GPIO.output(LEFT,GPIO.LOW)
        self.STATE_X = LEFT

    def right(self):
        if self.STATE_X == LEFT:
            self.middle()
        print("right")
        GPIO.output(RIGHT,GPIO.LOW)
        self.STATE_X = RIGHT

    def fwd(self):
        if self.STATE_Y == BAK:
            self.stop()
        print("forward")
        GPIO.output(FWD,GPIO.LOW)
        self.STATE_Y = FWD

    def bak(self):
        if self.STATE_Y == FWD:
            self.stop()
        print("back")
        GPIO.output(BAK,GPIO.LOW)
        self.STATE_Y = BAK

    def stop(self):
        print("stop")
        GPIO.output(FWD,GPIO.HIGH)
        GPIO.output(BAK,GPIO.HIGH)
        self.STATE_Y = STOP

    def middle(self):
        print("middle")
        GPIO.output(LEFT,GPIO.HIGH)
        GPIO.output(RIGHT,GPIO.HIGH)
        self.STATE_X = MIDDLE

    def keep(self,steps=0):
        print("keep",steps)
        time.sleep(STEPSIZE*steps)
    
    def handleMove(self, movement):
        if movement==FWD:
            self.fwd()
        elif movement == BAK:
            self.bak()
        elif movement == LEFT:
            self.left()
        elif movement == RIGHT:
            self.right()
        elif movement == STOP:
            self.stop()
        elif movement == MIDDLE:
            self.middle()
        elif movement == KEEP:
            self.keep(100)

class EventEmitter:
    def __init__(self):
        pass

class Car:
    def __init__(self):
        self.ctrl = Controller()
        self.operations=[FWD,BAK,LEFT,RIGHT,KEEP,STOP,MIDDLE]

    def get_Controller():
        return self.ctrl

    def operation_emit_random(self):
        event = random.randint(0,len(self.events)-1)
        return self.events[event]

    def start(self):
        try:
            while True:
                op = self.operation_emmit_random()
                self.ctrl.handleMove(op)
                self.ctrl.handleMove(KEEP)
        except  Exception as ex:
            print ex
        finally:
            self.ctrl.handleMove(STOP)
            self.ctrl.handleMove(MIDDLE)
            GPIO.cleanup()
