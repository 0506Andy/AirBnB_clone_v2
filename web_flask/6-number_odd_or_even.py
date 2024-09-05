#!/usr/bin/python3
"""
Flask web application with specific routes.

This script handles routes including number odd/even check.
"""

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """
    Displays "Hello HBNB!".
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB".
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays "C " followed by text with underscores replaced by spaces.
    """
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Displays "Python " followed by text with underscores replaced by spaces.
    """
    text = text.replace('_', ' ')
    return f"Python {text}"

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays "{n} is a number".
    """
    return f"{n} is a number"

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page with "Number: {n}".
    """
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Number Template</title>
    </head>
    <body>
        <h1>Number: {{ n }}</h1>
    </body>
    </html>
    '''
    return render_template_string(html_template, n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays an HTML page with "Number: {n} is even" or "odd".
    """
    with open('oddeven.html', 'r') as file:
        html_template = file.read()
    parity = 'even' if n % 2 == 0 else 'odd'
    return render_template_string(html_template, n=n, parity=parity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

