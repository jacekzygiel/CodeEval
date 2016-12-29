import sys


def prime(number):
    y = 2
    if number < 2:
        return False
    while y < number:
        if number % y == 0:
            return False
        y += 1
    return True


def func(line):
    line = map(int, line.rstrip('\n').split(','))
    primes = 0;
    for x in range(line[0], line[1]+1):
        if prime(x) == True:
            primes += 1
    return primes


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('CountingPrimes.txt')
    except IOError:
        main(sys.argv[1])
