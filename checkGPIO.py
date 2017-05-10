#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time
import MovementController

def main():
    mc = MovementController.Controller()
    mc.checkStatus()
    GPIO.cleanup()

main()
