import sys


def func(line):
    line = line.rstrip('\n').split(', ')
    return ''.join([x for x in line[0] if x not in line[1]])


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('RemoveCharacters.txt')
    except IOError:
        main(sys.argv[1])
