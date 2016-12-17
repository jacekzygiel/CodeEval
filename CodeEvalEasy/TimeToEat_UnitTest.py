'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from TimeToEat import func


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(func(
            '02:26:31 14:44:45 09:53:27\n'),
            '14:44:45 09:53:27 02:26:31')

    def testTwo(self):
        self.assertEqual(func('05:33:44 21:25:41'), '21:25:41 05:33:44')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
