# -*- coding: utf-8 -*-

"""
Tests envvars package
"""
import os
import unittest
import types
import envvars

try:
    import mock
except ImportError:
    import unittest.mock as mock

# pylint: disable=R0904
class TestEnvvars(unittest.TestCase):
    """
        Tests the EnvVars package
    """
    def setUp(self):
        os.environ['STRING'] = 'This is a string'
        os.environ['QUOTED_STRING'] = '"True"'
        os.environ['BOOLEAN'] = 'False'
        os.environ['INT'] = '12345'

    def test_get_string(self):
        """ Test return value is of the correct type <string> """
        self.assertIs(type(envvars.get('string')), str)
        self.assertEqual('This is a string', envvars.get('string'))

    def test_get_quoted_string(self):
        """ Test return value is of the correct type <string> """
        self.assertIs(type(envvars.get('QUOTED_STRING')), str)
        self.assertEqual('True', envvars.get('QUOTED_STRING'))

    def test_get_boolean(self):
        """ Test return value is of the correct type <bool> """
        self.assertIs(type(envvars.get('BOOLEAN')), bool)
        self.assertFalse(envvars.get('BOOLEAN'))

    def test_get_int(self):
        """ Test return value is of the correct type <int> """
        self.assertIs(type(envvars.get('INT')), int)
        self.assertEqual(envvars.get('INT'), 12345)

    def test_get_default_value(self):
        """ Test return value of default value """
        self.assertEqual(
            envvars.get('MISSING_KEY', 'default_value'),
            'default_value'
        )

    def test_get_line_(self):
        """ Test the _get_line_ generator functionlity """
        _file_ = mock.Mock(
            return_value=['key1=value1', 'key2=value2', '# this is a comment',
                          'an invalid line'])
        with mock.patch('envvars.open', _file_, create=True):

            # pylint: disable=W0212
            response = envvars._get_line_('filepath')
            self.assertIs(type(response), types.GeneratorType)
            response = list(response)

            _file_.assert_called_once_with('filepath')
            self.assertEqual(len(response), 2)
            self.assertEqual(
                [('KEY1', 'value1'), ('KEY2', 'value2')],
                response
            )


    @mock.patch('envvars._get_line_', create=True)
    def test_load(self, mock_line):
        """
            Test loading data into os.environ from file content
        """
        _environ = {}
        def _setdetault(key, value):
            """ Set key->value """
            _environ.setdefault(key, value)

        with mock.patch('os.path.exists') as mock_pathexists, \
                    mock.patch('os.environ') as mock_environ:
            mock_line.return_value = [
                ('KEY11', 'value1'),
                ('KEY22', 'value2')
            ]
            mock_pathexists.return_value = True
            mock_environ.setdefault.side_effect = _setdetault

            envvars.load('/file/path')

            mock_pathexists.assert_called_once_with('/file/path')
            self.assertEqual(_environ['KEY11'], 'value1')
            self.assertEqual(_environ['KEY22'], 'value2')
