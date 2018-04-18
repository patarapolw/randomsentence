"""
Randomize a word from google-10000-english.txt, with some utility functions.
"""
import math
import re
import string
try:
    from secrets import choice
except ImportError:
    from random import choice

from randomsentence.dir import database_path

__doctest_skip__ = ['Word.random']


class Word:
    def __init__(self, filename: str=None):
        """
        Read a file of words, one on each line (separated by '\n')
        Default is google-10000-english.txt
        https://github.com/first20hours/google-10000-english

        :param str filename: path to file to be read.
        """
        if filename is None:
            filename = database_path('google-10000-english.txt')

        self.words = []
        with open(filename) as f:
            for line in f:
                self.words.append(line.strip())

    def random(self, min_common=100, max_common=None):
        """
        Randomize a word from file. Uncommon words are ignored.

        :param int min_common: minimum commonness to ignore.
        :param int max_common: maximum commonness to ignore. Ignore some uncommon words.
        :return str: a randomized word, attempting to use secrets.common first if present (Python >= 3.6)

        >>> Word().random()
        bathrooms
        """
        return choice(self.words[min_common:max_common])

    def commonness(self, word):
        """
        Commonness of a word.

        :param str word: a word to check
        :return -1 | 0 | positive int | math.inf: If not word, -1. If not in list: math.inf.
        If in list: the order in the list of commonness, starting from zero.

        >>> Word().commonness('bathrooms')
        7570
        >>> Word().commonness('Bathrooms')
        7570
        >>> Word().commonness('Elysa')
        inf
        >>> Word().commonness('on')
        -1
        """
        if not self.is_word(word):
            return -1

        try:
            return self.words.index(word.lower())
        except ValueError:
            return math.inf

    @staticmethod
    def is_word(word):
        """
        Check if a keyword qualify as a "word". Punctuation removed, the word must be longer than 2 characters.

        :param str word: a word to check
        :return bool: whether is a word

        >>> Word.is_word('bathrooms')
        True
        >>> Word.is_word('adhserfsds')
        True
        >>> Word.is_word('on')
        False
        >>> Word.is_word('roll-on')
        True
        >>> Word.is_word('a.c.')
        False
        """
        word = re.sub('[{}]'.format(string.punctuation), '', word)
        if len(word) < 3:
            return False
        if word.isalpha():
            return True

        return False

    @staticmethod
    def to_keywords(sentence):
        """

        :param sentence:
        :return list: list of keywords

        >>> Word.to_keywords('And then illustrates the new Martin Short talk show.')
        ['and', 'then', 'illustrates', 'the', 'new', 'martin', 'short', 'talk', 'show']
        """
        keywords = sentence.lower().split(' ')
        for i, keyword in enumerate(keywords):
            if keyword[-1] in string.punctuation:
                keywords[i] = keyword[:-1]
            if keyword[0] in string.punctuation:
                keywords[i] = keyword[1:]

        return keywords


if __name__ == '__main__':
    pass
