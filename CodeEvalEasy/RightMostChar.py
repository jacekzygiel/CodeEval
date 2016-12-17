import sys


def func(line):
    line = line.rstrip('\n').split(',')
    findIn = line[0][::-1]
    toFind = line[1]
    position = findIn.find(toFind)

    toFindLen = len(findIn)
    output = toFindLen - position - 1
    if output == 1:
        return output + 1
    return output


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('RightMostChar.txt')
    except IOError:
        main(sys.argv[1])
