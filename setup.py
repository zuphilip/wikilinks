from setuptools import setup

setup(
    version = '0.0.1',
    name = 'wikilinks',
    url = 'http://github.com/edsu/wikilinks',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    license = 'http://www.opensource.org/licenses/mit-license.php',
    py_modules = ['wikilinks'],
    install_requires = ['six'],
    test_requirements= ['pytest'],
    description = 'Get a list of Wikipedia articles that link to a website.',
    test_suite = 'test',
)
