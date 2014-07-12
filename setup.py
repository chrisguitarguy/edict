# -*- coding: utf-8 -*-
"""
Edict is a tool for greating command line application in Python 3.3+
"""

import setuptools

setuptools.setup(
    name='edict',
    version='1.0-alpha',
    author='Christopher Davis',
    author_email='cdavis9999@gmail.com',
    url='https://github.com/chrisguitarguy/edict',
    description='A small abstraction around argparse that uses function annotations',
    py_modules='edict',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License'
    ]
)
