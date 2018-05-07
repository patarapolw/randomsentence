import nltk
import os
import json


def word_list_tagger(filein="eff-long.txt", fileout=None):
    if fileout is None:
        fileout = os.path.splitext(filein)[0] + '-tagged.json'
    with open(filein) as f:
        all_words = f.read().strip().split('\n')
    with open(fileout, 'w') as f:
        json.dump(nltk.pos_tag(all_words), f)


if __name__ == '__main__':
    word_list_tagger()
