import sys


def func(line):
    numberCount = 0
    line = line.rstrip('\n').split(' ')

    for x in range(1, int(line[1])):
       zeros =  sum([1 for element in bin(x)[2:] if int(element) == 0])
       if zeros == int(line[0]):
           numberCount += 1
    return numberCount


def main(input_file):
    with open(input_file, 'r') as testCases:3
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('OneZeroTwoZeros.txt')
    except IOError:
        main(sys.argv[1])
