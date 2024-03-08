#!/usr/bin/python3
""" Task 10 """
from flask import Flask
from flask import render_template
from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def storage_close(self):
    """close the sesion"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def states():
    """Display a HTML page with the a list depending on filters.
    Route ("/hbnb_filters")
    """
    return render_template("10-hbnb_filters.html",
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values())


if __name__ == '__main__':
    """ start the web app """
    app.run(host='0.0.0.0', port=5000)
