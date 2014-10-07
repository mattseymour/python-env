#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test runner
"""
from unittest import (defaultTestLoader, TestSuite, TextTestRunner)
from coverage import coverage


if __name__ == '__main__':
    cov = coverage()
    cov.exclude('test')
    cov.exclude('tests/')
    cov.exclude('mock/*')
    cov.start()

    test_suite = TestSuite()

    for _suite in defaultTestLoader.discover('tests', pattern='test_*.py'):
        for test in _suite:
            test_suite.addTests(test)
    TextTestRunner().run(test_suite)

    cov.stop()
    cov.save()
    cov.report()