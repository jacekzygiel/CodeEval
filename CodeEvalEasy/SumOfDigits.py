import sys


def sumOfDigits(number):
    output = 0
    # number = number.replace("\n", "")
    # for digit in number:
    #    output += int(digit)
    # output = sum(int(digit) for digit in number)
    output = sum(int(digit) for digit in number.replace("\n", ""))
    return output


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            sOD = sumOfDigits(test)
            print sOD

if __name__ == '__main__':
    try:
        main('SumOfDigits.txt')
    except IOError:
        main(sys.argv[1])
