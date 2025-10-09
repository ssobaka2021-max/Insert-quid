import unittest
import math
from circle import *

class CircleTestCase(unittest.TestCase):
    def test_circle_area_normal(self):
        self.assertAlmostEqual(area(5), math.pi * 25)
        self.assertAlmostEqual(area(2.5), math.pi * 6.25)

    def test_circle_area_zero(self):
        self.assertEqual(area(0),0)

    def test_circle_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_circle_perimeter_normal(self):
        self.assertAlmostEqual(perimeter(10), 2 * math.pi * 10)
        self.assertAlmostEqual(perimeter(4.5), 2 * math.pi * 4.5)

    def test_circle_perimeter_zero(self):
        self.assertEqual(perimeter(0),0)

    def test_circle_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-5)


