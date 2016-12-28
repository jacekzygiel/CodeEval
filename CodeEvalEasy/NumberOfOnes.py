import sys


def func(line):
    return sum( 1 for x in bin(int(line)) if x == '1')


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('NumberOfOnes.txt')
    except IOError:
        main(sys.argv[1])
