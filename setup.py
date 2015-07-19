

import os

from eveimageserver import __version__
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="eveimageserver",
    version=__version__,
    author="Regner Blok-Andernse",
    author_email="regnerba@gmail.com",
    description=("A collection of utility metods for interacting with the EVE Online image server."),
    license="MIT",
    keywords="eve image server",
    url="https://github.com/Regner/eveimageserver",
    packages=find_packages(),
    long_description=open('README.md').read(),
    install_requires=[line.strip() for line in open('requirements.txt')],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
