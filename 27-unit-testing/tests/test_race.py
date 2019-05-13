import unittest
import src.car as car
import src.race as race

class TestRace(unittest.TestCase):
    def test_winner(self):
        c1 = car.Car('green', 40)
        c2 = car.Car('blue', 70)
        r  = race.Race([c1, c2])

        self.assertEqual(c2, r.winner())


