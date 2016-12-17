'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from StringsAndArrows import func


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(func('<--<<--<<\n'), 2)

    def testTwo(self):
        self.assertEqual(func('<<>>--><--<<--<<>>>--><'), 4)

    def testThree(self):
        self.assertEqual(func('<-->>'), 2)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
