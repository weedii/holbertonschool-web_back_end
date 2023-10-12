#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, jsonify

app = Flask(__name__)

hello = {"message": "Bienvenue"}

app.route('/', methods=["GET"])


def bienvenue():
    """bienvenue method"""
    return jsonify(hello)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
