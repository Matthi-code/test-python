"""Tests voor main module."""

import unittest
from io import StringIO
from unittest.mock import patch

from main import main


class TestMain(unittest.TestCase):
    
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_output(self, mock_stdout):
        main()
        output = mock_stdout.getvalue()
        
        # Check greeting
        self.assertIn("Welkom bij Claude-dev!", output)
        
        # Check calculations
        self.assertIn("10 + 5 = 15", output)
        self.assertIn("10 - 5 = 5", output)
        self.assertIn("10 * 5 = 50", output)
        self.assertIn("10 / 5 = 2.0", output)
        
        # Check prime checks
        self.assertIn("Is 17 prime? True", output)
        self.assertIn("Is 18 prime? False", output)


if __name__ == "__main__":
    unittest.main()
