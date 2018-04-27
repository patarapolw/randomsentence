"""
Generate a sentence, randomly or from a list of keywords/initials. This is based on Brown corpus.

>>> from randomsentence import Brown
>>> tagged_sentence = Brown().get_tagged_sent()
>>> tagged_sentence
[('She', 'PPS'), ('saw', 'VBD'), ('it', 'PPO'), ('then', 'RB'), (',', ','), ('the', 'AT'), ('distant', 'JJ'), ('derrick', 'NN'), ('of', 'IN'), ('the', 'AT'), ('wildcat', 'NN'), ('--', '--'), ('a', 'AT'), ('test', 'NN'), ('well', 'RB'), ('in', 'IN'), ('unexplored', 'JJ'), ('country', 'NN'), ('.', '.')]

For Brown corpus, it is tagged based on Part-of-speech. This can easily be turned to a real sentence.

>>> from randomsentence import SentenceTool
>>> sentence_tool = SentenceTool()
>>> sentence_tool.detokenize_tagged(tagged_sentence)
'She saw it then, the distant derrick of the wildcat -- a test well in unexplored country.'
>>> from randomsentence import KeywordParse
>>> parser = KeywordParse()
>>> tagged_sentence = parser.from_keyword_list(['love', 'blind', 'trouble'])
>>> tagged_sentence
[('On', False), ('the', False), ('love', True), ('he', False), ('stopped', False), ('at', False), ('the', False), ('blind', True), ('to', False), ('receive', False), ('his', False), ('trouble', True)]

For KeywordParse, the word is tagged based on whether the keyword overlaps.

>>> sentence_tool.detokenize_tagged(tagged_sentence)
'On the love he stopped at the blind to receive his trouble'
>>> tagged_sentence = parser.from_initials('JKr')
>>> tagged_sentence
[('These', False), ('joints', True), ('may', False), ('be', False), ('knotted', True), ('as', False), ('receives', True)]
>>> sentence_tool.detokenize_tagged(tagged_sentence)
'These joints may be knotted as receives'

Grammar fixing module is also included, in case minor grammar fix is needed. This is based on language-check / languagetool.

>>> from randomsentence import GrammarCorrector
>>> corrector = GrammarCorrector()
>>> corrector.correct('A sentence with a error in the Hitchhiker’s Guide tot he Galaxy')
'A sentence with an error in the Hitchhiker’s Guide to the Galaxy'

Note:
    KeywordParse sometimes fail. It returns None on failure.
"""
import doctest
doctest.testmod()

__doctest_skip__ = ['*']
