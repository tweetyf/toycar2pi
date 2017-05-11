#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time
FWD= 14
BAK= 15
LEFT = 17
RIGHT = 18
KEEP = 10000
STOP = 10001
MIDDLE = 10002

STEPSIZE = 0.01

class Controller:
    def __init__(self):
        self.initializeGPIO()
    
    def initializeGPIO(self):
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
            self.keep(1)
        print("left")
        GPIO.output(LEFT,GPIO.LOW)
        self.STATE_X = LEFT

    def right(self):
        if self.STATE_X == LEFT:
            self.middle()
            self.keep(1)
        print("right")
        GPIO.output(RIGHT,GPIO.LOW)
        self.STATE_X = RIGHT

    def fwd(self):
        if self.STATE_Y == BAK:
            self.stop()
            self.keep(1)
        print("forward")
        GPIO.output(FWD,GPIO.LOW)

    def bak(self):
        if self.STATE_Y == FWD:
            self.stop()
            self.keep(1)
        print("back")
        GPIO.output(BAK,GPIO.LOW)

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

    def keep(self,step=0):
        print("keep",steps)
        time.sleep(STEPSIZE*steps)

    def checkStatus(self):
        print("Checking... Please you should now check your Autobot status to see if that is right.")
        fwd()
        bak()
        stop()
        left()
        left()
        right()
        right()
        middle()
        print("All Check Done!")

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
            self.keep(1)
    
    def runconsole(self):
        keymap = {'w': FWD, 's':BAK, 'a':LEFT, 'd':right}
        while True:
            mv = raw_input('')
            self.handleMove(keymap[mv])

def main():
    cc = Controller()
    cc.runconsole()
    GPIO.cleanup()
    
if __name__ =='__main__':
    main()
