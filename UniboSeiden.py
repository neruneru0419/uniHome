import RPi.GPIO as GPIO
import time
class TouchSensor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(14, GPIO.IN)

        GPIO.setup(24, GPIO.OUT)
        self.right = GPIO.PWM(24, 50)
        self.right.start(0)

        GPIO.setup(23, GPIO.OUT)
        self.left = GPIO.PWM(23, 50)
        self.left.start(0)

    def dance(self):
        for i in range(5):
            self.right.ChangeDutyCycle(2.5)
            self.left.ChangeDutyCycle(4.875)
            time.sleep(0.5)

            self.right.ChangeDutyCycle(9.625)
            self.left.ChangeDutyCycle(12)
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
        self.dance()
unibo_dance = TouchSensor()
unibo_dance.touch_dance()
print("finish")

GPIO.cleanup()
