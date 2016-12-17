import sys


def get_bit(byte, idx):
    return ((byte & (1 << idx)) != 0)


def main(input_file):
    with open(input_file, 'r') as lines:
        for line in lines:
            lineElements = line.rstrip('\n').split(",")
            a = get_bit(int(lineElements[0]), int(lineElements[1])-1)
            b = get_bit(int(lineElements[0]), int(lineElements[2])-1)

            if a == b:
                print 'true'
            else:
                print 'false'


if __name__ == '__main__':
    try:
        main('BitPositions.txt')
    except IOError:
        main(sys.argv[1])
