import RPi.GPIO as GPIO
import time
class touchSensor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(14, GPIO.IN)

        GPIO.setup(24, GPIO.OUT)
        right = GPIO.PWM(24, 50)
        right.start(0)

        GPIO.setup(23, GPIO.OUT)
        left = GPIO.PWM(23, 50)
        left.start(0)

    def dance(self):
        for i in range(5):
            right.ChangeDutyCycle(2.5)
            left.ChangeDutyCycle(4.875)
            time.sleep(0.5)

            right.ChangeDutyCycle(9.625)
            left.ChangeDutyCycle(12)
            time.sleep(0.5)

    print("start")


    def touch_dance(self):
        j = 0
        while j < 1.5:
            if GPIO.input(14) != 0:
                j += 0.1
            else:
                j = 0

            time.sleep(0.1)
    dance()

touch_dance()
print("finish")

GPIO.cleanup()
