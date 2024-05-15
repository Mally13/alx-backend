#!/usr/bin/env python3
"""Defines app routes"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    Defines app route /
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
