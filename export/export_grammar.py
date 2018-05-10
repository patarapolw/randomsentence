from nltk.corpus import brown
import sqlite3
import json


def brown2sqlite():
    with sqlite3.connect('SentenceMaker.db') as conn:
        conn.execute('''CREATE TABLE tagged_sents
                        ( id INT PRIMARY KEY NOT NULL,
                          tagged_sentence TEXT NOT NULL);''')
        for i, tagged_sentence in enumerate(brown.tagged_sents()):
            conn.execute('''INSERT INTO tagged_sents (id, tagged_sentence)
                            VALUES (?, ?)''', (i, json.dumps(tagged_sentence)))
            conn.commit()


def brown2txt():
    with open('sentences-tagged.txt', 'w') as f:
        for tagged_sentence in brown.tagged_sents():
            f.write(json.dumps(tagged_sentence))
            f.write('\n')


if __name__ == '__main__':
    brown2txt()
