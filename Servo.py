import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)

pwm=GPIO.PWM(03, 50)

pwm.start(7.5)

try:
	while True:
		pwm.ChangeDutyCycle(7.5)
		sleep(1)
		pwm.ChangeDutyCycle(9.1)
		sleep(1)
		pwm.ChangeDutyCycle(10.7)
		sleep(1)
		pwm.ChangeDutyCycle(12.5)
		sleep(1)
		pwm.ChangeDutyCycle(10.7)
		sleep(1)
		pwm.ChangeDutyCycle(9.1)
		sleep(1)
		pwm.ChangeDutyCycle(7.5)
		sleep(1)
		pwm.ChangeDutyCycle(5.9)
		sleep(1)
		pwm.ChangeDutyCycle(4.3)
		sleep(1)
		pwm.ChangeDutyCycle(2.5)
		sleep(1)

except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()