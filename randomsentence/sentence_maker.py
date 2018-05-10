import nltk
from time import time
try:
    from secrets import choice
except ImportError:
    from random import choice

from randomsentence.randomsentence import RandomSentence

__doctest_skip__ = ['SentenceMaker.from_keyword_list']


class SentenceMaker:
    def __init__(self):
        self.random_sentences = RandomSentence(do_markovify=False)

    def from_keyword_list(self, keyword_list, strictness=2, timeout=3):
        """
        Convert a list of keywords to sentence. The result is sometimes None

        :param list keyword_list: a list of string
        :param int | None strictness: None for highest strictness. 2 or 1 for a less strict POS matching
        :param float timeout: timeout of this function
        :return list of tuple: sentence generated

        >>> SentenceMaker().from_keyword_list(['Love', 'blind', 'trouble'])
        [('For', False), ('love', True), ('to', False), ('such', False), ('blind', True), ('we', False), ('must', False), ('turn', False), ('to', False), ('the', False), ('trouble', True)]
        """
        keyword_tags = nltk.pos_tag(keyword_list)

        start = time()
        while time() - start < timeout:
            index = 0
            output_list = []
            tagged_sent = self.random_sentences.get_tagged_sent()
            for word, tag in tagged_sent:
                if index >= len(keyword_tags):
                    return self.get_overlap(keyword_list, output_list, is_word_list=True)

                if self.match_pos(tag, keyword_tags[index][1], strictness=strictness):
                    output_list.append(keyword_tags[index][0])
                    index += 1
                else:
                    output_list.append(word)

        return []

    @staticmethod
    def match_pos(pos1, pos2, strictness=2):
        """
        Match part-of-speech as defined in https://catalog.ldc.upenn.edu/docs/LDC99T42/tagguid1.pdf
        :param pos1:
        :param pos2:
        :param int | None strictness: None is the strictest
        :return bool:

        >>> SentenceMaker.match_pos('NN', 'PRP', 0)
        True
        """
        return pos1[:strictness] == pos2[:strictness]

    @staticmethod
    def get_overlap(initials_list_or_word_list, tokens, is_word_list=True):
        """

        :param list of str | list of lists initials_list_or_word_list:
        :param list of str tokens:
        :param bool is_word_list: If False, initials_list
        :return list of tuple:

        """
        index = 0
        result = []
        for token in tokens:
            if index >= len(initials_list_or_word_list):
                break
            if ((is_word_list and token.lower() == initials_list_or_word_list[index].lower()) or
                    (not is_word_list and
                     any([token.startswith(initial) for initial in initials_list_or_word_list[index]]))):
                result.append((token, True))
                index += 1
            else:
                result.append((token, False))

        if index != len(initials_list_or_word_list):
            raise ValueError('Does not overlap')
        else:
            return result


if __name__ == '__main__':
    print(SentenceMaker().from_keyword_list(['Love', 'blind', 'trouble']))
