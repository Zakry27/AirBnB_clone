#!/usr/bin/python3
import unittest
from models.state import State
"""
the Unittest Module for State class
"""


class TestUser(unittest.TestCase):
    ''' the Unittest for State class '''

    def test_object_Instantiation(self):
        ''' the instantiates class '''
        self.state = State()

    def testattr(self):
        ''' the test Class: State attributes '''
        self.state = State()
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertFalse(hasattr(self.state, "random_attr"))
        self.assertTrue(hasattr(self.state, "name"))
        self.assertTrue(hasattr(self.state, "id"))
        self.assertEqual(self.state.name, "")
        self.state.name = "WonderLand"
        self.assertEqual(self.state.name, "WonderLand")
        self.assertEqual(self.state.__class__.__name__, "State")

    def testsave(self):
        ''' the testing method: save '''
        self.state = State()
        self.state.save()
        self.assertTrue(hasattr(self.state, "updated_at"))

    def teststr(self):
        ''' the testing __str__ return format of BaseModel '''
        self.state = State()
        s = "[{}] ({}) {}".format(self.state.__class__.__name__,
                                  str(self.state.id), self.state.__dict__)
        self.assertEqual(print(s), print(self.state))

if __name__ == '__main__':
    unittest.main()
