# История хэшов коммитов #
<_7t45abd_> - Unit test for circle.py
    __Код для тестирования круга__
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



<_23sa7hx_> - Unit test for rectangle.py
    __Код для тестирования прямоугольника__
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
<_54hrsaa_> - Unit test for square.py
    __Код для тестирования квадрата__
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

< _12mbcsa_> - Unit test for triangle.py
    __Код для тестирования треугольника__
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
    


