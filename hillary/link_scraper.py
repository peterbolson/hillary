import requests
from bs4 import BeautifulSoup

urls = ["http://www.economist.com/topics/hillary-clinton"]
selectors = [".topic-item-title a"]

class LinkScraper:

    def __init__(self):
        link_sets = []
        for url,selector in zip(urls,selectors):
            html = requests.get(url).text
            soup = BeautifulSoup(html)
            links = soup.select(selector)
            link_sets.append(links)
        self.link_sets = link_sets

    def get_links(self):
        return None
