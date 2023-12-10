#!/usr/bin/python3
"""
the unittest for the sate module
"""

import unittest
from models.state import State
from datetime import datetime
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """
    the testing of state class
    that inherits from basemodel
    """
    def test_type_of_name(self):
        state = State()
        self.assertEqual(type(state.name), str)


    def test_ids(self):
        test1 = State()
        test2 = State()
        self.assertNotEqual(test1.id, test2.id)


    def test_str_representation(self):
        state = State()
        expected = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(state.__str__(), expected)
    
    def test_state_save(self):
        state = State()
        updated_before_save = state.updated_at
        state.save()
        updated_after_save = state.updated_at
        self.assertNotEqual(updated_before_save, updated_after_save)
    
    def test_place_to_dict(self):
        state = State()
        state.name = "ISNOTREAL"

        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("name", state.to_dict())
        self.assertIn("__class__", state.to_dict())
