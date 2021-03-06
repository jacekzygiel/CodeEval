import sys


def func(line):
    line = line.rstrip('\n')
    output = sum( int(item)**len(line) for item in line)
    return True if int(line) == output else False


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('ArmstrongNumbers.txt')
    except IOError:
        main(sys.argv[1])
