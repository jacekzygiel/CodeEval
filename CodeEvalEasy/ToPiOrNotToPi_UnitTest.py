'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from ToPiOrNotToPi import func


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(func('3'), '4')

    def testTwo(self):
        self.assertEqual(func('1'), '3')

    def testThree(self):
        self.assertEqual(func('1654'), '1')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
