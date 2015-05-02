import requests
from bs4 import BeautifulSoup

url = "https://www.hillaryclinton.com/"

class WordCloudScraper:

    def __init__(self):
        self.text = requests.get(url).text

    def word_counts(self):
        return [("happy",2),("sad",1)]
