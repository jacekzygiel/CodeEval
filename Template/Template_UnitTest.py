'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest

from CodeEvalEasy.MultipliactionTable import func


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(func(5), 6)

    def testTwo(self):
        self.assertEqual(func(4), 8)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
