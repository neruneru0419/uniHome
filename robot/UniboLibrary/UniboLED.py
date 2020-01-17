import RPi.GPIO as GPIO
import time
from threading import Thread


def led_fade():
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

        r.stop()
        GPIO.output(rPin, GPIO.HIGH)
        GPIO.cleanup()

    except KeyboardInterrupt:
        r.stop()
        g.stop()
        GPIO.output(rPin, GPIO.HIGH)
        GPIO.output(gPin, GPIO.HIGH)
        GPIO.cleanup()

        
def red_led_fade():
    rPin = 21

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(rPin, GPIO.OUT)
    GPIO.output(rPin, GPIO.LOW)
    r = GPIO.PWM(rPin, 1000)
    r.start(0)

    try:
        for i in range(5):
            for dc in range(0, 101, 4):
                r.ChangeDutyCycle(dc)
                time.sleep(0.05)
            time.sleep(1)
            for dc in range(100, -1, -4):
                r.ChangeDutyCycle(dc)
                time.sleep(0.05)
            time.sleep(1)

        r.stop()
        GPIO.output(rPin, GPIO.HIGH)
        #GPIO.cleanup()
    except KeyboardInterrupt:
        r.stop()
        GPIO.output(rPin, GPIO.HIGH)
        GPIO.cleanup()

def sound():
    SOUNDER = 27

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SOUNDER, GPIO.OUT, initial = GPIO.LOW)

    Hz = 100
    p = GPIO.PWM(SOUNDER, 1)

    p.start(50)

    for _ in range(1, 20):

        p.ChangeFrequency(440)
        time.sleep(0.5)
        p.ChangeFrequency(880)
        time.sleep(0.5)

    p.stop()
    #GPIO.cleanup()


def danger():
    thread_audio = Thread(target=sound)
    thread_led = Thread(target=red_led_fade)

    thread_audio.start()
    thread_led.start()
if __name__ == "__main__":
    sound()
