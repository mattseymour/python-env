Python and Django Environment Variables
============

![Downloads this month](https://pypip.in/d/envvars/badge.png)

NOTE: If you are installing from source please download the latest tagged version of the code (... unless you are brave in which case use master).

A simple module which will allow python apps and webapps to read .env files (forman style); storing the key-value in the `os environment variables`.

## Installation:

Install via pip: `pip install envvars` or by download the package. Running `python setup.py`.


## Usage:

Loading environment variables into `os.environ`:

Add the following line to your main python file.

    import envvars

Filepath can be blank if `.env` is in current working directory

    envvars.load() or envvars.load('/path/to/file')

### Django

To load `.env` into django add the following lines of code into the `manage.py` and `wsgi.py` files.

Example .env file:

    DJANGO_SETTINGS_MODULE = settings.dev
    DJANGO_SECRETKEY = somerandomkey

Example manage.py file:

    #!/usr/bin/env python
    import os
    import sys

    import envvars

    if __name__ == "__main__":
        # sets DJANGO_SETTINGS_MODULE='settings.dev'
        envvars.load()

        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv)


Example settings.py file:

    import envvars
    SECRET_KEY = envvars.get('DJANGO_SECRETKEY', default='fall back value')



## Using environment variables:

You can use the set environment variables using either `os.environ` or `envvars.get`. `envvars.get` has the added advantage of converting to python type. Therefore, a key value set of `KEY=True` will be returned as a bool type not string as os.environ would normally do.

Envvars.get can be used within your application by:

    # key=12345
    return_val = envvars.get('key')
    > 1234 # type int
