# !usr/bin/env python3

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "key"  # Will be changed afterwards.
socketio = SocketIO(app)


@app.route("/")
def index() -> str:
    return ""


if __name__ == "__main__":
    socketio.run(app, cors_allowed_origins=["http://localhost:3000"])
