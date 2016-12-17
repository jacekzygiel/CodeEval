import sys


def func(line):
    line = line.rstrip('\n').split(';')
    inter0 = line[0].split(',')
    inter1 = line[1].split(',')

    output = ''
    for x in range(len(inter0)):
        for y in range(len(inter1)):
            if inter0[x] == inter1[y] and inter0[x] != ',':
                output += inter0[x] + ','

    return output[:-1]


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('SetIntersection.txt')
    except IOError:
        main(sys.argv[1])
