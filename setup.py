from setuptools import setup, find_packages

setup(
    name="pig-dicegame",
    version='1.0.0',
    description='Pig the dice game developed using TTD',
    author='Oscar Karlsson, Hampus Andersson, Stefan Cleasson',
    author_email='oscar.karlsson0024@stud.hkr.se',
    # private link, but good practice.
    url='https://github.com/OsvarK/pig-dicegame',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pig = src.driver:main'
        ],
    },
)
