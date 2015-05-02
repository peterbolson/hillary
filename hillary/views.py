from flask import render_template
from . import app

from word_cloud import WordCloudScraper
from link_scraper import LinkScraper

import json

@app.route('/')
def index():

    # create word cloud
    wcs = WordCloudScraper()
    words = wcs.word_counts()

    # scrape links from common websites
    ls = LinkScraper()
    links = ls.get_links()

    welcome_message = 'NO.'
    return render_template('index.html',
            welcome_message=welcome_message,
            words=json.dumps(words),
            links=links)
