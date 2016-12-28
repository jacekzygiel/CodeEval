import sys


def func(line):
    line = line.rstrip('\n').split(',')
    return line[0].rfind(line[1])


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('RightMostChar2.txt')
    except IOError:
        main(sys.argv[1])
