'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from SetIntersection import func


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(func('1,2,3,4;4,5,6'), '4')

    def testTwo(self):
        self.assertEqual(func('20,21,22;45,46,47'), '')

    def testThree(self):
        self.assertEqual(func('7,8,9;8,9,10,11,12'), '8,9')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
