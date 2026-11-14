from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/get-message")
def read_root():
    return jsonify({"Message": "Congrats! This is your first API!"})