'''
Created on Nov 3, 2016

@author: zygielj
Topic:
'''
import sys


# with open(sys.argv[1], 'r') as lines:
with open('FindAWriter.txt', 'r') as lines:
    for line in lines:
        intNumbers = []
        writerName = ''
        name, numbers = line.split('|')
        numbers = numbers.split()

        for number in numbers:
            intNumbers.append(int(number))

        for x in intNumbers:
            writerName += name[x-1]
        print writerName

if __name__ == '__main__':
    pass
