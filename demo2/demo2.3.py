import RPi.GPIO as GPIO
import time


KAVP=20
KAVV=21

AUTP=4
AUTK=5
AUTV=6

painettu=0
PIR=24
NAPPI=26
GPIO.setmode(GPIO.BCM)

GPIO.setup(PIR, GPIO.IN)
GPIO.setup(NAPPI, GPIO.IN)

GPIO.setup (AUTP, GPIO.OUT)
GPIO.setup (AUTK, GPIO.OUT)
GPIO.setup (AUTV, GPIO.OUT)

GPIO.setup (KAVP, GPIO.OUT)
GPIO.setup (KAVV, GPIO.OUT)

def normitilanne():
	GPIO.output(KAVP, 1)
	GPIO.output(KAVV, 0)
	GPIO.output(AUTP, 0)
	GPIO.output(AUTK, 0)
	GPIO.output(AUTV, 1)
	painettu = 0
		

def vaihdavalot():
	GPIO.output(KAVP, 1)
	GPIO.output(AUTV, 1)
	time.sleep (3.0)
	GPIO.output(AUTV, 0)
	GPIO.output(AUTK, 1)
	time.sleep (1.0)
	GPIO.output(AUTK, 0)
	GPIO.output(AUTP, 1)
	GPIO.output(KAVP, 0)
	GPIO.output(KAVV, 1)
	time.sleep(3.0)
	GPIO.output(AUTK, 1)
	GPIO.output(AUTV, 0)
	GPIO.output(KAVP, 1)
	GPIO.output(KAVV, 0)
	time.sleep (1.0)
	GPIO.output(AUTV, 1)
	GPIO.output(AUTK, 0)
	
	
	
loppu = time.time() + 30
normitilanne()
while time.time() < loppu:
	if GPIO.input(NAPPI) == 1:
		
		if painettu == 0:
			vaihdavalot()
			
			painettu = 1
			normitilanne()
			painettu = 0
GPIO.cleanup()