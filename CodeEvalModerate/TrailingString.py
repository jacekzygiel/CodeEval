import sys


def func(line):
    line = line.rstrip('\n').split(',')
    return 1 if line[0][len(line[0]) - len(line[1]):] == line[1] else 0


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('TrailingString.txt')
    except IOError:
        main(sys.argv[1])
