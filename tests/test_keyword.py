"""
5.4680 seconds per KeywordParse
0.0934 seconds per KeywordParse.from_keyword_list
0.0892 seconds per KeywordParse.from_initials_list
"""

import pytest
import string
from random import choice

from randomsentence.keyword import KeywordParse
from randomsentence.word import WordTool
from randomsentence.sentence import SentenceTool

word_tool = WordTool()
keyword_parse = KeywordParse()
sentence_tool = SentenceTool()


@pytest.fixture()
def from_keyword_list():
    def func(length=3, strictness=None):
        """

        :param length: number of words in keyword_list
        :param strictness:
        :return:

        from_keyword_list(), length=3, strictness=None, Success 30 of 50, 0.0224 seconds per test
        from_keyword_list(), length=3, strictness=2, Success 997 of 1000, 0.0147 seconds per test
        from_keyword_list(), length=4, strictness=2, Success 998 of 1000, 0.0198 seconds per test
        from_keyword_list(), length=5, strictness=2, Success 996 of 1000, 0.0280 seconds per test
        from_keyword_list(), length=6, strictness=2, Success 997 of 1000, 0.0472 seconds per test
        """
        keyword_list = [word_tool.get_random_word() for _ in range(length)]
        sentence = keyword_parse.from_keyword_list(keyword_list=keyword_list, strictness=strictness)
        if sentence is None:
            return False

        print(sentence_tool.detokenize([word for word, _ in sentence]))
        for word, is_overlap in sentence:
            assert isinstance(word, str)
            assert isinstance(is_overlap, bool)

        return True

    return func


@pytest.mark.repeat
@pytest.mark.parametrize('length, strictness', [[3, 2], [4, 2], [5, 2], [6, 2]])
def test_from_keyword_list(from_keyword_list, length, strictness):
    assert from_keyword_list(length, strictness)


@pytest.fixture()
def from_initials_list():
    """

    :return:
    length=3, Success 50 of 50, 0.0949 seconds per from_initials_list.<locals>.func
    length=4, Success 50 of 50, 0.1373 seconds per from_initials_list.<locals>.func
    length=5, Success 50 of 50, 0.1500 seconds per from_initials_list.<locals>.func
    length=5, Success 50 of 50, 0.1495 seconds per from_initials_list.<locals>.func
    """
    def func(length=3):
        starters = [[c] for c in string.ascii_lowercase]
        starters.remove(['x'])
        starters.append(['ex'])
        initials_list = [choice(starters) for _ in range(length)]

        sentence = keyword_parse.from_initials_list(initials_list)
        if sentence is None:
            return False

        print(sentence_tool.detokenize([word for word, _ in sentence]))
        for word, is_overlap in sentence:
            assert isinstance(word, str)
            assert isinstance(is_overlap, bool)

        return True

    return func


@pytest.mark.repeat
@pytest.mark.parametrize('length', [3, 4, 5, 6])
def test_from_initials_list(from_initials_list, length):
    assert from_initials_list(length)


@pytest.fixture()
def from_initials():
    """

    :return:
    length=6, Success 50 of 50, 0.1671 seconds per from_initials.<locals>.func
    """
    def func(length=3):
        initials = ''.join([choice(string.ascii_letters) for _ in range(length)])
        print(initials)

        sentence = keyword_parse.from_initials(initials)
        if sentence is None:
            return False

        print(sentence_tool.detokenize([word for word, _ in sentence]))
        for word, is_overlap in sentence:
            assert isinstance(word, str)
            assert isinstance(is_overlap, bool)

        return True

    return func


@pytest.mark.repeat
@pytest.mark.parametrize('length', [3, 4, 5, 6])
def test_from_initials(from_initials, length):
    assert from_initials(length)


if __name__ == '__main__':
    from MyUtils.testing.repeat import success_rate
    from functools import partial

    success_rate(partial(from_keyword_list(), 6, 2), rep=1000)
    # pytest.main([__file__])
