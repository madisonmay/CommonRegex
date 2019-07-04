from setuptools import setup, find_packages


REQUIREMENTS = [
    'spacy >= 2.1.4'
]

setup(
    name="commonregex",
    packages=['commonregex'],
    version="2.0.0",
    install_requires=REQUIREMENTS,
)

