from nltk.corpus import brown
import json

if __name__ == '__main__':
    with open('grammar_patterns.json', 'w') as f:
        json.dump(list(brown.tagged_sents()), f)
