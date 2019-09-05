import RPi.GPIO as GPIO
import time

rPin = 21
gPin = 15

GPIO.setmode(GPIO.BCM)

GPIO.setup(rPin, GPIO.OUT)
GPIO.output(rPin, GPIO.LOW)  
r = GPIO.PWM(rPin, 1000)
r.start(0)

GPIO.setup(gPin, GPIO.OUT)
GPIO.output(gPin, GPIO.LOW)  
g = GPIO.PWM(gPin, 1000)
g.start(0)

try:
    while True:
        for dc in range(0, 101, 4):
            r.ChangeDutyCycle(dc)
            g.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(1)
        for dc in range(100, -1, -4):
            r.ChangeDutyCycle(dc)
            g.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(1)

except KeyboardInterrupt:
    r.stop()
    g.stop()
    GPIO.output(rPin, GPIO.HIGH)
    GPIO.output(gPin, GPIO.HIGH)
    GPIO.cleanup()
