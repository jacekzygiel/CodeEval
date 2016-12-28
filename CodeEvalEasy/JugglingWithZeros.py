import sys


def func(line):
    line = line.rstrip('\n').split(' ')
    flags = line[::2]
    values = line[1::2]
    output = ''
    for x in range(0, len(flags)):
        if flags[x] == '00':
            output += ''.join(['1' for x in values[x]])
        elif flags[x]== '0':
            output += ''.join(['0' for x in values[x]])
    return int(output, 2)

def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('JugglingWithZeros.txt')
    except IOError:
        main(sys.argv[1])
