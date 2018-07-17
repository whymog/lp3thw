try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Ex47',
    'author': 'Nick Cummings',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email address.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
