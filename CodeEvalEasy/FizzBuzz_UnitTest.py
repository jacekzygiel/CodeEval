'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from FizzBuzz import fizzBuzz


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(fizzBuzz('3 5 10\n'), '1 2 F 4 B F 7 8 F B')

    def testTwo(self):
        self.assertEqual(fizzBuzz('2 7 15\n'),
                         '1 F 3 F 5 F B F 9 F 11 F 13 FB 15')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
