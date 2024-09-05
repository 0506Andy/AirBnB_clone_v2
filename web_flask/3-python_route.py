#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return f'C {text}'

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Display 'Python ' followed by the text variable, replacing underscores with spaces.
    Default value for text is 'is cool'.
    """
    text = text.replace('_', ' ')
    return f'Python {text}'

if __name__ == '__main__':
    # Run the app on all available network interfaces at port 5000
    app.run(host='0.0.0.0', port=5000)

