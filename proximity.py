import RPi.GPIO as GPIO
import time

rightPin = 40
leftPin = 38

GPIO.setmode(GPIO.BOARD)

GPIO.setup(rightPin, GPIO.IN)
GPIO.setup(leftPin, GPIO.IN)

input = GPIO.input(rightPin)
input2 = GPIO.input(leftPin)

while True:
	if GPIO.input(rightPin) == False:
		print("right")
    elif GPIO.input(leftPin) == False:
        print("left")

	time.sleep(0.1)

