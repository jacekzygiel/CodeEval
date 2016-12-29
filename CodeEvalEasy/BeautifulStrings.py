import sys
import string


def func(line):
    values = []
    chars = string.ascii_lowercase
    value = 0
    for x in range(1, 27):
        values.append(x)
    for element in line.rstrip().lower():
        a = chars.index(element)
        b = values[a]
        value += 1

    return value


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('BeautifulStrings.txt')
    except IOError:
        main(sys.argv[1])
