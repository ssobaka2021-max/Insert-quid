import unittest
from triangle import *

class TestTriangle(unittest.TestCase):
    def test_triangle_area_normal(self):
        self.assertEqual(area(10, 5), 25)
        self.assertEqual(area(7, 3), 10.5)
    def test_triangle_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 0), 0)
    def test_triangle_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5, 10)
        with self.assertRaises(ValueError):
            area(5, -10)
    def test_triangle_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(5, 5, 5), 15)
    def test_triangle_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)
    def test_triangle_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)
    


