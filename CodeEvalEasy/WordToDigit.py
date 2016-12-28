import sys


def func(line):
    alphaToDigit = {'zero': 0,
                    'one': 1,
                    'two': 2,
                    'three': 3,
                    'four': 4,
                    'five': 5,
                    'six': 6,
                    'seven': 7,
                    'eight': 8,
                    'nine': 9}

    line = line.rstrip().split(';')
    return ''.join([str(alphaToDigit[x]) for x in line])


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('WordToDigit.txt')
    except IOError:
        main(sys.argv[1])
