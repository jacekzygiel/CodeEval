import sys


def getKey(item):
    return item[0]


def func(testCase):
    tab = []
    lineLong = []
    [lineLong.append([len(tab[x]), x]) for x in range(1, len([tab.append(line.rstrip()) for line in testCase]))]
    return '\n'.join([tab[(sorted(lineLong, key=getKey, reverse=True))[y][1]]
                      for y in range(int(tab[0]))])


def main(input_file):
        print func(open(input_file, 'r'))

if __name__ == '__main__':
    try:
        main('LongestLines.txt')
    except IOError:
        main(sys.argv[1])
