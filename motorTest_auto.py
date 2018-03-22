import RPi.GPIO as GPIO
from datetime import datetime as dt
import sys, tty, termios, time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)

# set GPIO Pins
GPIO_TRIGGER = 12
GPIO_ECHO = 18

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

initial = True
state = False
starttime = dt.now()
pressed = False
speed = 30
lastDistance = 0

forwardLeft = GPIO.PWM(31, 50)
reverseLeft = GPIO.PWM(33, 50)

forwardRight = GPIO.PWM(37, 50)
reverseRight = GPIO.PWM(35, 50)


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

def TurnOff():
    forwardLeft.stop()
    reverseLeft.stop()
    forwardRight.stop()
    reverseRight.stop()

TurnOff()

print("Spreman!")

#while True:
#    char = getch()
#    if(char == "w"):
#        forwardRight.start(speed)
#        forwardLeft.start(speed)
#        forwardLeft.ChangeDutyCycle(speed)
#        forwardRight.ChangeDutyCycle(speed)
#    elif(char == "s"):
#        reverseRight.start(speed)
#        reverseLeft.start(speed)
#        reverseLeft.ChangeDutyCycle(speed)
#        reverseRight.ChangeDutyCycle(speed)
#    elif(char == "d"):
#        forwardRight.start(speed)
#        forwardRight.ChangeDutyCycle(speed)
#    elif(char == "a"):
#        forwardLeft.start(speed)
#        forwardLeft.ChangeDutyCycle(speed)
#    elif (char == "f"):
#        speed = speed - 5
#        if (speed < 20):
#            speed = 20
#        print(speed)
#    elif (char == "r"):
#        speed = speed + 5
#        if (speed > 100):
#            speed = 100
#        print(speed)
#    elif(char == "x"):
#        TurnOff()
#        break
#    else:
#	TurnOff()


try:
    while True:
        dist = distance()
        if dist > 50:
            dist = lastDistance
        if dist < 10:
            TurnOff()
        else:
            forwardRight.start(speed)
            forwardLeft.start(speed)
            forwardLeft.ChangeDutyCycle(speed)
            forwardRight.ChangeDutyCycle(speed)
        time.sleep(0.1)
        lastDistance = dist

    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()
