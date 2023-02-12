#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

setup(
    name='pyChatGPT-intl',
    version="0.0.4",
    description='This Python3 module acts as a wrapper for ChatGPT API and will help you to use ChatGPT in your own '
                'language.',
    long_description='This Python3 module acts as a wrapper for ChatGPT API and will help you to use ChatGPT in your '
                     'own language.',
    readme="README.md",
    long_description_content_type='text/markdown',
    url='https://github.com/asirihewage/pyChatGPT-intl',
    author='Asiri Hewage',
    author_email='foolmashi@gmail.com',
    license='GNU General Public License v3 (GPLv3)',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'pychatgptintl = pychatgptintl.__main__:main',
        ],
    },
    install_requires=[
        "tls_client",
        "rich"
    ],
)
