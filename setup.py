try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Generate GUI from INI',
    'author': 'Chris Maue',
    'author_email': 'csmaue@gmail.com',
    'url': 'https://github.com/csm0042/guibyini.git',
    'download_url': 'https://github.com/csm0042/guibyini.git',
    'version': '1.0.0',
    'packages': ['guibyini'],
    'name': 'guibyini'
}
setup(**config)