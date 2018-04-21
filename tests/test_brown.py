"""
15.8908 seconds per Brown
0.0925 seconds per Brown.get_tagged_sent
0.0000 seconds per Brown.initials_to_pos
0.0002 seconds per Brown.word_from_pos_and_initials
"""
import yaml

from randomsentence.brown import Brown
from randomsentence.dir import database_path

brown = Brown()


def test_get_tagged_sent():
    tagged_sent = brown.get_tagged_sent()

    for word, tag in tagged_sent:
        assert isinstance(word, str)
        assert isinstance(tag, str)


def test_word_from_pos_and_initials():
    with open(database_path('settings.yaml')) as f:
        starter_dict = yaml.safe_load(f)['startswith']['brown']

    for k, v in starter_dict.items():
        print(k)
        for pos in v['pos']:
            for initials in v['allowed']:
                print(pos, initials)
                word = brown.word_from_pos_and_initials(pos=pos, initials=initials)
                print(word)
                assert isinstance(word, str)


if __name__ == '__main__':
    from tests import timeit
    from functools import partial
    timeit(Brown)
