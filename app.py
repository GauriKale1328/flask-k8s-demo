import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v1")

PAGE = """
<!doctype html>
<html>
<head>
  <title>Cloud-Native Demo</title>
  <style>
    body {{ font-family: Arial, sans-serif; background:#0f172a; color:#e2e8f0;
           display:flex; align-items:center; justify-content:center; height:100vh; margin:0; }}
    .card {{ background:#1e293b; padding:40px 60px; border-radius:16px; text-align:center;
            box-shadow:0 10px 30px rgba(0,0,0,.4); }}
    h1 {{ margin:0 0 10px; color:#38bdf8; }}
    .pod {{ font-size:22px; color:#facc15; font-weight:bold; }}
    .ver {{ margin-top:10px; color:#4ade80; }}
  </style>
</head>
<body>
  <div class="card">
    <h1>Docker + Kubernetes Demo</h1>
    <p>Served by pod:</p>
    <div class="pod">{pod}</div>
    <div class="ver">App version: {version}</div>
    <p style="color:#94a3b8">Refresh the page to see load balancing across pods</p>
  </div>
</body>
</html>
"""


@app.route("/")
def home():
    return PAGE.format(pod=socket.gethostname(), version=APP_VERSION)


@app.route("/health")
def health():
    return jsonify(status="OK"), 200


@app.route("/info")
def info():
    return jsonify(pod=socket.gethostname(), version=APP_VERSION)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
