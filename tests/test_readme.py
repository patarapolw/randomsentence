"""
>>> from randomsentence.sentence_maker import SentenceMaker
>>> sentence_maker = SentenceMaker()
>>> tagged_sentence = sentence_maker.from_keyword_list(['balmy', 'tricycle', 'jingle', 'overpass'])
>>> tagged_sentence
[('Tommy', False), (',', False), ('of', False), ('balmy', True), (',', False), ('had', False), ('never', False), ('heard', False), ('of', False), ('a', False), ('kotowaza', False), (',', False), ('or', False), ('Japanese', False), ('tricycle', True), (',', False), ('which', False), ('says', False), (',', False), ('``', False), ('Tanin', False), ('yori', False), ('miuchi', False), ("''", False), (',', False), ('and', False), ('is', False), ('literally', False), ('translated', False), ('as', False), ('``', False), ('jingle', True), ('are', False), ('better', False), ('than', False), ('overpass', True)]

>>> from randomsentence.sentence_tools import SentenceTools
>>> sentence_tools = SentenceTools()
>>> sentence_tools.detokenize_tagged(tagged_sentence)
"Tommy, of balmy, had never heard of a kotowaza, or Japanese tricycle, which says, ``Tanin yori miuchi '', and is literally translated as`` jingle are better than overpass"

>>> from randomsentence.randomsentence import RandomSentence
>>> random_sentence = RandomSentence(do_markovify=True)
>>> tagged_sentence = random_sentence.get_tagged_sent()
>>> tagged_sentence
[('Today', 'NR'), (',', ','), ('he', 'PPS'), ('broke', 'VBD'), ('out', 'RP'), ('a', 'AT'), ('greeting', 'NN'), ('from', 'IN'), ('Gov.', 'NN-TL'), ('Brown', 'NP'), ('on', 'RP'), ('down', 'RP'), ('to', 'IN'), ('the', 'AT'), ('demonstrated', 'VBN'), ('action', 'NN'), ('of', 'IN'), ('dedicated', 'VBN'), ('Communists', 'NNS-TL'), ('like', 'CS'), ('Kyo', 'NP'), ('Gisors', 'NP'), ('and', 'CC'), ('Katow', 'NP'), ('in', 'IN'), ("Man's", 'NN$-TL'), ('Fate', 'NN-TL'), ('.', '.')]
>>> sentence_tools.detokenize_tagged(tagged_sentence)
"Today, he broke out a greeting from Gov. Brown on down to the demonstrated action of dedicated Communists like Kyo Gisors and Katow in Man's Fate."
"""

__doctest_skip__ = ['*']


if __name__ == '__main__':
    import doctest
    doctest.testmod()
