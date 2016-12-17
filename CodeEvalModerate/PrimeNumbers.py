'''
Created on Nov 3, 2016

@author: zygielj
'''
import sys


def prime(number):
    y = 2
    if number < 2:
        return False
    while y < number:
        if number % y == 0:
            return False
        y += 1
    return True


def main():
    # with open(sys.argv[1], 'r') as lines:
    with open('PrimeNumbers.txt', 'r') as lines:
        for line in lines:
            output = ''
            for number in range(int(line)):
                if prime(number) == True:
                    output += str(number) + ','
            print output[:-1]

if __name__ == '__main__':
    main()
