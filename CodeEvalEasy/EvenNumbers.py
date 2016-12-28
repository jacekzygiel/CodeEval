import sys


def func(line):
    return 1 if int(line) % 2 == 0 else 0


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('EvenNumbers.txt')
    except IOError:
        main(sys.argv[1])
