import sys


def reverseWord(line):
    line = line.rstrip('\n').split(' ')
    swapLine = ''
    for item in line:
        start = item[0]
        stop = item[-1]
        item = stop + item[1:]
        item = item[:-1] + start
        swapLine += item + ' '
    return swapLine[:-1]


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = reverseWord(test)
            print result

if __name__ == '__main__':
    try:
        main('SwapNumbers.txt')
    except IOError:
        main(sys.argv[1])
