#!/usr/bin/python3
""""""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


def teardown_appcontext(exception=None):

    storage.close()


app.teardown_appcontext(teardown_appcontext)


@app.route('/states_list', strict_slashes=False)
def states_list():

    states = storage.all(State)
    sorted_states = {state.id: state for state in
                     sorted(states.values(), key=lambda x: x.name)}
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
