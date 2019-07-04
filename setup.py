from setuptools import setup, find_packages


REQUIREMENTS = [
    'spacy >= 2.1.4'
]

setup(
    name="commonregex",
    packages=find_packages(),
    version="2.0.0",
    install_requires=REQUIREMENTS,
)

