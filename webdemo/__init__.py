from bottle import Bottle, TEMPLATE_PATH, template, request, static_file
from diceware_utils.wordlist import Wordlist

from randomsentence.sentence_maker import SentenceMaker
# from randomsentence.randomsentence import RandomSentence
from randomsentence.sentence_tools import SentenceTools

sentence_maker = SentenceMaker()
# random_sentence = RandomSentence()
random_sentence = sentence_maker.random_sentences
sentence_tools = SentenceTools()
word_list = Wordlist()

TEMPLATE_PATH.append('./webdemo/templates/')
randomsentenceapp = Bottle()


@randomsentenceapp.route('/')
def index():
    return template('index.html')


@randomsentenceapp.post('/generate')
def generate():
    keywords = request.forms.get('keywords', '')
    if keywords == '':
        return sentence_tools.detokenize_tagged(random_sentence.get_tagged_sent())
    else:
        return render_token(keywords.split(' '))


@randomsentenceapp.post('/randomize_words')
def randomize_words():
    number_of_words = 6
    return ' '.join([word_list.get_random_word() for _ in range(number_of_words)])


@randomsentenceapp.get('/static/js/<filename>')
def js(filename):
    return static_file(filename, root='webdemo/static/js')


def render_token(keyword_list):
    tagged_sentence = sentence_maker.from_keyword_list(keyword_list)
    sentence_tokens = []
    for word, match in tagged_sentence:
        if match:
            sentence_tokens.append('<b>{}</b>'.format(word))
        else:
            sentence_tokens.append(word)

    return sentence_tools.detokenize(sentence_tokens)
