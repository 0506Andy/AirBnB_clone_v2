#!/usr/bin/python3
"""
Flask web application to display states and their cities.
"""

from flask import Flask, render_template, abort
from models import storage

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()

@app.route('/states', strict_slashes=False)
def states():
    """
    Displays a list of all State objects sorted by name.
    """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    
    return render_template('9-states.html', states=sorted_states, type='list')

@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """
    Displays details about a specific State and its Cities.
    """
    state = storage.all("State").get(f"State.{id}")
    if not state:
        return render_template('9-states.html', type='not_found')
    
    cities = state.cities if hasattr(state, 'cities') else state.cities()
    sorted_cities = sorted(cities, key=lambda city: city.name)
    
    return render_template('9-states.html', state=state, cities=sorted_cities, type='detail')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

