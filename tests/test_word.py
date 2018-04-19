"""
0.0802 seconds per WordTool
0.0000 seconds per WordTool.get_random_word
0.0002 seconds per WordTool.commonness
0.0000 seconds per WordTool.is_word
0.0007 seconds per WordTool.in_dictionary
"""
import pytest

from randomsentence.word import WordTool

word_tool = WordTool()


def test_get_random_word():
    word = word_tool.get_random_word()
    assert isinstance(word, str)


if __name__ == '__main__':
    from tests import timeit
    from functools import partial

    timeit(partial(word_tool.in_dictionary, word='bathrooms'))
