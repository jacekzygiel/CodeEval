'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from SimpleSorting import func


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(func('70.920 -38.797 14.354 99.323 90.374 7.581\n')
                         , '-38.797 7.581 14.354 70.920 90.374 99.323')

    def testTwo(self):
        self.assertEqual(func('-37.507 -3.263 40.079 27.999 65.213 -55.552\n')
                         , '-55.552 -37.507 -3.263 27.999 40.079 65.213')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
