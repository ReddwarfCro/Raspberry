import RPi.GPIO as GPIO
import time

pin = 40

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.IN)

input = GPIO.input(pin)

while True:
	if (GPIO.input(pin)):
		print("In Range")
	time.sleep(1)