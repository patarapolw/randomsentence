import pytest
from diceware_utils.wordlist import Wordlist

from randomsentence.sentence_maker import SentenceMaker
from randomsentence.sentence_tools import SentenceTools

word_list = Wordlist()
sentence_maker = SentenceMaker()
sentence_tools = SentenceTools()


@pytest.fixture()
def from_keyword_list():
    def func(length=3, strictness=None):
        """

        :param length: number of words in keyword_list
        :param strictness:
        :return:
        """
        keyword_list = [word_list.get_random_word() for _ in range(length)]
        sentence = sentence_maker.from_keyword_list(keyword_list=keyword_list, strictness=strictness)
        if sentence is None:
            return False

        print(sentence_tools.detokenize([word for word, _ in sentence]))
        for word, is_overlap in sentence:
            assert isinstance(word, str)
            assert isinstance(is_overlap, bool)

        return True

    return func


@pytest.mark.repeat
@pytest.mark.parametrize('length, strictness', [[3, 2], [4, 2], [5, 2], [6, 2]])
def test_from_keyword_list(from_keyword_list, length, strictness):
    assert from_keyword_list(length, strictness)


if __name__ == '__main__':
    from MyUtils.testing.repeat import success_rate
    from functools import partial

    success_rate(partial(from_keyword_list(), 6, 2), rep=1000)
    # pytest.main([__file__])
