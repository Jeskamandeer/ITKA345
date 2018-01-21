import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


LED=4

GPIO.setmode (GPIO.BCM)
GPIO.setup (LED, GPIO.OUT)

for i in range (0, 100):
	GPIO.output (LED, 1)
	time.sleep (0.1)
	GPIO.output (LED, 0)
	time.sleep (0.1)

GPIO.cleanup ()