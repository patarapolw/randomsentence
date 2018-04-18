from textblob import TextBlob
from time import time
try:
    import language_check
except ImportError:
    from randomsentence.languagetool import languagetool_commandline

from randomsentence.ngram import Oanc
from randomsentence.sentence import Sentence

__doctest_skip__ = ['KeywordParse.to_sentence']


class KeywordParse:
    def __init__(self, languagetool: str=None):
        if languagetool is None:
            self.tool = language_check.LanguageTool('en-US')
        else:
            self.tool = languagetool

    def to_sentence(self, keyword_list,
                    sentence_char_length=140, strictness=2, timeout=20):
        """
        Convert a list of keywords to sentence. The result is sometimes

        :param list keyword_list: a list of string
        :param int | None sentence_char_length:
        :param int | None strictness: None for highest strictness. 2 or 1 for a less strict POS matching
        :param float timeout: timeout of this function
        :return str: sentence generated

        >>> KeywordParse().to_sentence(['love', 'blind', 'trouble'])
        I am out to my ex-wife love and not doing any blind but might be some trouble.

        TODO: Eliminate return None
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
                    output = output[0].upper() + output[1:] + '.'
                    if isinstance(self.tool, str):
                        return languagetool_commandline(output, self.tool)
                    else:
                        return language_check.correct(output, self.tool.check(output))

                if self.match_pos(tag, keyword_tags[index][1], strictness=strictness):
                    output_list.append(keyword_tags[index][0])
                    index += 1
                else:
                    output_list.append(word)

        return None

    @staticmethod
    def match_pos(pos1, pos2, strictness=2):
        """
        Match part-of-speech as defined in https://catalog.ldc.upenn.edu/docs/LDC99T42/tagguid1.pdf
        :param pos1:
        :param pos2:
        :param int | None strictness:
        :return bool:

        >>> KeywordParse.match_pos('NN', 'PRP', 0)
        True
        """
        pools = [
            ['N', 'P']  # noun
        ]

        if strictness == 0:
            for pool in pools:
                if pos1 in pool and pos2 in pool:
                    return True

        return pos1[:strictness] == pos2[:strictness]


if __name__ == '__main__':
    pass
