'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from MultiplesOfANumber import func


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(func('13,8\n'), 16)

    def testTwo(self):
        self.assertEqual(func('17,16\n'), 32)

    def testThree(self):
        self.assertEqual(func('1598,2\n'), 1598)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
