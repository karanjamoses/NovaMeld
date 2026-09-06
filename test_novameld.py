# test_novameld.py
"""
Tests for NovaMeld module.
"""

import unittest
from novameld import NovaMeld

class TestNovaMeld(unittest.TestCase):
    """Test cases for NovaMeld class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NovaMeld()
        self.assertIsInstance(instance, NovaMeld)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NovaMeld()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
