import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! You are looking might fine today.'
