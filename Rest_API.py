from flask import Flask, abort, jsonify, request

from Logger import Logger
from LightSensorController import LightSensorController
from time import localtime, strftime

app = Flask(__name__)

_log = Logger()
_lightSensorController = LightSensorController()

def startWebApi():
    app.run(debug=True, host="0.0.0.0", threaded=True)


@app.route('/lightsensor')
def poolpump():
    _log.info("GET Request received: " + str(request))
    lightLevel = _lightSensorController.getLightLevel()
    _log.info("LightSensor Level Status [" + str(lightLevel) + "]")
    return jsonify(Device="LightSensor", LightLevel=lightLevel,
                   Timestamp=strftime("%a, %d %b %Y %H:%M:%S +0000", localtime()))


startWebApi()