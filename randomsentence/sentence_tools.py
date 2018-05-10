from mosestokenizer import MosesDetokenizer

try:
    from secrets import choice
except ImportError:
    from random import choice


class SentenceTools:
    def __init__(self):
        self.detokenizer = MosesDetokenizer('en')

    def detokenize(self, tokens):
        """
        Join words/sentence_tokens
        :param list of str tokens:
        :return str:
        >>> SentenceTools().detokenize(['The', 'White', 'Russians', 'and', 'the', 'Ukrainians', 'would', 'say', 'that', 'Stalin', 'and', 'Molotov', 'were', 'far', 'less', 'reliable', 'defenders', 'of', 'Russia', 'than', 'Curzon', 'and', 'Clemenceau', '.'])
        'The White Russians and the Ukrainians would say that Stalin and Molotov were far less reliable defenders of Russia than Curzon and Clemenceau.'
        """
        return self.detokenizer(tokens)

    def detokenize_tagged(self, tagged_tokens):
        """

        :param tagged_tokens:
        :return:
        """
        return self.detokenize([token for token, tag in tagged_tokens])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
