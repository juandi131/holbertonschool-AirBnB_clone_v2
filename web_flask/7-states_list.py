#!/usr/bin/python3
"""Module to start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    return render_template("7-states_list.html", storages=storage.all(State))


@app.teardown_appcontext
def remove_current_sql_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")

