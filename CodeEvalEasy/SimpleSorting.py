''' NOT PASS '''

import sys


def func(line):
    # line = line.rstrip('\n').split(' ')
    output = [float(n) for n in line.rstrip('\n').split(' ')]
    output.sort()
    outputString = ''
    for element in output:
        outputString += str(element) + ' '
    return outputString[:-1]
    #return " ".join(map(str, output))


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result[:-1]

if __name__ == '__main__':
    try:
        main('SimpleSorting.txt')
    except IOError:
        main(sys.argv[1])
