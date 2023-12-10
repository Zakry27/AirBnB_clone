#!/usr/bin/python3
"""
the unittest for the amenity module
"""
from datetime import datetime
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    the unittesting the amenity class
    """

    def test_name(self):
        amenity1 = Amenity()
        self.assertIsInstance(amenity1.name, str)


    def test_ids(self):
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_instance_types(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(amenity.name, str)

    def test_str_repre(self):
        amenity = Amenity()
        expected = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(amenity.__str__(), expected)


    def test_amenity_to_dict(self):
        amenity = Amenity()
        T_format = "%Y-%m-%dT%H:%M:%S.%f"
        amenity.name = "AMN"
        amenity.number = 16
        self.assertIn("name", amenity.to_dict())
        self.assertIn("number", amenity.to_dict())
        self.assertIn("id", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())
        self.assertIn("__class__", amenity.to_dict())
        self.assertEqual(amenity.to_dict()["created_at"], amenity.created_at.strftime(T_format))
