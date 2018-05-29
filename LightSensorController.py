import time
from GPIOController import GPIOController
from Logger import Logger


class LightSensorController:

    GPIO_PIN = 7

    def __init__(self):
        self._log = Logger()
        self._GPIOController = GPIOController()

    def dispose(self):
        self._log.info("Disposing GPIOController...")
        self._GPIOController.cleanUp()

    def getLightLevel(self):
        lightLevel = GPIOController.readFromGPIO(self.GPIO_PIN)
        self._log.info("Lightlevel " + str(lightLevel))
        return lightLevel

