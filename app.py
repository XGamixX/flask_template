import flask

app = flask.Flask(__name__)

@app.route('/ping')
def ping():
    return flask.jsonify({"status": "ok", "message": "pong"}), 200

if __name__ == "__main__":
    app.run("0.0.0.0")