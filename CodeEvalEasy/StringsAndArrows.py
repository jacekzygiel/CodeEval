import sys
import re


def func(line):
    arrowRight = '>>->'
    arrowLeft = '<-<<'
    line = line.rstrip('\n')
    check = ''
    AR = line.count(arrowRight)
    arrowsNumber = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(arrowRight), line))

    return AR


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('StringsAndArrows.txt')
    except IOError:
        main(sys.argv[1])
