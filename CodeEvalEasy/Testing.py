import sys


def func(line):
    line = line.rstrip('\n').split('|')
    right = line[1]
    check = line[0]
    right = right[1:]
    check = check[:-1]
    fails = 0

    for x in range(len(right)):
        if check[x] != right[x]:
            fails += 1

    if fails == 0:
        return 'Done'
    elif fails > 6:
        return 'Critical'
    elif fails > 4 and fails <= 6:
        return 'High'
    elif fails > 2 and fails <= 4:
        return 'Medium'
    if fails >= 2:
        return 'Low'


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('Testing.txt')
    except IOError:
        main(sys.argv[1])
