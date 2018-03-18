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

forwardLeft = GPIO.PWM(31, 100)
reverseLeft = GPIO.PWM(33, 100)

forwardRight = GPIO.PWM(37, 100)
reverseRight = GPIO.PWM(35, 100)


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def TurnOff():
    forwardLeft.stop()
    reverseLeft.stop()
    forwardRight.stop()
    reverseRight.stop()

TurnOff()

print("Spreman!")

while True:
    char = getch()
    if(char == "w"):
        forwardRight.start(50)
        forwardLeft.start(50)
        forwardLeft.ChangeDutyCycle(50)
        forwardRight.ChangeDutyCycle(50)

    #if(char == "s"):
        #print("nazad")
        #RunBackward(0.01)

    #if(char == "d"):
        #print("desno")
        #RunRight(0.01)

    #if(char == "a"):
        #print("lijevo")
        #RunLeft(0.01)

    if(char == "x"):
        TurnOff()
        break


try:
    #RunForward(0.0001)
    #RunBackward(0.0001)
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
