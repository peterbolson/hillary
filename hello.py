import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    welcome_message = 'Hello World! You are looking might fine today.'
    print welcome_message
    return render_template('index.html', welcome_message=welcome_message)

if __name__ == '__main__':
    if os.environ.get("FLASK_DEBUG") == 'True':
         app.debug = True
    app.run()
