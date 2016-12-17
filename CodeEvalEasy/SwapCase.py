'''
Created on Nov 3, 2016

@author: zygielj
'''
import sys


# with open(sys.argv[1], 'r') as strings:
with open('SwapCase.txt', 'r') as lines:
    swapCaseLetters = [line.swapcase() for line in lines]
    swapCase = ''
    for line in swapCaseLetters:
        swapCase += line
    print swapCase


# Option 2
'''    data = ''
    for line in lines:
        lineToPrint = ''
        lineToPrint += line.swapcase()
        data += lineToPrint
    print data
'''


# Option 3
'''        for char in line:
            if char.islower():
                swapChar = char.upper()
            elif char.isupper():
                swapChar = char.lower()
            else:
                swapChar = char

'''

if __name__ == '__main__':
    pass
