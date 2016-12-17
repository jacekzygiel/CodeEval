''' SOLVED - UNITTEST DON'T WORK'''
import sys


def func(line, lastIndex):
    line = line.rstrip('\n')
    index = 0
    s = list(line)
    for element in line:
        if 'C' in line:
            if element == 'C':
                if lastIndex == -1 or lastIndex == index:
                    s[index] = "|"
                    return "".join(s), index
                elif lastIndex > index:
                    s[index] = "/"
                    return "".join(s), index
                elif lastIndex < index:
                    s[index] = "\\"
                    return "".join(s), index
        else:
            if element == '_':
                if lastIndex == -1 or lastIndex == index:
                    s[index] = "|"
                    return "".join(s), index
                elif lastIndex > index:
                    s[index] = "/"
                    return "".join(s), index
                elif lastIndex < index:
                    s[index] = "\\"
                    return "".join(s), index
        index += 1


def main(input_file):
    with open(input_file, 'r') as testCases:
        lastIndex = -1
        for test in testCases:
            result, lastIndex = func(test, lastIndex)
            print result

if __name__ == '__main__':
    try:
        main('RacingChars.txt')
    except IOError:
        main(sys.argv[1])
