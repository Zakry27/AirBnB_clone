#!/usr/bin/python3
"""
the unittest for the Place module
"""

import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """
    the unittest for the review class
    """
    def test_instances_type(self):
        review = Review()
        self.assertIs(Review, type(review))
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_rev_str_repr(self):
        review = Review()
        str_format = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(review.__str__(), str_format)

    def test_rev_save(self):
        review = Review()
        updated_before_save = review.updated_at
        review.save()
        updated_after_save = review.updated_at
        self.assertNotEqual(updated_before_save, updated_after_save)

    def test_rev_to_dict(self):
        review = Review()
        review.text = "Amazing place"
        self.assertIn("text", review.to_dict())
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def test_ids(self):
        review1 = Review()
        review2 = Review()
        self.assertEqual(review1.id, review2.id)
