import re
import string
from collections import defaultdict

import requests
from bs4 import BeautifulSoup

urls = ["https://www.hillaryclinton.com/",
        "https://www.hillaryclinton.com/about/bio/"]

class WordCloudScraper:

    def __init__(self):
        raw_texts = []
        for url in urls:
            html = requests.get(url).text
            soup = BeautifulSoup(html)
            raw_texts.append(soup.findAll(text=True))
        self.raw_texts = raw_texts
        self.stopwords = ["a", "about", "above", "after", "again",
                "against", "all", "am", "an", "and", "any",
                "are", "aren't", "as", "at", "be", "because",
                "been", "before", "being", "below", "between",
                "both", "but", "by", "can't", "cannot", "could",
                "couldn't", "did", "didn't", "do", "does", "doesn't",
                "doing", "don't", "down", "during", "each", "few",
                "for", "from", "further", "had", "hadn't", "has",
                "hasn't", "have", "haven't", "having", "he", "he'd",
                "he'll", "he's", "her", "here", "here's", "hers",
                "herself", "him", "himself", "his", "how", "how's",
                "i", "i'd", "i'll", "i'm", "i've", "if",
                "in", "into", "is", "isn't", "it", "it's",
                "its", "itself", "let's", "me", "more", "most",
                "mustn't", "my", "myself", "no", "nor", "not",
                "of", "off", "on", "once", "only", "or",
                "other", "ought", "our", "ours", "ourselves", "out",
                "over", "own", "same", "shan't", "she", "she'd",
                "she'll", "she's", "should", "shouldn't", "so", "some",
                "such", "than", "that", "that's", "the", "their",
                "theirs", "them", "themselves", "then", "there", "there's",
                "these", "they", "they'd", "they'll", "they're", "they've",
                "this", "those", "through", "to", "too", "under",
                "until", "up", "very", "was", "wasn't", "we",
                "we'd", "we'll", "we're", "we've", "were", "weren't",
                "what", "what's", "when", "when's", "where", "where's",
                "which", "while", "who", "who's", "whom", "why",
                "why's", "with", "won't", "would", "wouldn't", "you",
                "you'd", "you'll", "you're", "you've", "your",
                "yours", "yourself", "yourselves"]

    def word_counts(self):
        counts = defaultdict(lambda: 0)
        for texts in self.raw_texts:
            visible_texts = filter(self.visible,texts)
            words = [t.lower().translate({ord(char): None for char in u'!"#%\'()*+,-./:;<=>?@[\]^_`{|}~'})
                     for text in visible_texts
                     for t in text.split()
                     if t.lower() not in self.stopwords]
            for word in words:
                counts[word] += 1
        counts = sorted(list(counts.items()), key=lambda x: x[1],reverse=True)
        return counts

    @staticmethod
    def visible(element):
        string = str(element.encode('utf-8', 'ignore'))
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        elif re.match('\s*<!--.*-->', string):
            return False
        elif re.match('\n', string):
            return False
        elif re.match('\[if.*', string):
            return False
        elif re.match('./', string):
            return False
        elif re.match('<', string):
            return False
        return True

