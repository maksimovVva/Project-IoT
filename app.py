from flask import Flask
import Edison
import json

app = Flask(__name__)
edison = Edison.Edison()

@app.route('/isParty')
def isParty():
    active = edison.isParty()
    if active:
        data = "PARTY IS DETECTED!"
    else:
        data = "There are no party :("
    return data


@app.route('/loudness')
def getLoudness():
    data = "Sound is " +str(edison.getLoudness())
    return data


@app.route('/brightness')
def getBrightness():
    data = "Light is " +str(edison.getBrightness())
    return data


@app.route('/vibration')
def getVibration():
    data = "Vibration is " + str(edison.getVibration())
    return data

@app.route('/allSensors')
def getVibration():
    data = "Sound is " + str(edison.getLoudness())
    data += "\nLight is " + str(edison.getBrightness())
    data += "\nVibration is " + str(edison.getVibration())
    active = edison.isParty()
    if active:
        data += "\n\nPARTY IS DETECTED!"
    else:
        data += "\n\nThere are no party :("
    return data


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True, host='0.0.0.0', port = 8998)