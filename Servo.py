import RPi.GPIO as GPIO
import time
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)

# set GPIO Pins
GPIO_TRIGGER = 12
GPIO_ECHO = 18

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

pwm=GPIO.PWM(03, 50)

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

pwm.start(7.5)
wait = 1 

try:
	while True:
		pwm.ChangeDutyCycle(7.5)
        	print(distance())
		sleep(wait)
		pwm.ChangeDutyCycle(9.1)
        	print(distance())
		sleep(wait)
		pwm.ChangeDutyCycle(10.7)
        	print(distance())
		sleep(wait)
		pwm.ChangeDutyCycle(12.5)
        	print(distance())
		sleep(wait)
		pwm.ChangeDutyCycle(7.5)
        	print(distance())
		sleep(wait)
		pwm.ChangeDutyCycle(5.9)
        	print(distance())
		sleep(wait)
		pwm.ChangeDutyCycle(4.3)
        	print(distance())
		sleep(wait)
		pwm.ChangeDutyCycle(2.5)
        	print(distance())
		sleep(wait)

except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()
