import string
import pytest
from random import randint

from randomsentence.keyword import keywords_to_sentence
from randomsentence.word import Word

word = Word()


@pytest.mark.repeat
def test_keywords_to_sentence(min_length=4, max_length=6):
    """
    The result is sometimes None.

    :param min_length: minimum number of keywords
    :param max_length: maximum number of keywords
    :return:
    """
    keyword_list = [word.random() for _ in range(randint(min_length, max_length))]
    sentence = keywords_to_sentence(keyword_list)

    if sentence is not None:
        assert not sentence[0].islower()
        assert sentence[-1] in string.punctuation
    else:
        print(keyword_list)
        assert sentence is None


if __name__ == '__main__':
    pytest.main(['--count=50', '-m', 'repeat', __file__])
