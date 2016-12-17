import sys
#import datetime


def func(line):
    timestamps = sorted(line.rstrip('\n').split(' '), reverse=True)
    return ' '.join(timestamps)


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('TimeToEat.txt')
    except IOError:
        main(sys.argv[1])
