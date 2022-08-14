.env files for Python
============
[![Build Status](https://travis-ci.org/mattseymour/python-dotenv.svg?branch=travis-ci-build)](https://travis-ci.org/mattseymour/python-dotenv)
![Downloads this month](https://pypip.in/d/python-dotenv/badge.png)

A `.env` file is a text file holding values which will be added into the applications environment variables. The file uses the following format; a single key=value pair on each line.


## Installation:

Install via pip: `pip install python-env` or by download the package. Running `python setup.py`.


## Usage:

Loading environment variables into `os.environ`:

Add the following line to your main python file.

    import dotenv

Filepath can be blank if `.env` is in current working directory

    dotenv.load() or dotenv.load('/path/to/file')

### Usage with Django

To load `.env` into django add the following lines of code into the `manage.py` and `wsgi.py` files.

Example .env file:

    DJANGO_SETTINGS_MODULE = settings.dev
    DJANGO_SECRETKEY = somerandomkey

Example manage.py file:

    #!/usr/bin/env python
    import os
    import sys

    import dotenv

    if __name__ == "__main__":
        # sets DJANGO_SETTINGS_MODULE='settings.dev'
        dotenv.load()

        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv)


Example settings.py file:

    import dotenv
    SECRET_KEY = dotenv.get('DJANGO_SECRETKEY', default='fall back value')



## Using environment variables:

You can use the set environment variables using either `os.environ` or `dotenv.get`. `dotenv.get` has the added advantage of converting to python type. Therefore, a key value set of `KEY=True` will be returned as a bool type not string as os.environ would normally do.

dotenv.get can be used within your application by:

    # key=12345
    return_val = dotenv.get('key')
    > 1234 # type int
