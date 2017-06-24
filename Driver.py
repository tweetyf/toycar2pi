#!/usr/bin/python
import random
import Car

class BaseDriver:
    def __init__(self):
        self.operations=[
        Car.FWD,
        Car.BAK,
        Car.LEFT,
        Car.RIGHT,
        Car.KEEP,
        Car.STOP,
        Car.MIDDLE]
    
    def step(self):
        raise NotImplementedError()
        
    def getNextOP(self):
        raise NotImplementedError()
    
    def haveDataFromSensor(self,newData):
        raise NotImplementedError()

class DrunkDriver(BaseDriver):
    def setp(self):
        # what could a drunk driver possibly do?
        pass
        
    def getNextOP(self):
        event = random.randint(0,len(self.operations)-1)
        return self.operations[event]
    
    def haveDataFromSensor(self,newData):
        pass

class DeadDirver(BaseDriver):
    def setp(self):
        # what could a dead driver possibly do?
        pass
    
    def getNextOP(self):
        return Car.KEEP
    
    def haveDataFromSensor(self,newData):
        pass
