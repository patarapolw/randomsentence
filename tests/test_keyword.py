import string
import pytest
from random import randint

from randomsentence.keyword import KeywordParse
from randomsentence.word import Word

word = Word()
keyword_parse = KeywordParse('/Users/patarapolw/PycharmProjects/sentencebuilder/sentencebuilder/'
                             'LanguageTool-4.1/languagetool-commandline.jar')


@pytest.mark.repeat
@pytest.mark.slow
def test_keywords_to_sentence(number_of_keywords=randint(4, 6), timeout=20, strictness=2):
    """
    The result is sometimes None, even with 60 seconds' timeout; although it might not be None in a repeated run.

    :param int number_of_keywords: number of keywords
    :param float timeout: timeout to the function
    :param int | None strictness: Strictness of POS matching
    :return:

    number_of_keywords:
    2 - 49 of 50, 2.9815 seconds per function, strictness=None
    3 - 45 of 50, 6.1684 seconds per test, strictness=None
    4 - 48 of 50, 3.0103 seconds per test, strictness=2
    5 - 47 of 50, 4.9906 seconds per test, strictness=2
    6 - 35 of 50, 7.5317 seconds per test, strictness=2
    6 - 50 of 50, 0.9463 seconds per test, strictness=0
    """
    keyword_list = [word.random() for _ in range(number_of_keywords)]
    sentence = keyword_parse.to_sentence(keyword_list,
                                         timeout=timeout, sentence_char_length=None, strictness=strictness)

    if sentence is not None:
        print(sentence)
        assert not sentence[0].islower()
        assert sentence[-1] in string.punctuation

        return True
    else:
        print(keyword_list)
        assert sentence is None

        return False


if __name__ == '__main__':
    # pytest.main(['--count=50', '-m', 'repeat', __file__])
    from tests import timeit
    from functools import partial

    timeit(partial(test_keywords_to_sentence, number_of_keywords=6, strictness=0),
           validator=lambda x: x, rep=50)
