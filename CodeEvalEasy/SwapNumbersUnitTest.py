'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from SwapNumbers import reverseWord


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(reverseWord(
            '4Always0 5look8 4on9 7the2 4bright8 9side7 3of8 5life5\n'),
            '0Always4 8look5 9on4 2the7 8bright4 7side9 8of3 5life5')

    def testTwo(self):
        self.assertEqual(reverseWord(
            '5Nobody5 7expects3 5the4 6Spanish4 9inquisition0\n'),
            '5Nobody5 3expects7 4the5 4Spanish6 0inquisition9')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
