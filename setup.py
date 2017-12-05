from setuptools import setup, find_packages


setup(
    name='poloniex_aio',
    version='0.1.0b4',
    url='https://github.com/OlivierCazade/poloniex_aio',
    author='Olivier Cazade',
    author_email='olivier.cazade@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='An async library for Poloniex api',
    python_requires='>=3.5'
)
