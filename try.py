from flask import Flask

app = Flask(__name__)

@app.route('/loudness')
def getLoudness():
    return "55"

@app.route('/brightness')
def getbrightness():
    return "56"

@app.route('/vibration')
def getvibration():
    return "57"

@app.route('/isParty')
def getisParty():
    return "58"

@app.route('/allSensors')
def getallSensors():
    return "59"

if __name__ == "__main__":
    app.debug = True
    app.run(debug=True, host='0.0.0.0', port = 8998)