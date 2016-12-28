import sys
from datetime import datetime


def func(line):
    line = line.rstrip('\n').split(' ')
    FMT = '%H:%M:%S'
    if line[0] > line[1]:
        delta = datetime.strptime(line[0], FMT) - datetime.strptime(line[1], FMT)
    else:
        delta = datetime.strptime(line[1], FMT) - datetime.strptime(line[0], FMT)
    return '{:02d}:{:02d}:{:02d}'.format(delta.seconds / 3600, (delta.seconds / 60) % 60, delta.seconds % 60)

def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('DeltaTime.txt')
    except IOError:
        main(sys.argv[1])
