import RPi.GPIO as GPIO
from datetime import datetime as dt
import sys, tty, termios, time, threading


class myTh(threading.Thread):
    def __init__(self, threadID, name, where):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.where = where

    def run(self):
        runWehicle(self.name, self.where)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

initial = True
state = False
starttime = dt.now()
pressed = False


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def runWehicle(threadName, where):
    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def LightLED(LedId, state):
        GPIO.output(LedId, state)

    run = True
    ct = dt.now()
    while run:
        char = getch()
        LightLED(33, 0)
        LightLED(35, 0)
        if (char != "w" or ((dt.now() - ct).total_seconds() > 0.1)):
            run = False
            break
        time.sleep(0.01)
        LightLED(33, 1)
        LightLED(35, 1)
        time.sleep(0.01)


def TurnOff():
    GPIO.output(31, False)
    GPIO.output(33, False)
    GPIO.output(35, False)
    GPIO.output(37, False)


TurnOff()

print("Spreman!")

while True:
    char = getch()
    if (char == "w"):
        # print("naprijed")
        thf = myTh(1, "Thread-1", "f")
        thf.start()

    if (char == "s"):
        # print("nazad")
        thb = myTh(2, "Thread-2", "b")
        thb.start()

    if (char == "a"):
        # print("desno")
        thr = myTh(3, "Thread-3", "r")
        thr.start()

    if (char == "d"):
        # print("lijevo")
        thl = myTh(4, "Thread-4", "l")
        thl.start()

    if (char == "x"):
        print("Kraj")
        break

try:
    # RunForward(0.0001)
    # RunBackward(0.0001)
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
