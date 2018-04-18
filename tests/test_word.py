import pytest

from randomsentence.word import Word

word = Word()


@pytest.mark.repeat
def test_random():
    randomized_word = word.random()
    print(randomized_word)

    assert isinstance(randomized_word, str)
    assert randomized_word not in word.words[:100]


if __name__ == '__main__':
    pytest.main(['--count=50', '-m', 'repeat', __file__])
