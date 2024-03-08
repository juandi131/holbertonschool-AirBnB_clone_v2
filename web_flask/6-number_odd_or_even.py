#!/usr/bin/python3
""" Task 6 """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Hello HBNB """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """C + text"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """ Python is cool """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_is_integer(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_templates(n):
    return render_template("5-number.html", num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if (n % 2) == 0:
        n_is = 'even'
    else:
        n_is = 'odd'
    context = {'num': n, 'n_is': n_is}
    return render_template("6-number_odd_or_even.html", **context)


if __name__ == '__main__':
    """ start the web app """
    app.run(host='0.0.0.0', port=5000)
