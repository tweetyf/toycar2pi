#!/usr/bin/python
import sys
import time
import Car,Driver

STEPSIZE = 0.001

class World:
    def __init__(self):
        self.car = Car.Car()
        self.driver = Driver.DrunkDriver()
        self.car.set_Driver(self.driver)

    def start(self):
        try:
            while True:
                self.driver.step()
                self.car.step()
                time.sleep(STEPSIZE)
        except  Exception as ex:
            print ex
        finally:
            self.car.destory()


if __name__ =='__main__':
    wd = World()
    wd.start()
    
