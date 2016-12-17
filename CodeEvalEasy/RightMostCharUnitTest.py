import unittest
from RightMostChar import func


class Test(unittest.TestCase):

    def testOne(self):
        self.assertEqual(func('Hello World,r\n'), 8)

    def testTwo(self):
        self.assertEqual(func('Hello CodeEval,E\n'), 10)

    def testThree(self):
        self.assertEqual(func('How to learn to Cook,C\n'), 16)

    def testFour(self):
        self.assertEqual(func('y5gXmbtfkrKj9rurEv8ywOUA1gqS7dwE7jn314eNHHe7s'
                              'lTsqI0,5\n'), 2)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
