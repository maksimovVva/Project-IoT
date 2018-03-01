from flask import Flask
import json

app = Flask(__name__)

@app.route('/loudness')
def getLoudness():
    data = {"answer": "55"}
    data_json = json.dumps(data)
    return data_json

if __name__ == "__main__":
    app.debug = True
    app.run(debug=True, host='0.0.0.0', port = 8998)