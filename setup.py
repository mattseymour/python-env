#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup envvars
"""

import envvars

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='envvars',
    version=envvars.__version__,
    description='Get and Set environment variables using .env file',
    author='Matt Seymour',
    author_email='matt@mattseymour.net',
    url="http://github.com/mattseymour/python-envvars",
    packages=['envvars'],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests'
)
