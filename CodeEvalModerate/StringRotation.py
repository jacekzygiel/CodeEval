import sys


def func(line):
    line = line.rstrip('\n').split(',')
    for x in line[0]:
        c = line[1].find(x)
        if c == -1:
            return False
        else:
            line[1] = line[1].replace(x, '', 1)
    if len(line[1]) != 0:
        return False
    return True


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('StringRotation.txt')
    except IOError:
        main(sys.argv[1])
