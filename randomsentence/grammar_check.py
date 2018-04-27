import subprocess
try:
    import language_check
except ImportError:
    pass

__doctest_skip__ = ['GrammarCorrector.correct']


def languagetool_commandline(bad_sentence, executable_path, temp_file='tmp.txt'):
    with open(temp_file, 'w') as f:
        f.write(bad_sentence)

    return subprocess.check_output(['java', '-jar', executable_path,
                                    '-l', 'en-US', '-a', temp_file]).decode()


class GrammarCorrector:
    def __init__(self, languagetool_commandline_path: str=None):
        if languagetool_commandline_path is None:
            self.tool = language_check.LanguageTool('en-US')
        else:
            self.tool = languagetool_commandline_path

    def correct(self, sentence, temp_file='tmp.txt'):
        """

        :param str sentence:
        :param str temp_file:
        :return str: grammatically correct sentence
        >>> GrammarCorrector().correct('A sentence with a error in the Hitchhiker’s Guide tot he Galaxy')
        'A sentence with an error in the Hitchhiker’s Guide to the Galaxy'
        """
        if isinstance(self.tool, str):
            return languagetool_commandline(sentence, self.tool, temp_file)
        else:
            return language_check.correct(sentence, self.tool.check(sentence))
