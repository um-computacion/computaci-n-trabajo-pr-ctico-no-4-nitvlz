import unittest
from factorial import factorial_iterative, factorial_recursive

class TestFactorial(unittest.TestCase):

    def test_factorial_iterative(self):
        self.assertEqual(factorial_iterative(0), 1)
        self.assertEqual(factorial_iterative(5), 120)

    def test_factorial_recursive(self):
        self.assertEqual(factorial_recursive(0), 1)
        self.assertEqual(factorial_recursive(5), 120)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            factorial_iterative(-1)
        with self.assertRaises(ValueError):
            factorial_recursive(-1)

if __name__ == '__main__':
    unittest.main()
