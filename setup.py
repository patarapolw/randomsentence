from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['nltk', 'markovify', 'mosestokenizer']
pytest_requires = ['xdist', 'repeat', 'timeout', 'doctestplus']
tests_require = ['pytest'] + ['pytest-{}'.format(req) for req in pytest_requires]

setup(
    name='randomsentence',  # Required
    version='0.3.1',  # Required
    description='Generate a sentence, randomly or from a list of keywords/initials. '
                'This is based on Brown corpus.',  # Required
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/patarapolw/randomsentence',  # Optional
    author='Pacharapol Withayasakpunt',  # Optional
    author_email='patarapolw@gmail.com',  # Optional
    keywords='random sentence random_sentence random_word',  # Optional
    packages=["randomsentence"],  # Required
    install_requires=install_requires,  # Optional
    python_requires='>=3.5',
    license='MIT',
    classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Utilities'
    ],
    tests_require=tests_require,
    extras_require={  # Optional
        'test': tests_require,
        'with-language-check': ['language-check']
    }
)
