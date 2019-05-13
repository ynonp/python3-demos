import unittest
from lib.car import Car


class TestCar(unittest.TestCase):
    def setUp(self) -> None:
        self.c1 = Car('blue', 20)
        self.c2 = Car('green', 30)

    def test_faster_then(self):
        self.assertTrue(self.c2.is_faster_than(self.c1))
        self.assertFalse(self.c1.is_faster_than(self.c2))

    def test_colors(self):
        self.assertEqual(self.c1.color, 'blue')

    def test_speed(self):
        self.assertEqual(self.c1.speed, 20)

