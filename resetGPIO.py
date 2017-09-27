import logging
import RPi.GPIO as GPIO
import requests
import socket
import fcntl
import struct

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

payload = {'name':str(get_ip_address('wlx3c3300213b66'))}

url = 'http://vinkovicnodejs.herokuapp.com/api/ip'
#payload = {'name':'test'}

r = requests.post(url, json=payload)

print(r.text)
print(r.status_code)

try:
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.setup(35, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)
    GPIO.cleanup()
except:
    logger.error("E nesto nije u redu")



logger.info('Masina se rebutala i resetirala GPIO')

