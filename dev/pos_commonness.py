"""
Initial complete: ["VBD", "NN", "JJ", "NNS", "VBZ", "VBN", "VB", "RB", "VBG", "QL", "NN-HL"]
Major system complete: ["VBD", "NN", "IN", "JJ", "NNS", "VBZ", "VBN", "VB", "RB", "VBG", "QL", "JJT", "NN-HL", "VBN-HL", "JJR", "NN$", "NNS-HL", "VBG-HL", "NNS$", "JJ-HL", "FW-NN", "FW-NNS", "NN-NC", "NN+BEZ"]
"""

from nltk.corpus import brown
import string
import yaml


def startswith(starters_list, words):
    for word in words:
        for starters in starters_list:
            if any([word.startswith(starter) for starter in starters]):
                starters_list.remove(starters)
                break

    return starters_list


def major_system(filename='/Users/patarapolw/PycharmProjects/DictPassword/memorable_password/mnemonic.yaml'):
    with open(filename) as f:
        entry = yaml.load(f)

    for k, v in entry['major_system'].items():
        yield v


def xinitial():
    starters = [[c] for c in string.ascii_lowercase]
    starters.remove(['x'])
    starters.append(['ex'])

    return starters


def main():
    pos_dict = dict()
    for word, tag in brown.tagged_words():
        pos_dict.setdefault(tag, set()).add(word)

    overlap_dict = dict()
    for k, v in pos_dict.items():

        overlap_dict[k] = startswith(xinitial(), v)

    for k, v in sorted(overlap_dict.items(), key=lambda x: len(x[1])):
        if len(v) == 0:
            print('"{}"'.format(k), end=', ')


if __name__ == '__main__':
    print(xinitial())
