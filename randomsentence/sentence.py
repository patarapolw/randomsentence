"""
Sentence generator module based on random common google words -> OANC sentences -> markovify
"""

import markovify
from time import time
import string
import re
try:
    from secrets import choice
except ImportError:
    from random import choice

from randomsentence.utils import timeout_function
from randomsentence.ngram import Oanc
from randomsentence.word import Word

__doctest_skip__ = ['Sentence.*']


class Sentence:
    def __init__(self, keyword: str=None, query: str=None):
        """
        Generate Markov model from OANC on __init__,
        with random keyword, or as defined in ngram.Oanc
        :param str keyword: a single keyword as defined in ngram.Oanc
        :param str query: querying string as in ngram.Oanc
        """
        self.word = Word()
        self.text_model = self.generate(keyword, query)
        self.raw = ''

    def generate(self, keyword: str=None, query: str=None, timeout=20):
        """
        Generate Markov model from OANC on,
        with random keyword, or as defined in ngram.Oanc
        :param str keyword: a single keyword as defined in ngram.Oanc
        :param str query: querying string as in ngram.Oanc
        :return Markov model:
        """
        if keyword is None:
            keyword = self.word.random()
        while not self.word.is_word(keyword):
            keyword = self.word.random()

        start = time()
        while time() - start < timeout:
            try:
                self.raw = Oanc(keyword, query).raw
                if self.raw:
                    self.text_model = timeout_function(markovify.Text, args=(self.raw, ),
                                                       timeout_duration=3)
                    return self.text_model
            except KeyError:
                pass

            keyword = self.word.random()
            query = None

        raise TimeoutError

    def random(self, sentence_char_length: int=None, timeout=10):
        """
        Generate a random sentence via markovify
        :param int sentence_char_length: number of characters in markovify.model.make_short_sentence
        :param float timeout: limit in seconds to markovify.make_sentence
        :return str: random sentence

        >>> Sentence().random()
        The design of these efforts are aimed at balancing the needs of the data required for the president of the auditors applying them are the keys to ensuring that work done conforms to the organization's main network, ensuring that an adequate supply of wellprepared financial professionals is available to fill key positions.
        """
        def make_sentence():
            global result
            if sentence_char_length == -1:
                result = self.text_model.make_sentence()
            else:
                result = self.text_model.make_short_sentence(sentence_char_length)

            return result

        if sentence_char_length is None:
            sentence_char_length = 140

        start = time()
        while time() - start < timeout:
            result = timeout_function(make_sentence, timeout_duration=timeout)

            if result is not None:
                return result

            self.text_model = self.generate()

        return choice(self.raw.split('\n'))

    def with_rating(self, minimum=1000, count=4, timeout=5, sentence_char_length=None):
        """
        Generate a random sentence, with commonness rating as defined in google-10000-english.txt
        :param int minimum: minimum commonness to be counted in "count"
        :param int count: minimum count of commonness before return
        :param float timeout: timeout to return in seconds
        :param int sentence_char_length: number of characters in markovify.model.make_short_sentence
        :return list: a list of tuple of length 2 of (word_in_sentence, frequency_rating)

        >>> Sentence().with_rating()
        {'rating': [('hannah', inf), ('completed', 1507), ('her', 137), ('degree', 1202), ('the', 0), ('work', 124), ('of', -1), ('the', 0), ('test', 501)], 'sentence': 'Hannah completed her degree the work of the test.'}
        """
        start = time()

        while time()-start < timeout:
            sentence = self.random(sentence_char_length=sentence_char_length)
            words = [re.sub('[{}]'.format(string.punctuation), '', raw.lower()) for raw in sentence.split(' ')]

            rating = [(word, self.word.commonness(word)) for word in words]

            count_min = 0
            for pair in rating:
                if pair[0].isalpha():
                    if pair[1] > minimum or pair[1] == -1:
                        count_min += 1

            if count_min >= count:
                return {
                    'rating': rating,
                    'sentence': sentence
                }

        raise TimeoutError


if __name__ == '__main__':
    s = Sentence(keyword='love')
    while True:
        print(s.random())
