from flask import Flask, jsonify
from datetime import datetime, timezone
import socket

app = Flask(__name__)


@app.route("/api/v1/details")
def info():
    return jsonify({
        "time": datetime.now(timezone.utc).strftime("%I:%M:%S%p on %B %d, %Y"),
        "hostname": socket.gethostname(),
        "message": "You are doing great, little human! <3",
        "deployed_on": "kubernetes",
    })


@app.route("/api/v1/healthz")
def health():
    return jsonify({"status": "up"}), 200


@app.route("/api/v1/readyz")
def ready():
    return jsonify({"status": "ready"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
