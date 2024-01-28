#!/usr/bin/python3
"""
    script that starts a Flask web application

"""
from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def display(text):
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def num_display(n):
    eturn "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_html(n):
    return render_template('5-number.html', name=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', name=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
