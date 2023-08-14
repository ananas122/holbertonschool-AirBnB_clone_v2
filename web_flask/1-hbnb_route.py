#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask

#Creer des instances à partir de la biblio Flask
# __name__ : pr determiner le nom du module actuel
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

