import unittest

from randomsentence.ngram import Oanc
from randomsentence.word import Word
from randomsentence.sentence import Sentence


class TestNgram(unittest.TestCase):
    oanc = Oanc()

    def test_ngram(self):
        length = 4
        text = self.oanc.clip(length)
        print([word for word in text.split(' ') if Word.is_word(word)])
        self.assertEqual(len([word for word in text.split(' ') if Word.is_word(word)]), length)


class TestSentence(unittest.TestCase):
    sentence = Sentence()

    def test_random(self):
        self.assertIsInstance(self.sentence.random(), str)

    def test_with_rating(self):
        rated_sentence = self.sentence.with_rating()

        for pair in rated_sentence:
            self.assertEqual(len(pair), 2)


class TestWord(unittest.TestCase):
    word = Word()

    def test_random(self):
        randomized_word = self.word.random()
        self.assertIsInstance(randomized_word, str)
        self.assertNotIn(randomized_word, self.word.words[:100])


if __name__ == '__main__':
    unittest.main()
