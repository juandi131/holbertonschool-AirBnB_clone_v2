#!/usr/bin/python3
""" Task 0 """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """ Hello HBNB """
    return 'Hello HBNB!'


if __name__ == '__main__':
    """ start the web app"""
    app.run(host='0.0.0.0', port=5000)
