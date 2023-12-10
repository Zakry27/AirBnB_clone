#!/usr/bin/python3
from console import HBNBCommand
from unittest.mock import create_autospec
from unittest.mock import patch
from models.engine.file_storage import FileStorage
from io import StringIO
import unittest
import sys
"""
the Unittest Module for console.py
"""


class TestConsole(unittest.TestCase):
    ''' the Unittest for console.py module '''

    def SetUp(self):
        ''' setting mock_stdin and mock_stdout '''
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def test_Console(self, server=None):
        ''' this instantiates Console for HBNBCommand '''
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_Quit(self):
        ''' this tests quit method '''

        cmd = HBNBCommand()
        self.assertRaises(SystemExit, quit)

    def test_docs(self):
        ''' it tests docstrings '''
        self.assertTrue(len(HBNBCommand.__doc__) > 0,
                        "** No docstring Found ** ")
        """Checks for docstring existance"""
    def test_docstrings_in_console(self):
        """Tests docstrings exist in console.py"""
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)

    """Tests command interpreter outputs"""
    def test_emptyline(self):
        """Tests no user input"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            HBNBCommand().onecmd("\n")
            self.assertEqual(fake_output.getvalue(), '')

    def test_create(self):
        """Tests cmd output: create"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            HBNBCommand().onecmd("create SomeClass")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

    def test_show_id(self):
        ''' tests show id '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('show BaseModel')
            self.assertTrue(v.getvalue() == "** instance id missing **\n")

    def test_destroy_empty(self):
        ''' tests destroy method '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('destroy')
            self.assertTrue(v.getvalue() == "** class name missing **\n")

    def test_class_exist(self):
        ''' test class name exist '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('all FakeClass')
            self.assertTrue(v.getvalue() == "** class doesn't exist **\n")

    def test_all(self):
        ''' tests all method '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('all')
            self.assertTrue(len(v.getvalue()) > 0)

    def test_update(self):
        ''' tests update method '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('update BaseModel')
            self.assertTrue(v.getvalue() == "** instance id missing **\n")

    def test_alt_all(self):
        ''' tests [class].all method '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('User.all()')
            self.assertTrue(len(v.getvalue()) > 0)

    def test_count(self):
        ''' tests [class].count method '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('User.count()')
            self.assertTrue(int(v.getvalue()) >= 0)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('User.count()')
            self.assertTrue(int(v.getvalue()) >= 1)

    def test_user(self):
        ''' tests user object with console '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create User')
            user_id = v.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('show User')
            self.assertTrue(v.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('all User')
            self.assertTrue(v.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("update User " + user_id + " name betty")
            HBNBCommand().onecmd("show User " + user_id)
            self.assertFalse("betty" in v.getvalue())
            HBNBCommand().onecmd("destroy User " + user_id)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("show User "+user_id)
            self.assertEqual(v.getvalue(), "** no instance found **\n")


if __name__ == '__main__':
    unittest.main()
