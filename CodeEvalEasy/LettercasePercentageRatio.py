import sys


def func(line):
    upper = 0.0
    lower = 0.0
    for letter in line:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
    return "lowercase: {:.2f} uppercase: {:.2f}".format((100 / (upper + lower)) * lower,
                                                        (100 / (upper + lower)) * upper)


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('LettercasePercentageRatio.txt')
    except IOError:
        main(sys.argv[1])
