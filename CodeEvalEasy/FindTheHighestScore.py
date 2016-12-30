import sys
import os


def func(line):
    line = line.rstrip('').split(' | ')
    line = [map(int, line[x].split(' ')) for x in range(len(line))]
    return ' '.join([str(max(zip(*line)[x])) for x in range(len(line[0]))])


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            print func(test)

if __name__ == '__main__':
    try:
        main('{}.txt'.format(os.path.basename(sys.argv[0])[:-3]))
    except IOError:
        main(sys.argv[1])
