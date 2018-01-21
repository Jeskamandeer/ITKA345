import RPi.GPIO as GPIO
import time

LED=16
PAINIKE=6

GPIO.setmode (GPIO.BCM)
GPIO.setup (LED, GPIO.OUT)
GPIO.setup (PAINIKE, GPIO.IN)

loppu = time.time() + 10
while time.time() < loppu:
	GPIO.output(LED, GPIO.input (PAINIKE))
	time.sleep (0.1) # ilman tata prossukaytto 100%

GPIO.cleanup ()