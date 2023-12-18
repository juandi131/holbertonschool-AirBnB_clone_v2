#!/usr/bin/python3
""" start web application """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def lists():
    return render_template('7-states_list.html', data=storage.all(State))


@app.teardown_appcontext
def close(exception=None):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
