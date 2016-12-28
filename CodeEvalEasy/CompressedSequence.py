import sys


def func(line):
    line = line.rstrip('\n').split(' ')
    count = 0
    output = ''
    lastNumber = line[0]

    for x in range(len(line)+1):
        if x == len(line):
            output += '{} {} '.format(count, lastNumber)
        else:
            if line[x] == lastNumber:
                count += 1
            else:
                output += '{} {} '.format(count, lastNumber)
                count = 1
                lastNumber = line[x]

    return output


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('CompressedSequence.txt')
    except IOError:
        main(sys.argv[1])
