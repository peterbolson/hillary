from flask import render_template
from . import app

from word_cloud import WordCloudScraper
import json

@app.route('/')
def index():
    wcs = WordCloudScraper()
    words = wcs.word_counts()
    welcome_message = 'Hello World! You are looking might fine today.'
    return render_template('index.html',
            welcome_message=welcome_message,
            words=json.dumps(words))
