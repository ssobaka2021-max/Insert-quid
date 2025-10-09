import unittest
from square import *
class TestSquare(unittest.TestCase):
    def test_square_area_normal(self):
        self.assertEqual(area(5),25)
        self.assertEqual(area(10), 100)
        self.assertEqual(area(2.5), 6.25)
    def test_square_area_zero(self):
        self.assertEqual(area(0), 0)
    def test_square_area_negative(self):
       with self.assertRaises(ValueError):
           area(-5)
    def test_square_perimeter_normal(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(10), 40)
        self.assertEqual(perimeter(2.5), 10)
    def test_square_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
    def test_square_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-3)
