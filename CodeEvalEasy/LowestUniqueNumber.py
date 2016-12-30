import sys
import os


def func(line):
    line = map(int, line.rstrip().split(' '))
    ones = []
    [ones.append(element) for element in list(set(line)) if line.count(element) == 1 ]
    return line.index(min(ones))+1 if len(ones) != 0 else 0


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            print func(test)

if __name__ == '__main__':
    try:
        main('{}.txt'.format(os.path.basename(sys.argv[0])[:-3]))
    except IOError:
        main(sys.argv[1])
