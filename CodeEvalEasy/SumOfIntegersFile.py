'''
Created on Nov 2, 2016

@author: zygielj
'''
import sys


intsum = 0
with open(sys.argv[1], 'r') as numbers:
    for number in numbers:
        intsum += int(number)
    print intsum

if __name__ == '__main__':
    pass
