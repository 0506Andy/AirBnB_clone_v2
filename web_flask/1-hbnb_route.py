#!/usr/bin/python3

""" Import the Flask class from the flask module """
from flask import Flask

""" Create an instance of the Flask class """
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    Handle requests to the root URL (/)
    Returns 'Hello HBNB!'
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Handle requests to the /hbnb URL
    Returns 'HBNB'
    """
    return 'HBNB'

""" Start the Flask application """
if __name__ == '__main__':
    """
    Run the app on all available network interfaces at port 5000
    """
    app.run(host='0.0.0.0', port=5000)

