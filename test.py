#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test runner
"""
from unittest import (defaultTestLoader, TestSuite, TextTestRunner)

if __name__ == '__main__':
    test_suite = TestSuite()

    for _suite in defaultTestLoader.discover('tests', pattern='test_*.py'):
        for test in _suite:
            test_suite.addTests(test)
    TextTestRunner().run(test_suite)
