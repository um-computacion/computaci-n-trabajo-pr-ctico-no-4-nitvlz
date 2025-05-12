import unittest
from fibonacci import fibonacci_iterative, fibonacci_recursive

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_iterative(self):
        self.assertEqual(fibonacci_iterative(0), 0)
        self.assertEqual(fibonacci_iterative(1), 1)
        self.assertEqual(fibonacci_iterative(5), 5)
        self.assertEqual(fibonacci_iterative(10), 55)

    def test_fibonacci_recursive(self):
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_recursive(5), 5)
        self.assertEqual(fibonacci_recursive(10), 55)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fibonacci_iterative(-5)
        with self.assertRaises(ValueError):
            fibonacci_recursive(-5)

if __name__ == '__main__':
    unittest.main()
