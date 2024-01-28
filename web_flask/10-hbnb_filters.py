#!/usr/bin/python3
"""
    script that starts a Flask web application
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(excep):
    storage.close()


def hbnb_filters():
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
