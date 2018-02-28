from flask import Flask
import Edison
import json

app = Flask(__name__)
edison = Edison.Edison()

@app.route('/is_party')
def isParty():
    active = edison.isParty()
    if active:
        data = {"answer": "yes"}
    else:
        data = {"answer": "no"}
    data_json = json.dumps(data)
    return data_json


@app.route('/loudness')
def getLoudness():
    data = {"answer": str(edison.getLoudness())}
    data_json = json.dumps(data)
    return data_json


@app.route('/brightness')
def getBrightness():
    data = {"answer": str(edison.getBrightness())}
    data_json = json.dumps(data)
    return data_json


@app.route('/vibration')
def getVibration():
    data = {"answer": str(edison.getVibration())}
    data_json = json.dumps(data)
    return data_json


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True, host='0.0.0.0', port = 8998)