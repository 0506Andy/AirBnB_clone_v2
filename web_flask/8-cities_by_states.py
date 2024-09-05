#!/usr/bin/python3
"""
Flask web application to display cities by states.
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Displays a list of all State objects with their City objects.
    """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('8-cities_by_states.html', states=sorted_states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

