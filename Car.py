#!/usr/bin/python
import RPi.GPIO as GPIO
import Driver,Sensor

##These are GPIO serior ports.
FWD= 14
BAK= 15
LEFT = 17
RIGHT = 18
#These are defined states.
KEEP = 10000
STOP = 10001
MIDDLE = 10002

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

    def keep(self):
        #do nothing here.
        print("keep")
    
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
            self.keep()

class Car:
    def __init__(self):
        self.ctrl = Controller()
        self.driver = Driver.DeadDirver()
        self.sensors = []
        self.add_Sensor(Sensor.SonarSensor())

    def get_Controller(self):
        return self.ctrl
    
    def set_Driver(self, newDriver):
        self.driver = newDriver

    def add_Sensor(self, newSensor):
        self.sensors.append(newSensor)

    def step(self):
        op = self.driver.getNextOP()
        self.ctrl.handleMove(op)
        for sensor in self.sensors:
            sensor.step()
            sdata = sensor.readData()
            self.driver.haveDataFromSensor(sdata)
    
    def destory(self):
        self.ctrl.handleMove(STOP)
        self.ctrl.handleMove(MIDDLE)
        GPIO.cleanup()
