### IMPORTS ###

import flask

### CONSTANTS AND SETUP ###

app = flask.Flask(__name__)

### FUNCTIONS AND CLASSES ###


### ROUTES ###

@app.route('/ping')
def ping():
    return flask.jsonify({"status": "ok", "message": "pong"}), 200

if __name__ == "__main__":
    app.run("0.0.0.0", host="0.0.0.0", port=5000, threads=4)