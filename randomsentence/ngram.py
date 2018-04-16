"""
Web-scraping OANC's http://www.anc.org/cgi-bin/ngrams.cgi
"""

import requests
from bs4 import BeautifulSoup
import string
from random import randrange
import re

from randomsentence.word import Word


class Oanc:
    def __init__(self, keyword: str=None, query: str=None):
        """
        Web-scraping OANC's http://www.anc.org/cgi-bin/ngrams.cgi

        :param str keyword: a keyword.
        If not specified, a word (beyond commonness of 100) is randomized from google-10000-english.txt
        :param str query: querying language as defined in OANC's http://www.anc.org/cgi-bin/ngrams.cgi
        If not specified, keyword is used instead.
        If specified, keyword is ignored.

        # >>> Oanc().raw
        # a search result of a random keyword from OANC
        """
        self.word = Word()

        if keyword is None:
            keyword = self.word.random()

        params = {
            'key': '* {} *'.format(keyword),
            'print_max': 100,
            'freq_threshold': 0,
            'output_style': 'sentence',
            'output_aux': 0,
            'print_format': 'text',
            'sort': None
        }
        if query is not None:
            params['key'] = query

        r = requests.get('http://www.anc.org/cgi-bin/ngrams.cgi', params=params)

        self.raw = re.sub('( [{}].?)'.format(string.punctuation), self.punctuation_rules,
                          BeautifulSoup(r.text, 'html.parser').text)

    def clip(self, number_of_words):
        """
        Clip the paragraphs in OANC to a limited number of words.

        :param int number_of_words: the number of words to be clipped
        :return str: a fragment of a sentence

        # >>> Oanc().clip(4)
        # side of the two-way mirror
        """
        space = [-1]
        for i, char in enumerate(self.raw):
            if char == ' ':
                try:
                    if self.raw[i+1] not in string.punctuation:
                        space.append(i)
                except ValueError:
                    pass

        not_word = []
        for i in range(len(space)-1):
            word = self.raw[space[i]+1:space[i+1]]
            if not self.word.is_word(word):
                not_word.append(space[i+1])
        for key in not_word:
            space.remove(key)

        while True:
            try:
                start_index = randrange(len(space))
                start = space[start_index] + 1
                end = space[start_index + number_of_words]
                break
            except IndexError:
                pass

        return self.raw[start:end]

    @staticmethod
    def punctuation_rules(match_obj):
        """
        Fix broken punctuations in OANC results. Used in re.sub

        :param match_obj: match_obj as returned by re.sub.
        match_obj.group() is space followed by punctuation +/- followed by after-character
        :return str: correct punctuation
        """
        punctuation = match_obj.group()

        if punctuation[1] in '!.?,:;':
            return punctuation[1:]
        elif punctuation[1] in "'":
            if punctuation[-1] in string.ascii_letters:
                return punctuation[1:]
        elif punctuation[1] in '({[':
            return punctuation[:2]
        elif punctuation[1] in ')}]':
            return punctuation[1:]

        return punctuation


if __name__ == '__main__':
    print(Oanc().clip(4))
