'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from SumOfDigits import sumOfDigits


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(sumOfDigits('23'), 5)

    def testTwo(self):
        self.assertEqual(sumOfDigits('496'), 19)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
