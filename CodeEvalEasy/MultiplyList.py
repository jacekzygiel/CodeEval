import sys


def func(line):
    line = line.rstrip('\n').split(' | ')
    line[0] = [int(n) for n in line[0].split(" ")]
    line[1] = [int(n) for n in line[1].split(" ")]
    output = []
    output.append([line[0][element] * line[1][element] for element in range(len(line[0]))])
    return " ".join([str(x) for x in output[0]])


def main(input_file):
    with open(input_file, 'r') as testCases:
        for test in testCases:
            result = func(test)
            print result

if __name__ == '__main__':
    try:
        main('MultiplyList.txt')
    except IOError:
        main(sys.argv[1])
