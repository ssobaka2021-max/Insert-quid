import unittest
from rectangle import *

class TestRectangle(unittest.TestCase):

    def test_rectangle_area_normal(self):
        self.assertEqual(area(10, 5), 50)
        self.assertEqual(area(7, 3), 21)
        self.assertEqual(area(2.5, 4), 10.0)

    def test_rectangle_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_rectangle_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5, 10)
        with self.assertRaises(ValueError):
            area(5, -10)

    def test_rectangle_perimeter_normal(self):
        self.assertEqual(perimeter(10, 5), 30)
        self.assertEqual(perimeter(3, 7), 20)
        self.assertEqual(perimeter(2.5, 4), 13.0)

    def test_rectangle_perimeter_zero(self):
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(10, 0), 20)
        self.assertEqual(perimeter(0, 0), 0)

    def test_rectangle_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 10)
        with self.assertRaises(ValueError):
            perimeter(5, -10)

    def test_rectangle_perimeter_square(self):
        self.assertEqual(perimeter(5, 5), 20)