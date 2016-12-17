import sys


def fizzBuzz(line):
    line = line.rstrip('\n').split(' ')
    result = ''

    for x in range(1, int(line[2])+1):
        if x % int(line[0]) == 0 and x % int(line[1]) == 0:
            result += 'FB '
        elif x % int(line[0]) == 0:
            result += 'F '
        elif x % int(line[1]) == 0:
            result += 'B '
        else:
            result += (str(x) + ' ')
    return result[:-1]


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = fizzBuzz(test)
            print result

if __name__ == '__main__':
    try:
        main('FizzBuzz.txt')
    except IOError:
        main(sys.argv[1])
