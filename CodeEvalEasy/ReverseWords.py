import sys


def reverseWord(line):
    result = ''
    line = line.rstrip('\n').split(' ')

    for word in reversed(line):
        result += (str(word) + ' ')
    return result[:-1]


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = reverseWord(test)
            print result

if __name__ == '__main__':
    try:
        main('ReverseWords.txt')
    except IOError:
        main(sys.argv[1])
