from textblob import TextBlob
from time import time

from randomsentence.ngram import Oanc
from randomsentence.sentence import Sentence

__doctest_skip__ = ['keywords_to_sentence']


def keywords_to_sentence(keyword_list, sentence_char_length=140, strictness=None, timeout=20):
    """
    Convert a list of keywords to sentence. The result is sometimes

    :param list keyword_list: a list of string
    :param int sentence_char_length:
    :param int strictness: None for highest strictness. 2 or 1 for a less strict POS matching
    :param int timeout: timeout of this function
    :return str: sentence generated

    >>> keywords_to_sentence(['love', 'blind', 'trouble'])
    I am out to my ex-wife love and not doing any blind but might be some trouble.
    """
    keyword_tags = TextBlob(' '.join(keyword_list)).tags

    start = time()
    while time() - start < timeout:
        index = 0
        output_list = []
        sentence = Sentence().random(sentence_char_length=sentence_char_length)
        for word, tag in TextBlob(sentence).tags:
            if index >= len(keyword_tags):
                output = Oanc.punctuate(' '.join(output_list))
                return output[0].upper() + output[1:] + '.'

            if tag[:strictness] == keyword_tags[index][1][:strictness]:
                output_list.append(keyword_tags[index][0])
                index += 1
            else:
                output_list.append(word)

    return None


if __name__ == '__main__':
    print(keywords_to_sentence(['love', 'blind', 'trouble']))