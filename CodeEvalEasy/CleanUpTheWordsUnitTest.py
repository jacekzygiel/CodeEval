'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from CleanUpTheWords import cleanUp


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(cleanUp('(--9Hello----World...--)\n'), 'hello world')

    def testTwo(self):
        self.assertEqual(cleanUp('Can 0$9 ---you~\n'), 'can you')

    def testThree(self):
        self.assertEqual(cleanUp('13What213are;11you-123+138doing7\n'), 'what are you doing')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
