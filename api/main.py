from contextlib import redirect_stdout
from io import StringIO
from string import ascii_uppercase

from flask import Flask, jsonify, request

from algo import bye_tracking

app = Flask(__name__)


@app.get("/get-message")
def read_root():
    return jsonify({"Message": "Congrats! This is your first API!"})


@app.post("/api/schedule")
def create_schedule():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Send a JSON object."}), 400

    players = data.get("players")
    sessions = data.get("sessions")
    if type(players) is not int or not 4 <= players <= len(ascii_uppercase):
        return jsonify({"error": "Players must be a number from 4 to 26."}), 400
    if type(sessions) is not int or sessions < 1:
        return jsonify({"error": "Sessions must be a positive number."}), 400

    output = StringIO()
    with redirect_stdout(output):
        bye_tracking(list(ascii_uppercase[:players]), sessions)

    return jsonify({"output": output.getvalue()})
