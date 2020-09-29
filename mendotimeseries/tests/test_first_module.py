import unittest
import sys
import numpy

# sys.path is a list of absolute path strings
sys.path.append('../')
from mendotimeseries.first_module import *

class TestSuma(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(2,2),4)
        self.assertNotEqual(sum(2,2),5)

class TestMatMul(unittest.TestCase):
    def test_matmul(self):
        self.assertEqual(matmul([[1,2],[4,5]], [[8,3,5],[4,7,3]]), [[16, 17, 11],[52, 47, 35]])
        self.assertEqual(matmul([[1,2,3],[4,5,3],[1,2,3]], [[8,3,1],[7,3,1],[2,3,2]]), [[28, 18,  9],[73, 36, 15],[28, 18,  9]])

class TestRW(unittest.TestCase):
    def test_rw(self):
        self.assertEqual(len(randomwalk(10)),10)
        self.assertEqual(isinstance(randomwalk(10), np.ndarray), True)

class TestMax(unittest.TestCase):
    def test_max(self):
    	self.assertEqual(max([1,2,5,8,3,4,6]),8)
    	self.assertEqual(isinstance(max([1,2,5,8,3,4,6]), int),True)
