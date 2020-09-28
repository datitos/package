import unittest
import sys
# sys.path is a list of absolute path strings
sys.path.append('../')
from module_sum import *

class TestSuma(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2,2),4)
        self.assertNotEqual(sum(2,2),5)