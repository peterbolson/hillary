from flask import render_template
from . import app

from .word_cloud import WordCloudScraper

@app.route('/')
def index():
    welcome_message = 'NO.'
    return render_template('index.html', welcome_message=welcome_message)

