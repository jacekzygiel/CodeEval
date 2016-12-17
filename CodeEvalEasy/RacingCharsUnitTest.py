'''
Created on Nov 9, 2016

@author: zygielj
'''
import unittest
from RacingChars import main


class Test(unittest.TestCase):

    def testOne(self):
        textIn = '''
        #########_##
        ########C_##
        #######_####
        ######_#C###
        #######_C###
        #######_####
        ######C#_###
        ######C_####
        #######_####
        #######_####
        '''

        textOut = '''
        #########|##
        ########/_##
        #######/####
        ######_#\###
        #######_|###
        #######/####
        ######/#_###
        ######|_####
        #######\####
        #######|####
        '''
        self.assertEqual(main('RacingChars.txt'), textOut)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
