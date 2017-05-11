#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time
import Car

def checkController():
    print("Checking... Please you should now check your Autobot status to see if that is right.")
    car = Car.Car()
    controller = car.get_Controller()
    controller.fwd()
    controller.keep(200)
    controller.bak()
    controller.keep(300)
    controller.stop()
    controller.keep(500)
    controller.left()
    controller.keep(200)
    controller.middle()
    controller.keep(400)
    controller.left()
    controller.keep(400)
    controller.right()
    controller.keep(200)
    controller.middle()
    controller.keep(400)
    controller.right()
    controller.keep(400)
    controller.middle()
    GPIO.cleanup()
    print("All Check Done!")

def run_console():
    import curses
    try:
        keymap = {ord('w'): Car.FWD, ord('s'):Car.BAK, ord('a'):Car.LEFT, ord('d'):Car.RIGHT}
        stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        stdscr.keypad(1)
        stdscr.addstr(0,5,"Hit 'q' to quit")
        stdscr.refresh()
        mv = ''
        car = Car.Car()
        controller = car.get_Controller()
        while mv != ord('q'):
            mv = stdscr.getch()
            if (mv==ord(' ')):
                controller.handleMove(Car.STOP)
                controller.handleMove(Car.MIDDLE)
            else:
                evnt = keymap[mv]
                controller.handleMove(evnt)
            stdscr.refresh()
    except Exception as ex:
        print ex
    finally:
        GPIO.cleanup()
        curses.endwin()

def testCar():
    mc = Car.Car()
    mc.start()
    
if __name__ =='__main__':
    run_console()
