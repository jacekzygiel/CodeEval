'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from OneZeroTwoZeros import func


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(func('1 8\n'), 3)

    def testTwo(self):
        self.assertEqual(func('2 4\n'), 1)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
