import unittest
import sys
# sys.path is a list of absolute path strings
sys.path.append('../')
from first_module import *

class TestSuma(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2,2),4)
        self.assertNotEqual(sum(2,2),5)

class TestMatMul(unittest.TestCase):
    def test_matmul(self):
        self.assertEqual(matmul([[1,2],[4,5]], [[8,3,5],[4,7,3]]), [[16, 17, 11],[52, 47, 35]])
        self.assertEqual(matmul([[1,2,3],[4,5,3],[1,2,3]], [[8,3,1],[7,3,1],[2,3,2]]), [[28, 18,  9],[73, 36, 15],[28, 18,  9]])