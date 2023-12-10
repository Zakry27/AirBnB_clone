#!/usr/bin/python3
import unittest
from models.amenity import Amenity
"""
the Unittest Module for Amenity class
"""


class TestAmenity(unittest.TestCase):
    ''' the Unittest for Amenity class '''

    def test_object_Instantiation(self):
        ''' instantiate class '''
        self.amenity = Amenity()

    def testattr(self):
        ''' the test Class: Amenity attributes '''
        self.amenity = Amenity()
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertFalse(hasattr(self.amenity, "random_attr"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")

    def testsave(self):
        ''' the testing method: save '''
        self.amenity = Amenity()
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def teststr(self):
        ''' the testing __str__ return format of Amenity '''
        self.amenity = Amenity()
        s = "[{}] ({}) {}".format(self.amenity.__class__.__name__,
                                  str(self.amenity.id), self.amenity.__dict__)
        self.assertEqual(print(s), print(self.amenity))

if __name__ == '__main__':
    unittest.main()
