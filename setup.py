#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


try:
    with open("version.txt") as file:
        __version__ = file.readline().strip()

    # check that version is correct (vX.X.X or vX.X.X.devXXX), eg v0.8.0.dev0
    assert re.match(r"^v\d\.\d\.\d$|^v\d\.\d\.\d\.dev\d+$", __version__)
except FileNotFoundError:
    # when user installs via pip install git+https://github.com/devopshq/artifactory.git
    # this should be discouraged, publish dev package instead
    __version__ = "0.8.0.alpha0"

# default build status, see: https://pypi.python.org/pypi?%3Aaction=list_classifiers
if "dev" in __version__ or "alpha" in __version__:
    dev_status = "4 - Beta"
else:
    dev_status = "5 - Production/Stable"


setup(
    name="dohq-artifactory",
    version=__version__,
    py_modules=["artifactory"],
    license="MIT License",
    description="A Python interface to Artifactory",
    long_description="See full documentation here: https://devopshq.github.io/artifactory/",
    author="Alexey Burov",
    author_email="aburov@ptsecurity.com",
    classifiers=[
        "Development Status :: {}".format(dev_status),
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Filesystems",
    ],
    url="https://devopshq.github.io/artifactory/",
    download_url="https://github.com/devopshq/artifactory",
    install_requires=[
        "requests",
        "python-dateutil",
        "PyJWT",
    ],
    zip_safe=False,
    package_data={"": ["README.md"]},
    packages=["dohq_artifactory"],
)
