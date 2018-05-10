from nltk.corpus import brown
import markovify
try:
    from secrets import choice
except ImportError:
    from random import choice

__doctest_skip__ = ['RandomSentence.get_tagged_sent']


class RandomSentence:
    def __init__(self, do_markovify=True):
        """

        :param do_markovify:
        """
        self.tagged_sents = list(brown.tagged_sents())
        if do_markovify:
            self.model = markovify.Chain(self.tagged_sents, 2)

    def get_tagged_sent(self):
        """

        :return list of tuples of non-space-separated strings:
        >>> random_sentence = RandomSentence()
        >>> random_sentence.get_tagged_sent()
        [('As', 'CS'), ('she', 'PPS'), ('was', 'BEDZ'), ('rather', 'QL'), ('tired', 'VBN'), ('this', 'DT'), ('evening', 'NN'), (',', ','), ('her', 'PP$'), ('simple', 'JJ'), ('``', '``'), ('Thank', 'VB'), ('you', 'PPO'), ('for', 'IN'), ('the', 'AT'), ('use', 'NN'), ('of', 'IN'), ('your', 'PP$'), ('bath', 'NN'), ("''", "''"), ('--', '--'), ('when', 'WRB'), ('she', 'PPS'), ('sat', 'VBD'), ('down', 'RP'), ('opposite', 'IN'), ('him', 'PPO'), ('--', '--'), ('spoken', 'VBN'), ('in', 'IN'), ('a', 'AT'), ('low', 'JJ'), ('voice', 'NN'), (',', ','), ('came', 'VBD'), ('across', 'RB'), ('with', 'IN'), ('coolnesses', 'NNS'), ('of', 'IN'), ('intelligence', 'NN'), ('and', 'CC'), ('control', 'NN'), ('.', '.')]
        """
        try:
            return list(self.model.gen())
        except AttributeError:
            return choice(self.tagged_sents)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
