#!/usr/bin/env python3
"""Basic Babel setup & Parametrize templates"""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__, template_folder="templates")
babel = Babel(app)


class Config():
    """config class for babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """get_locale method that determine the best match
    with our supported languages for the client's browser"""
    locale = request.args.get("locale")
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """index method to render default template"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
