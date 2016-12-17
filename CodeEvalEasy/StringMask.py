import sys


def stringMask(line):
    line = line.rstrip('\n').split(' ')
    word = line[0]
    mask = line[1]
    output = ''

    for x in range(len(mask)):
        if mask[x] == '1':
            output += word[x].upper()
        elif mask[x] == '0':
            output += word[x].lower()

    return output


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = stringMask(test)
            print result

if __name__ == '__main__':
    try:
        main('StringMask.txt')
    except IOError:
        main(sys.argv[1])
