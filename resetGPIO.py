import logging
import RPi.GPIO as GPIO
import requests
import socket
import fcntl
import struct
import time

logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/home/pi/logs/startup.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.INFO)

def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, 
		struct.pack('256s', ifname[:15])
	)[20:24])

while True:
    try:
        logger.info(get_ip_address('wlx3c3300213b66'))
        payload = {'name':str(get_ip_address('wlx3c3300213b66'))}
        url = 'http://vinkovicnodejs.herokuapp.com/api/ip'
        r = requests.post(url, json=payload)
        break
    except:
        time.sleep(5)

while True:
    try:
        GPIO.setmode(GPIO.BOARD) 
        GPIO.setup(31, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)
        GPIO.setup(35, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)
        GPIO.cleanup()
        break
    except:
        logger.info("E nesto nije u redu")



logger.info('Masina se rebutala i resetirala GPIO')

