import sys


def func(line):
    line = line.rstrip('\n').split(' ')
    return ' '.join([item[0].upper() + item[1:] if item[0].isalpha() else item
                     for item in line])


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('CapitalizeWords.txt')
    except IOError:
        main(sys.argv[1])
