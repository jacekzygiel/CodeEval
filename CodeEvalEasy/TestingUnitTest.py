'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from Testing import func


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(func('Heelo Codevval | Hello Codeeval'), 'Low')

    def testTwo(self):
        self.assertEqual(func('hELLO cODEEVAL | Hello Codeeval'), 'Critical')

    def testThree(self):
        self.assertEqual(func('Hello Codeeval | Hello Codeeval'), 'Done')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
