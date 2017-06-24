#!/usr/bin/python
import RPi.GPIO as GPIO
class BaseSensor:
    def __init__(self):
        self.name="BaseSensor"
    
    def readData(self):
        raise NotImplementedError();
    
    def step(self):
        raise NotImplementedError()
    
    def getName(self):
        raise NotImplementedError()
    
    def setName(self,newName):
        raise NotImplementedError()

class SonarSensor(BaseSensor):
    def readData(self):
        pass
        return 0
        
    def setp(self):
        pass
    
    def getSensorName(self):
        return self.name
    
    def setName(self,newName):
        self.name=newName
