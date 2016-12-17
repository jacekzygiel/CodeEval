'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from FirstNonRepeatedCharacter import func


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(func('yellow'), 'y')

    def testTwo(self):
        self.assertEqual(func('tooth'), 'h')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
