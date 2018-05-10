"""
17.8224 seconds per Brown
0.0925 seconds per Brown.get_tagged_sent
0.0000 seconds per Brown.initials_to_pos
0.0002 seconds per Brown.word_from_pos_and_initials
"""
from randomsentence.randomsentence import RandomSentence

rand_sents = RandomSentence()


def test_get_tagged_sent():
    tagged_sent = rand_sents.get_tagged_sent()

    print(tagged_sent)
    for word, tag in tagged_sent:
        assert isinstance(word, str)
        assert isinstance(tag, str)


if __name__ == '__main__':
    from tests import timeit
    from functools import partial
    timeit(test_get_tagged_sent)
