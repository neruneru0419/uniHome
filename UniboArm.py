import RPi.GPIO as GPIO
import time
import threading

class Arm:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(24, GPIO.OUT)
        self.right = GPIO.PWM(24, 50)
        self.right.start(0)

        GPIO.setup(23, GPIO.OUT)
        self.left = GPIO.PWM(23, 50)
        self.left.start(0)

        self.val = [2.5, 3.6875, 4.875, 6.0625, 7.25, 8.4375, 9.625, 10.8125, 12]
 
    def default(self):
        self.right.ChangeDutyCycle(self.val[0])
        self.left.ChangeDutyCycle(self.val[8])

    def oyasumi(self): 
        self.right.ChangeDutyCycle(self.val[7])
        self.left.ChangeDutyCycle(self.val[1])

    def tadaima(self):
        self.right.ChangeDutyCycle(self.val[5])
        self.left.ChangeDutyCycle(self.val[8])

    def ohayou(self):
        self.right.ChangeDutyCycle(self.val[5])
        self.left.ChangeDutyCycle(self.val[3])

    def dance(self):
        for i in range(5):
            self.right.ChangeDutyCycle(self.val[0])
            self.left.ChangeDutyCycle(self.val[3])
            time.sleep(0.5)

            self.right.ChangeDutyCycle(self.val[5])
            self.left.ChangeDutyCycle(self.val[8])
            time.sleep(0.5)
    def move_arm(self):
        self.oyasumi()
        time.sleep(2)
        self.tadaima()
        time.sleep(2)
        self.ohayou()
        time.sleep(2)
        self.dance()
        time.sleep(2)
        self.default()
