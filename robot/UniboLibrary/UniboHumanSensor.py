import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
def human_sensor():
    try:
        return bool(GPIO.input(26))
    except(KeyboardInterrupt):
        print("interrupt")
    GPIO.cleanup()
def test_human():
    while True:
        print(GPIO.input(26))

if __name__ == "__main__":
    test_human()
