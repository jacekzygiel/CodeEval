import sys


def func(line):
    letters = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    for element in line:
        print element
    return 1


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('TelephoneWords.txt')
    except IOError:
        main(sys.argv[1])
