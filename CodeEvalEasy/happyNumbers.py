'''
Created on Nov 2, 2016

@author: zygielj
'''
import sys


# with open(sys.argv[1], 'r') as numbers:
with open('happyNumbers.txt', 'r') as numbers:
    for number in numbers:
        square = 0
        for digit in str(number):
                print digit
            # square += int(digit)**2
        print square
