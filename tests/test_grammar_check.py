"""
4.8544 seconds per GrammarCorrector.correct
"""
import pytest
import os

from randomsentence.grammar_check import GrammarCorrector


@pytest.mark.skipif('TRAVIS' in os.environ,
                    reason='languagetool-commandline.jar not on Travis CI')
def test_grammar_tools(path='/Users/patarapolw/PycharmProjects/LanguageTool-4.1/languagetool-commandline.jar'):
    gc = GrammarCorrector(languagetool_commandline_path=path)
    print(gc.correct(sentence='A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'))


@pytest.mark.skip(reason="Author cannot install language_check")
def test_grammar_tools_language_check():
    gc = GrammarCorrector()
    print(gc.correct(sentence='A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'))


if __name__ == '__main__':
    from tests import timeit
    from functools import partial

    # timeit(partial(gc.correct, sentence='A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'))
