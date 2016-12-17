import sys


def main(input_file):
    with open(input_file, 'r') as lines:
        for line in lines:
            digits = []
            strings = []
            printStrings = ''
            printDigits = ''
            # rstrip removes trailing characters
            line = line.rstrip('\n').split(',')

            for item in line:
                if item.isdigit():
                    digits.append(item)
                else:
                    strings.append(item)
            for x in strings:
                printStrings += (x + ',')

            for y in digits:
                printDigits += (y + ',')

            printDigits = printDigits[:-1]
            printStrings = printStrings[:-1]

            if printDigits == '':
                print('{}'.format(printStrings))
            elif printStrings == '':
                print('{}'.format(printDigits))
            else:
                print('{}|{}'.format(printStrings, printDigits))

if __name__ == '__main__':
    try:
        main('MixedContent.txt')
    except IOError:
        main(sys.argv[1])
