'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from ReverseWords import reverseWord


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(reverseWord('Hello World\n'), 'World Hello')

    def testTwo(self):
        self.assertEqual(reverseWord('Hello CodeEval\n'), 'CodeEval Hello')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
