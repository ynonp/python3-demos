import unittest

class TestSomething(unittest.TestCase):
    def test_something(self):
        # self.assertEqual()
        # self.assertTrue()
        x = 10
        y = 20
        self.assertEqual(40, x + y)
