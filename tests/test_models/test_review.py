#!/usr/bin/python3
import unittest
from models.review import Review
"""
the Unittest Module for Review class
"""


class TestUser(unittest.TestCase):
    ''' the Unittest for Review class '''

    def test_object_Instantiation(self):
        ''' the instantiates class '''
        self.review = Review()

    def testattr(self):
        ''' the test Class: Review attributes '''
        self.review = Review()
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertFalse(hasattr(self.review, "random_attr"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertEqual(self.review.text, "")
        self.assertEqual(self.review.__class__.__name__, "Review")

    def testsave(self):
        ''' the testing method: save '''
        self.review = Review()
        self.review.save()
        self.assertTrue(hasattr(self.review, "updated_at"))

    def teststr(self):
        ''' the testing __str__ return format of BaseModel '''
        self.review = Review()
        s = "[{}] ({}) {}".format(self.review.__class__.__name__,
                                  str(self.review.id), self.review.__dict__)
        self.assertEqual(print(s), print(self.review))

if __name__ == '__main__':
    unittest.main()
