"""
Web-scraping OANC's http://www.anc.org/cgi-bin/ngrams.cgi
"""

import requests
from bs4 import BeautifulSoup
import string
import re

from randomsentence.word import Word

__doctest_skip__ = ['Oanc.__init__']


class Oanc:
    def __init__(self, keyword: str=None, query: str=None):
        """
        Web-scraping OANC's http://www.anc.org/data/oanc/ngram/

        :param str keyword: a keyword.
        If not specified, a word (beyond commonness of 100) is randomized from google-10000-english.txt
        :param str query: querying language as defined in OANC's http://www.anc.org/cgi-bin/ngrams.cgi
        If not specified, keyword is used instead.
        If specified, keyword is ignored.

        >>> Oanc(keyword='adns').raw
        \n
        >>> Oanc(keyword='love').raw
        Sentences containing the word 'love'
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

        self.raw = self.punctuate(BeautifulSoup(r.text, 'html.parser').find('pre').text).strip()

    @staticmethod
    def punctuate(sentence):
        """
        Correct punctuation for 'Lexical token' output style:
        'http://www.anc.org/data/oanc/ngram/'
        :param str sentence: badly punctuated sentence
        :return str: well punctuated sentence

        >>> Oanc.punctuate('Readers would write her with their questions on life , love , and ( usually ) microeconomics , and she would give them really great advice , e . g . , " Wake up and smell the coffee , honey ! " ')
        'Readers would write her with their questions on life, love, and (usually) microeconomics, and she would give them really great advice, e. g. , " Wake up and smell the coffee, honey! " '
        """
        def rules(match_obj):
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

        return re.sub('( [{}].?)'.format(string.punctuation), rules, sentence)


if __name__ == '__main__':
    pass
