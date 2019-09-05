import RPi.GPIO as GPIO
import time
import disco
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN)

i = 0

while i < 1.8:
    if GPIO.input(14) != 0:
        i += 0.1
    else:
        i = 0

    time.sleep(0.1)
disco.disco()
#GPIO.cleanup()
