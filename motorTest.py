import RPi.GPIO as GPIO
from datetime import datetime as dt
import sys, tty, termios, time

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


def LightLED(LedId, state):
    GPIO.output(LedId, state)


def TurnOff():
    GPIO.output(31, False)
    GPIO.output(33, False)
    GPIO.output(35, False)
    GPIO.output(37, False)


def RunForward(speed):
    run = True
    ct = dt.now()
    while run:
        LightLED(31, 0)
        LightLED(37, 0)
        char = getch()
        if(char != "w"):
            run = False
            break
        time.sleep(speed)
        LightLED(31, 1)
        LightLED(37, 1)
        time.sleep(speed)


def RunRight(speed):
    run = True
    ct = dt.now()
    while run:
        LightLED(31, 0)
        char = getch()
        if(char != "d"):
            run = False
            break
        time.sleep(speed)
        LightLED(31, 1)
        time.sleep(speed)


def RunLeft(speed):
    run = True
    ct = dt.now()
    while run:
        LightLED(37, 0)
        char = getch()
        if(char != "a"):
            run = False
            break
        time.sleep(speed)
        LightLED(37, 1)
        time.sleep(speed)


def RunBackward(speed):
    run = True
    ct = dt.now()
    while run:
        LightLED(33, 0)
        LightLED(35, 0)
        char = getch()
        if(char != "s"):
            run = False
            break
        time.sleep(speed)
        LightLED(33, 1)
        LightLED(35, 1)
        time.sleep(speed)


TurnOff()

print("Spreman!")

while True:
    char = getch()
    if(char == "w"):
        #print("naprijed")
        RunForward(0.01)

    if(char == "s"):
        #print("nazad")
        RunBackward(0.01)

    if(char == "d"):
        #print("desno")
        RunRight(0.01)

    if(char == "a"):
        #print("lijevo")
        RunLeft(0.01)

    if(char == "x"):
        print("Kraj")
        break


try:
    #RunForward(0.0001)
    #RunBackward(0.0001)
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
