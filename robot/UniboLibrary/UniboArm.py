import RPi.GPIO as GPIO
import time
import threading

def greeting(words):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(24, GPIO.OUT)
    right = GPIO.PWM(24, 50)
    right.start(0)

    GPIO.setup(23, GPIO.OUT)
    left = GPIO.PWM(23, 50)
    left.start(0)

    val = [2.5, 3.6875, 4.875, 6.0625, 7.25, 8.4375, 9.625, 10.8125, 12]

    if words == "おやすみ": 
        right.ChangeDutyCycle(val[7])
        left.ChangeDutyCycle(val[1])
        time.sleep(5)
    elif words == "ただいま" or words == "おかえり":
        right.ChangeDutyCycle(val[5])
        left.ChangeDutyCycle(val[8])
        time.sleep(5)
    elif words == "おはよう":
        right.ChangeDutyCycle(val[5])
        left.ChangeDutyCycle(val[3])
        time.sleep(5)
    right.ChangeDutyCycle(val[0])
    left.ChangeDutyCycle(val[8])
    time.sleep(1)
