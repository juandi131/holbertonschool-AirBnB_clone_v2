#!/usr/bin/python3
""" start web application """

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHBNB():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def Text(text):
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def Pyth(text='is_cool'):
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def numb(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def temp(n):
    return render_template('5-number.html', data=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def OdEv(n):
    return render_template('6-number_odd_or_even.html', data=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
