import unittest
import src.car as car

class TestCar(unittest.TestCase):

    def setUp(self):
        self.c = car.Car('green', 40)

    def test_speed(self):
        self.assertEqual(self.c.speed, 40)

    def test_color(self):
        self.assertEqual(self.c.color, 'green')
