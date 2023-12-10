#!/usr/bin/python3
"""
the unittest for the Place module
"""

import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """
    the unittest for the place class
    """
    def test_instances_type(self):
        place1 = Place()
        self.assertIs(Place, type(place1))
        self.assertIsInstance(place1, BaseModel)
        self.assertIsInstance(place1.id, str)
        self.assertIsInstance(place1.created_at, datetime)
        self.assertIsInstance(place1.updated_at, datetime)
        self.assertIsInstance(place1.name, str)
        self.assertIsInstance(place1.city_id, str)
        self.assertIsInstance(place1.user_id, str)
        self.assertIsInstance(place1.description, str)
        self.assertIsInstance(place1.number_bathrooms, int)
        self.assertIsInstance(place1.number_rooms, int)
        self.assertIsInstance(place1.max_guest, int)
        self.assertIsInstance(place1.price_by_night, int)
        self.assertIsInstance(place1.latitude, float)
        self.assertIsInstance(place1.longitude, float)
        self.assertIsInstance(place1.amenity_ids, list)
 
    def test_place_str_repr(self):
        place = Place()
        str_format = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(place.__str__(), str_format)

    def _place_ids(self):
        place_1 = Place()
        place_2 = Place()
        self.assertNotEqual(place_1.id, place_2.id)

    def test_place_save(self):
        place_3 = Place()
        updated_before_save = place_3.updated_at
        place_3.save()
        updated_after_save = place_3.updated_at
        self.assertNotEqual(updated_before_save, updated_after_save)

    def test_place_to_dict(self):
        place = Place()
        place.price_by_night = 500
        place.max_guest = 2
        place.number_bathrooms = 1

        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("price_by_night", place.to_dict())
        self.assertIn("max_guest", place.to_dict())
        self.assertIn("number_bathrooms", place.to_dict())
        self.assertIn("__class__", place.to_dict())
