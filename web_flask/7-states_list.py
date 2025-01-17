#!/usr/bin/python3
"""
    script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(excep):
    if storage is not None:
        storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    data = storage.all(State)
    return render_template('7-states_list.html', total=data.values())


if __name__ == "__main__":
    app.run(host="0.0.0.0")
