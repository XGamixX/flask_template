### IMPORTS ###

import flask

### CONSTANTS AND SETUP ###

app = flask.Flask(__name__)

### FUNCTIONS AND CLASSES ###


### WEB PAGE ROUTES ###

@app.route('/')
def index():
    return flask.render_template("index.html"), 200

### API ROUTES ###

@app.route('/ping')
def ping():
    return flask.jsonify({"status": "ok", "message": "pong"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
