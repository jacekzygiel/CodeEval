import sys
import string


def func(line):
    output = ''
    lc = string.ascii_lowercase[0:10]
    for element in line:
        if element.isdigit():
            output += element
        elif element.isalpha():
            number = lc.find(element)
            if number < 0:
                pass
            else:
                output += str(number)

    if len(output) == 0:
        output = 'NONE'
    return output


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('HiddenDigits.txt')
    except IOError:
        main(sys.argv[1])
