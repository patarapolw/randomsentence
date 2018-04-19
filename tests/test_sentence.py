"""
0.0795 seconds per SentenceTool
0.0019 seconds per SentenceTool.rate
0.0015 seconds per SentenceTool.detokenize
"""
import string

from randomsentence.sentence import SentenceTool

sentence_tool = SentenceTool()


def test_rate(tokens=None):
    if tokens is None:
        tokens = ['The', 'White', 'Russians', 'and', 'the', 'Ukrainians', 'would', 'say', 'that', 'Stalin', 'and', 'Molotov', 'were', 'far', 'less', 'reliable', 'defenders', 'of', 'Russia', 'than', 'Curzon', 'and', 'Clemenceau', '.']
    for token, rating in sentence_tool.rate(tokens):
        assert all([char.islower() for char in token if char in string.ascii_letters])
        assert rating >= 0


if __name__ == '__main__':
    from tests import timeit
    from functools import partial

    timeit(partial(sentence_tool.detokenize, tokens=['The', 'White', 'Russians', 'and', 'the', 'Ukrainians', 'would', 'say', 'that', 'Stalin', 'and', 'Molotov', 'were', 'far', 'less', 'reliable', 'defenders', 'of', 'Russia', 'than', 'Curzon', 'and', 'Clemenceau', '.']))
