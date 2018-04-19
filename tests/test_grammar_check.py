"""
4.8544 seconds per GrammarCorrector.correct
"""
from randomsentence.grammar_check import GrammarCorrector

gc = GrammarCorrector(languagetool_commandline_path='/Users/patarapolw/PycharmProjects/sentencebuilder/sentencebuilder/LanguageTool-4.1/languagetool-commandline.jar')

if __name__ == '__main__':
    from tests import timeit
    from functools import partial

    timeit(partial(gc.correct, sentence='A sentence with a error in the Hitchhiker’s Guide tot he Galaxy'))
