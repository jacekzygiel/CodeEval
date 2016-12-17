'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from StringMask import stringMask


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(stringMask('hello 11001/n'), 'HEllO')

    def testTwo(self):
        self.assertEqual(stringMask('world 10000/n'), 'World')

    def testThree(self):
        self.assertEqual(stringMask('cba 111/n'), 'CBA')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
