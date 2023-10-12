#!/usr/bin/env python3
"""Basic Flask app"""

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=["GET"])
def bienvenue():
    """bienvenue method"""
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", methods=["POST"])
def register():
    """register end-point"""
    content = request.json
    email = content["email"]
    password = content["password"]
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
