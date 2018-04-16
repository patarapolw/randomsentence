"""
Sentence generator module based on random common google words -> OANC sentences -> markovify
"""

import markovify
from time import time

from randomsentence.ngram import Oanc
from randomsentence.word import Word


class Sentence:
    def __init__(self, keyword: str=None, query: str=None):
        """
        Generate Markov model from OANC on __init__,
        with random keyword, or as defined in ngram.Oanc
        :param str keyword: a single keyword as defined in ngram.Oanc
        :param str query: querying string as in ngram.Oanc
        """
        self.word = Word()
        if keyword is None:
            keyword = Word().random()
        self.text_model = markovify.Text(Oanc(keyword, query).raw)

    def random(self):
        """
        Generate a random sentence via markovify
        :return str: random sentence

        # >>> Sentence().random()
        # The design of these efforts are aimed at balancing the needs of the data required for the president of the auditors applying them are the keys to ensuring that work done conforms to the organization's main network, ensuring that an adequate supply of wellprepared financial professionals is available to fill key positions.

        todo: bypassing KeyError: ('___BEGIN__', '___BEGIN__')
        """
        while True:
            result = self.text_model.make_sentence()
            if result is not None:
                break

        return result

    def with_rating(self, minimum=1000, count=4, timeout=5):
        """
        Generate a random sentence, with commonness rating as defined in google-10000-english.txt
        :param int minimum: minimum commonness to be counted in "count"
        :param int count: minimum count of commonness before return
        :param float timeout: timeout to return in seconds
        :return list: a list of tuple of length 2 of (word_in_sentence, frequency_rating)

        # >>> Sentence().with_rating()
        # [('The', inf), ('larger', 1329), ('size', 336), ('of', -1), ('many', 183), ('of', -1), ('these', 92), ('fruits', 7329), ('results', 239), ('in', -1), ('their', 57), ('salt,', inf), ('no', -1), ('sugar', 3382), ('added', 664), ('to', -1), ('their', 57), ('canned', inf), ('fruits,', inf), ('and', 2), ('less', 534), ('tar', 8168), ('in', -1), ('their', 57), ('toppling', inf), ('over', 109), ('and', 2), ('thus', 1372), ('in', -1), ('an', -1), ('inability', inf), ('to', -1), ('properly', 3541), ('disperse', inf), ('the', 0), ('spores.', inf)]
        """
        start = time()

        while time()-start < timeout:
            global result
            words = self.random().split(' ')

            result = [(word, self.word.commonness(word)) for word in words]

            count_min = 0
            for pair in result:
                if pair[0].isalpha():
                    if pair[1] > minimum or pair[1] == -1:
                        count_min += 1

            if count_min >= count:
                return result

        raise TimeoutError


if __name__ == '__main__':
    print(Sentence().with_rating())
