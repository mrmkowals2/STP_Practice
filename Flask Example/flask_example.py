"""
To run this program, be sure to run cmd as administrator
and enter the following command to download Flask:
pip install Flask==0.11.1
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Pepe!"

app.run(port=8000)
