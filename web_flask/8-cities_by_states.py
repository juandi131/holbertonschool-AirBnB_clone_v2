#!/usr/bin/python3
""" Task 8 """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def storage_close(self):
    """close the sesion"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ show the list of states"""
    return render_template("8-cities_by_states.html",
                           states=storage.all(State))


if __name__ == '__main__':
    """ start the web app """
    app.run(host='0.0.0.0', port=5000)
