import sys


def func(line):
    line = line.rstrip('\n').split(',')

    x = int(line[0])
    y = int(line[1])
    multiply = 1
    result = 0

    while result < x:
        multiply += 1
        result = y * multiply

    return result


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('MultiplesOfANumber.txt')
    except IOError:
        main(sys.argv[1])
