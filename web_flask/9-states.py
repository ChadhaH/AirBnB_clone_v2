#!/usr/bin/python3
"""
    script that starts a Flask web application
"""

from flask import Flask, render_template
import models

app = Flask("__name__")


@app.teardown_appcontext
def refresh(excep):
    models.storage.close()


@app.route("/states", strict_slashes=False)
def states():
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    for states in storage.all("State").values():
        if states.id == id:
            return render_template("9-states.html", state=states)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
