import pytest

from randomsentence.ngram import Oanc

oanc = Oanc()


@pytest.mark.parametrize('keyword', ['ancc'])
def test_init_no_result(keyword):
    assert Oanc(keyword).raw == ''


@pytest.mark.parametrize('keyword', ['love'])
def test_init_has_result(keyword):
    assert len(Oanc(keyword).raw) > 1


if __name__ == '__main__':
    pass
