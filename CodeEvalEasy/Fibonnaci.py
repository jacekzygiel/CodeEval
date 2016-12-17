'''
Created on Nov 2, 2016

@author: zygielj
'''
import sys


def fibo(number):
        if number <= 1:
            return number
        else:
            return fibo(number-1)+fibo(number-2)

with open(sys.argv[1], 'r') as lines:
    for line in lines:
        print fibo(int(line))
