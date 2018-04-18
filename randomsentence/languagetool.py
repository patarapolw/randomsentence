import subprocess


def languagetool_commandline(bad_sentence, executable_path, temp_file='tmp.txt'):
    with open(temp_file, 'w') as f:
        f.write(bad_sentence)

    return subprocess.check_output(['java', '-jar', executable_path,
                                    '-l', 'en-US', '-a', temp_file]).decode()
