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
speed = 50

forwardLeft = GPIO.PWM(31, 50)
reverseLeft = GPIO.PWM(33, 50)

forwardRight = GPIO.PWM(37, 50)
reverseRight = GPIO.PWM(35, 50)

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
        forwardRight.start(speed)
        forwardLeft.start(speed)
        forwardLeft.ChangeDutyCycle(speed)
        forwardRight.ChangeDutyCycle(speed)
    elif(char == "s"):
        reverseRight.start(speed)
        reverseLeft.start(speed)
        reverseLeft.ChangeDutyCycle(speed)
        reverseRight.ChangeDutyCycle(speed)
    elif(char == "d"):
        forwardRight.start(speed)
        forwardRight.ChangeDutyCycle(speed)
    elif(char == "a"):
        forwardLeft.start(speed)
        forwardLeft.ChangeDutyCycle(speed)
    elif (char == "f"):
        speed = speed - 5
        if (speed < 20):
            speed = 20
        print(speed)
    elif (char == "r"):
        speed = speed + 5
        if (speed > 100):
            speed = 100
        print(speed)
    elif(char == "x"):
        TurnOff()
        break
    else:
	TurnOff()


try:
    #RunForward(0.0001)
    #RunBackward(0.0001)
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
