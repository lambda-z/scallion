import unittest
from greet_package import greet

class TestGreet(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet('Alice'), 'Hello, Alice!')
        self.assertEqual(greet('Bob'), 'Hello, Bob!')

if __name__ == '__main__':
    unittest.main()