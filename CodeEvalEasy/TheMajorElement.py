import sys


def func(line):
    line = line.rstrip('\n').split(',')
    objects = list(set(line))
    a = 1
    baza = []
    for object in objects:
        c = line.count(object)
        b = object

    return b


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('TheMajorElement.txt')
    except IOError:
        main(sys.argv[1])
