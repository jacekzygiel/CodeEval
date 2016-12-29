import sys
import os

def func(line):
    line = line.rstrip('\n').split(' ')
    for item in line:
        output = 1
    return output


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('{}.txt'.format(os.path.basename(sys.argv[0])[:-3]))
    except IOError:
        main(sys.argv[1])
