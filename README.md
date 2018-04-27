# Random Sentence

[![Build Status](https://travis-ci.org/patarapolw/randomsentence.svg?branch=master)](https://travis-ci.org/patarapolw/randomsentence)
[![PyPI version shields.io](https://img.shields.io/pypi/v/randomsentence.svg)](https://pypi.python.org/pypi/randomsentence/)
[![PyPI license](https://img.shields.io/pypi/l/randomsentence.svg)](https://pypi.python.org/pypi/randomsentence/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/randomsentence.svg)](https://pypi.python.org/pypi/randomsentence/)

Generate a sentence, randomly or from a list of keywords/initials. This is based on Brown corpus. 

## Installation

Download the git, and cd, then run
```
python setup.py install
python -m nltk.downloader all
```

## Usage


```pycon
>>> from randomsentence import Brown
>>> tagged_sentence = Brown().get_tagged_sent()
>>> tagged_sentence
[('She', 'PPS'), ('saw', 'VBD'), ('it', 'PPO'), ('then', 'RB'), (',', ','), ('the', 'AT'), ('distant', 'JJ'), ('derrick', 'NN'), ('of', 'IN'), ('the', 'AT'), ('wildcat', 'NN'), ('--', '--'), ('a', 'AT'), ('test', 'NN'), ('well', 'RB'), ('in', 'IN'), ('unexplored', 'JJ'), ('country', 'NN'), ('.', '.')]
```

For Brown corpus, it is tagged based on Part-of-speech. This can easily be turned to a real sentence.

```pycon
>>> from randomsentence import SentenceTool
>>> sentence_tool = SentenceTool()
>>> sentence_tool.detokenize_tagged(tagged_sentence)
'She saw it then, the distant derrick of the wildcat -- a test well in unexplored country.'
>>> from randomsentence import KeywordParse
>>> parser = KeywordParse()
>>> tagged_sentence = parser.from_keyword_list(['love', 'blind', 'trouble'])
>>> tagged_sentence
[('On', False), ('the', False), ('love', True), ('he', False), ('stopped', False), ('at', False), ('the', False), ('blind', True), ('to', False), ('receive', False), ('his', False), ('trouble', True)]
```

For KeywordParse, the word is tagged based on whether the keyword overlaps.

```pycon
>>> sentence_tool.detokenize_tagged(tagged_sentence)
'On the love he stopped at the blind to receive his trouble'
>>> tagged_sentence = parser.from_initials('JKr')
>>> tagged_sentence
[('These', False), ('joints', True), ('may', False), ('be', False), ('knotted', True), ('as', False), ('receives', True)]
>>> sentence_tool.detokenize_tagged(tagged_sentence)
'These joints may be knotted as receives'
```

Grammar fixing module is also included, in case minor grammar fix is needed. This is based on language-check / languagetool.

```pycon
>>> from randomsentence import GrammarCorrector
>>> corrector = GrammarCorrector()
>>> corrector.correct('A sentence with a error in the Hitchhiker’s Guide tot he Galaxy')
'A sentence with an error in the Hitchhiker’s Guide to the Galaxy'
```

## Todo
 
KeywordParse sometimes fail. It returns None on failure. This needs to be minimized.

## Found In

https://memorable-password.herokuapp.com/
