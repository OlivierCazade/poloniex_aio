from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='poloniex_aio',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    url='https://github.com/OlivierCazade/poloniex_aio',
    author='Olivier Cazade',
    author_email='olivier.cazade@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='An async library for Poloniex api',
    long_description=long_description,
    python_requires='>=3.5'
)
