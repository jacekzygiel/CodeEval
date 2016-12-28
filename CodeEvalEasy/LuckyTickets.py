import sys


def luckyTickets():
    tabu = []
    number = 4
    equals = 0

    for x in range(int('1{}'.format('0'*number))):
        if x < int('1{}'.format('0'*(number-3))):
            tabu.append('{}{}'.format('0'*(number-1), x))
        elif x < 100:
            tabu.append('{}{}'.format('0'*(number-2), x))
        elif x < 1000:
            tabu.append('{}{}'.format('0'*(number-3), x))
        elif x < 10000:
            tabu.append('{}{}'.format('0'*(number-4), x))
    print tabu

    for y in range(len(tabu)):
        sumA = 0
        sumB = 0

        for z in range(0, number/2):
            sumA += int(tabu[y][z])

        for k in range(number/2, number):
            sumB += int(tabu[y][k])

        if sumA == sumB:
            equals += 1;

    print equals


def func(line):
    line = line.rstrip('\n').split(' ')
    for item in line:
        output = 1
    return output


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result
    

if __name__ == '__main__':
    luckyTickets()
    try:
        main('LongestLines.txt')
    except IOError:
        main(sys.argv[1])
  