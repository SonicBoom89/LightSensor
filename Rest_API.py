from flask import Flask, abort, jsonify, request

from Logger import Logger
from LightSensorController import LightSensorController
from TemperatureSensorController import TemperatureSensorController
from time import localtime, strftime


app = Flask(__name__)

_log = Logger()
_lightSensorController = LightSensorController()
_temperatureSensorController = TemperatureSensorController()

def startWebApi():
    app.run(debug=True, host="0.0.0.0", threaded=True)


@app.route('/lightsensor')
def lightsensor():
    _log.info("GET Request received: " + str(request))
    lightLevel = _lightSensorController.getLightLevel()
    _log.info("LightSensor Level Status [" + str(lightLevel) + "]")
    return jsonify(Device="LightSensor", LightLevel=lightLevel,
                   Timestamp=strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()))

@app.route('/temperature')
def temperature():
    _log.info("GET Request received: " + str(request))
    temperature = _temperatureSensorController.getTemperature()
    _log.info("Temperature [" + str(temperature) + "]")
    return jsonify(Device="Temperature Sensor", Temperature=temperature,
                   Timestamp=strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()))


startWebApi()