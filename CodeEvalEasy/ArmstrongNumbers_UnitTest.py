'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from ArmstrongNumbers import func


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(func('6\n'), True)

    def testTwo(self):
        self.assertEqual(func('153\n'), True)

    def testThree(self):
        self.assertEqual(func('351\n'), False)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
