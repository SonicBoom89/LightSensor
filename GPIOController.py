import RPi.GPIO as GPIO
import time


class GPIOController:

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)  # GPIO Nummer via Board Nummern

    def readFromGPIO(self, gpioPin):
        GPIO.setup(gpioPin, GPIO.OUT)
        GPIO.output(gpioPin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(gpioPin, GPIO.IN)

        count = 0
        while (GPIO.input(gpioPin) == GPIO.LOW):
            count += 1
        return count

    def cleanUp(self):
        GPIO.clenup()
