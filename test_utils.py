"""Tests voor utils module."""

import unittest
from utils import greet, reverse_string, fibonacci


class TestUtils(unittest.TestCase):
    
    def test_greet(self):
        self.assertEqual(greet("World"), "Welkom bij World!")
        self.assertEqual(greet("Claude"), "Welkom bij Claude!")
    
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("Python"), "nohtyP")
    
    def test_fibonacci_empty(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(-1), [])
    
    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), [0])
    
    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])


if __name__ == "__main__":
    unittest.main()
