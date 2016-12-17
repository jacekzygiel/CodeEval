'''
Created on Nov 3, 2016

@author: zygielj
'''
import sys


# with open(sys.argv[1], 'r') as lines:
with open('DecimalToBinary.txt', 'r') as lines:
    for line in lines:
        print str(bin(int(line)))[2:]

if __name__ == '__main__':
    pass
