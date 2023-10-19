#!/usr/bin/env python3
"""Basic Babel setup"""

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """config class for babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    return "yes", 200


if __name__ == "__main__":
    app.run(debug=True)
