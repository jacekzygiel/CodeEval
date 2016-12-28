import sys


def func(line):
    words = ['negative',
             'zero',
             'one',
             'two',
             'three',
             'four',
             'five',
             'six',
             'seven',
             'eight',
             'nine',
             'ten',
             'eleven',
             'twelve',
             'thirteen',
             'fourteen',
             'fifteen',
             'sixteen',
             'seventeen',
             'eighteen',
             'nineteen',
             'twenty',
             'thirty',
             'forty',
             'fifty',
             'sixty',
             'seventy',
             'eighty',
             'ninety',
             'hundred',
             'thousand',
             'million']

    line = line.rstrip('\n').split(' ')

    return line


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('TextToNumber.txt')
    except IOError:
        main(sys.argv[1])
