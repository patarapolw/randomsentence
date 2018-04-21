from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['nltk', 'PyYAML', 'markovify']
pytest_requires = ['xdist', 'repeat', 'timeout', 'doctestplus']
tests_require = ['pytest'] + ['pytest-{}'.format(req) for req in pytest_requires]

setup(
    name='randomsentence',  # Required
    version='0.1.1',  # Required
    description='Generate a sentence, randomly or from a list of keywords/initials. '
                'This is based on Brown corpus.',  # Required
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/patarapolw/randomsentence',  # Optional
    author='Pacharapol Withayasakpunt',  # Optional
    author_email='patarapolw@gmail.com',  # Optional
    # classifiers=[  # Optional
    #     # How mature is this project? Common values are
    #     #   3 - Alpha
    #     #   4 - Beta
    #     #   5 - Production/Stable
    #     'Development Status :: 3 - Alpha',
    #
    #     # Indicate who your project is intended for
    #     'Intended Audience :: Developers',
    #     'Topic :: Software Development :: Build Tools',
    #
    #     # Pick your license as you wish
    #     'License :: OSI Approved :: MIT License',
    #
    #     # Specify the Python versions you support here. In particular, ensure
    #     # that you indicate whether you support Python 2, Python 3 or both.
    #     'Programming Language :: Python :: 2',
    #     'Programming Language :: Python :: 2.7',
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: 3.4',
    #     'Programming Language :: Python :: 3.5',
    #     'Programming Language :: Python :: 3.6',
    # ],
    keywords='random sentence random_sentence random_word',  # Optional
    packages=find_packages(exclude=['tests']),  # Required
    install_requires=install_requires,  # Optional
    python_requires='>=3',
    tests_require=pytest_requires,
    extras_require={  # Optional
        'test': ['tox'] + pytest_requires,
        'with-language-check': ['language-check']
    },
    package_data={  # Optional
        'randomsentence': ['database/*'],
    },
)
