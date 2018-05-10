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
    keyword_list = request.forms.get('keywords', '').split(' ')
    if len(keyword_list) == 0:
        return sentence_tools.detokenize_tagged(random_sentence.get_tagged_sent())
    else:
        return render_token(keyword_list)


@randomsentenceapp.post('/randomize_words')
def randomize_words():
    number_of_words = 6
    return ' '.join([word_list.get_random_word() for _ in range(number_of_words)])


@randomsentenceapp.get('/static/js/<filename:path>')
def send_js(filename):
    return static_file(filename, root='./webdemo/static/js')


def render_token(keyword_list):
    tagged_sentence = sentence_maker.from_keyword_list(keyword_list)
    for i, pair in enumerate(tagged_sentence):
        if pair[1]:
            tagged_sentence[i][0] = '<b>{}</b>'.format(pair[0])

    return sentence_tools.detokenize_tagged(tagged_sentence)
