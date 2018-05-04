import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)

pwm=GPIO.PWM(03, 50)

pwm.start(0)

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(03, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(03, False)
	pwm.ChangeDutyCycle(0)

SetAngle(180)
SetAngle(225)
SetAngle(270)
SetAngle(315)
SetAngle(270)
SetAngle(225)
SetAngle(180)
SetAngle(135)
SetAngle(90)
SetAngle(45)
SetAngle(90)
SetAngle(135)
SetAngle(180)

pwm.stop()
GPIO.cleanup()