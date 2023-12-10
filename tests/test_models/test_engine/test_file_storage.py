#!/usr/bin/python3
"""
the unittest for filestorage module
"""
import unittest
from models.engine.file_storage import FileStorage
import models
from models.user import User
from models.base_model import BaseModel
import json
import os
from datetime import datetime
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity


class TestFileStorage(unittest.TestCase):
    """
    testing filestorage class
    """

    def test_instance(self):
        self.assertIs(FileStorage, type(FileStorage()))
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)


    def test_all_in_storage(self):
        self.assertEqual(type(models.storage.all()), dict) 


    def test_FileStorage(self):
        self.assertEqual(type(models.storage), FileStorage)
         
    def test_new(self):
        base = BaseModel()
        user = User()
        models.storage.new(base)
        models.storage.new(user)
        self.assertIn("BaseModel.{}".format(base.id), models.storage.all().keys())
        self.assertIn("User.{}".format(user.id), models.storage.all().keys())

    def test_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_save(self):
        base = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(base)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        save_1 = ""
        with open("file.json", "r") as file:
            save_1 = file.read()
            self.assertIn("BaseModel." + base.id, save_1)
            self.assertIn("User." + user.id, save_1)
            self.assertIn("State." + state.id, save_1)
            self.assertIn("Place." + place.id, save_1)
            self.assertIn("City." + city.id, save_1)
            self.assertIn("Amenity." + amenity.id, save_1)
            self.assertIn("Review." + review.id, save_1)

    def test_reload_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload(self):
        base = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(base)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        ob = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base.id, ob)
        self.assertIn("User." + user.id, ob)
        self.assertIn("State." + state.id, ob)
        self.assertIn("Place." + place.id, ob)
        self.assertIn("City." + city.id, ob)
        self.assertIn("Amenity." + amenity.id, ob)
        self.assertIn("Review." + review.id, ob)

if __name__ == "__main__":
    unittest.main()
