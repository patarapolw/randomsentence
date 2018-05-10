import nltk
import sqlite3

from diceware_utils.wordlist import Wordlist


def word_list_tagger2sqlite(in_list: list=None, fileout='SentenceMaker.db'):
    if in_list is None:
        in_list = [Wordlist('eff-long').wordlist,
                   [word.lower() for word in Wordlist('aspell-en').wordlist]]
    all_words = set(sum(in_list, []))

    with sqlite3.connect(fileout) as conn:
        conn.execute('''CREATE TABLE dictionary
                                ( id INT PRIMARY KEY NOT NULL,
                                  word TEXT NOT NULL,
                                  pos T EXT NOT NULL);''')
        for i, pair in enumerate(nltk.pos_tag(sorted(all_words))):
            word, pos = pair
            conn.execute('''INSERT INTO dictionary (id, word, pos)
                            VALUES (?, ?, ?)''', (i, word, pos))
        conn.commit()


def word_list_tagger2txt(in_list: list=None, fileout='dictionary-tagged.txt'):
    if in_list is None:
        in_list = [Wordlist('eff-long').wordlist,
                   [word.lower() for word in Wordlist('aspell-en').wordlist]]
    all_words = set(sum(in_list, []))

    with open(fileout, 'w') as f:
        for word, pos in nltk.pos_tag(sorted(all_words)):
            f.write(word)
            f.write('\t')
            f.write(pos)
            f.write('\n')


if __name__ == '__main__':
    word_list_tagger2txt()
